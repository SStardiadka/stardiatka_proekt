import pyshorteners
s = pyshorteners.Shortener()
url = r'https://www.kufar.by/item/168855228'
qwe = s.tinyurl.short(url)
print(qwe)
# укорачивает ссылку