# скачать ютуб видиo
from pytube import YouTube
import time
from tqdm import tqdm

mylist = ["ok"]
for i in tqdm(mylist):
    yt = YouTube(r"https://youtu.be/B5GNie5w8lQ")
    ys = yt.streams.get_highest_resolution()
    ys.download(r"C:\stardiatka_proekt-1\python\Wfiles")
    print(i)
