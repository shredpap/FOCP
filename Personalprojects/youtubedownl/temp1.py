import os
try:
    from pytube import YouTube
    from art import *
except ModuleNotFoundError:
    os.system("pip install pytube")
    os.system("pip install art")
    os.system("pip install youtube-dl")
# addr=input("Enter File name to be created: ")
file=open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Personalprojects\youtubedownl\link.txt",'r')
a=[]
for i in file:
    a.append(i[:-1])
file.close()
print(a)
count=0
for k in a:
    try:
        yt=YouTube(k)
        video = yt.streams.filter(only_audio=True).first()
        # destination = r"C:\Users\Shreyash Parajuli\Music\Songs"
        destination = r"C:\Users\Shreyash Parajuli\Desktop\boulevard of broken dreams cover"
        out_file = video.download(output_path=destination)
        base, text = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        count+=1
        print(count,"--> "+yt.title + " has been successfully downloaded.")
    except FileExistsError:
        print(count,"--> ",FileExistsError)
        count+=1

tprint("Shred")
