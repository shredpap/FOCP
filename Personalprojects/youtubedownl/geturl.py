import os
try:
    from pytube import Playlist
    from art import *
except ModuleNotFoundError:
    os.system("pip install pytube")
    os.system("pip install art")
    os.system("pip install youtube-dl")
def get_playlist(playlists):
    urls=[]
    for playlist in playlists:
        playlists_url=Playlist(playlist)
        for url in playlists_url:
            urls.append(url)
    return urls
playlist=["https://youtube.com/playlist?list=PL779Lo_LkzYoXYzbakiMHT6URW7jdCZom"]
a="temp"
# for i in range(1):
    # a=input("Enter playlist link: ")
    # playlist.append(a)
pl_url=get_playlist(playlist)
with open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Personalprojects\youtubedownl\link.txt","w") as f:
    for url in pl_url:
        # print(url)
        f.write(url+"\n")
print("Successful...")