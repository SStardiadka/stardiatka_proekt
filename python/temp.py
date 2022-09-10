from urllib.request import urlopen
import re
s = urlopen("https://www.kufar.by/l/r~mogilev/videokarty").read().decode('utf-8')
a = re.findall(r'class=\"styles_title__wj__Y\">(.+?)</h3><p class|<span>(\d+)', s)
with open(r'Wfiles\data.txt','w', encoding="utf-8") as out:
    print(s, file=out)