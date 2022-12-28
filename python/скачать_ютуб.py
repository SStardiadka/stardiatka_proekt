# скачать ютуб видио
from pytube import YouTube
link = r'https://youtu.be/ntUvSEEhRUA'
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download(r'C:\stardiatka_proekt-1\python\Wfiles')
print('ok')