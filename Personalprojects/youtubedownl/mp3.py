import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"C:\Users\Shreyash Parajuli\Desktop\boulevard of broken dreams cover\V1.mp3")
my_clip.audio.write_audiofile(r"C:\Users\Shreyash Parajuli\Desktop\boulevard of broken dreams cover\my_result.mp3")