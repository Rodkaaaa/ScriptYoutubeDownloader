from pytube import YouTube

SAVE_PATH =' C:/Users/Rodka/Desktop/Programacion/py/Youtue'

link = input("Ingrese el link:")

yt = YouTube(link)

""" ys = yt.streams.get_highest_resolution() """
ys = yt.streams.get_audio_only("mp4")

print("downloading...")
ys.download()
print("downloaded")