from PIL import Image

img = Image.open(r"C:\Users\user\Desktop\nt.png")
res = img.rotate(70)
res.save(r"C:\Users\user\Desktop\res.png")
