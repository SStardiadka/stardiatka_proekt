#  создать кюар-код для ссылки
import qrcode

data = "https://www.youtube.com/channel/UCQFGE9LvAdlEXCTr5rnBj2A"

filaname = "zvezdodinka.png"

img = qrcode.make(data)

img.save(filaname)
