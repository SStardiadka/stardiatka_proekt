from urllib.request import urlopen

s = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html").read().decode('utf-8')
a = __import__('re').findall(r'<td>.* (\d+) .*<\/td>', s)
print(sum(map(int, a)))
print(s)