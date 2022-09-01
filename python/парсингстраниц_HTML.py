from urllib.request import urlopen
import re
s = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html").read().decode('utf-8')
a = re.findall(r'<td>.* (\d+) .*<\/td>', s)
print(sum(map(int, a)))
print(s)