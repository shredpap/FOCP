# import pafy
# from pytube import YouTube
# import os
file=open(r'C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Personalprojects\youtubedownl\links.txt','r')

# destination = r"C:\Users\Shreyash Parajuli\Music\Songs"
# for line in file:
#     yt=line
#     try:
#         # video=pafy.new(url)
#         # bestaudio=video.getbestaudio()
#         # print(video.title)
#         # bestaudio.download()
#         video = yt.streams.filter(only_audio=True).first()
#         out_file = video.download(output_path=destination)
#         base, text = os.path.splitext(out_file)
#         new_file = base + '.mp3'
#         os.rename(out_file, new_file)
#         print(yt.title + " has been successfully downloaded.")
#     except:
#         pass
# file.close()
a=[]
for i in file:
    a.append(i)
file.close()
print(a)