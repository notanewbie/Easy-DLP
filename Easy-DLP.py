import yt_dlp

print('EASY DLP')
print('=================')
print('')
print('Based on "youtube" by bmcs-ux    ')
print('')
print('=================')

print('')
#print ('[pastekan link]')

url = input ('link youtube:')
print("download    :" + url )

def menu():
	print('[1]. download video')
	print('[2]. download audio')
	

def baik():
	print('- download video')
	ydl_options = {'format': 'bestvideo[ext=webm]+bestaudio[ext=m4a]/bestvideo+bestaudio', 'merge-output-format': 'mp4', 'newline': True}
	with yt_dlp.YoutubeDL(ydl_options) as ydl:
		ydl.download([url])
	
def duet():
	print('- download audio')
	info = youtube_dl.YoutubeDL().extract_info(
	url = url,download = False)
		
	namafile = f"{info['title']}.mp3"
	options={'format': 'bestaudio/audio','keepvideo' :False,'outtmpl':namafile}
	
	with yt_dlp.YoutubeDL(options) as ydl:
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
