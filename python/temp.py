import mechanize
br = mechanize.Browser()
br.open("https://www.kufar.by/")
for i in br.forms():
    print(i)