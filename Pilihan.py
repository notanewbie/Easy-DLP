import youtube_dl

print('YOUTUBE DOWNLODER')
print('=================')
print('')
print('author : BIMA    ')
print('')
print('=================')

nama = input ('siapa namamu? :')
print('')
print("    Halo " + nama)
print('')
print ('[pastekan link]')

url = input ('link youtube:')
print("download    :" + url )

def menu():
	print('[1]. download video')
	print('[2]. download audio')
	

def baik():
	print('- download video')
	ydl_options = {}
	with youtube_dl.YoutubeDL(ydl_options) as ydl:
		ydl.download([url])
	
def duet():
	print('- download audio')
	info = youtube_dl.YoutubeDL().extract_info(
	url = url,download = False)
		
	namafile = f"{info['title']}.mp3"
	options={'format': 'bestaudio/audio','keepvideo' :False,'outtmpl':namafile,
	}
	
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([info['webpage_url']])
		

menu()

def index():			
    opsi = input('pilih:')

    if opsi == "1":
	     baik()

    elif opsi == "2":
     	duet()
	
    else:
    	print('[DANCOK SENG PENER COK LEK MILEH!!!]')
    	
if __name__=='__main__':
	
	while (True):
		index()