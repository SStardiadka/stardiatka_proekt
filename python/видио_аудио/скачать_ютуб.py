# скачать ютуб видиo
from pytube import YouTube
# import tpip installime
from tqdm import tqdm


yt = YouTube(r"https://www.youtube.com/watch?v=Du2MUFuGnsI")
ys = yt.streams.get_highest_resolution()
ys.download()
print("end of download")
