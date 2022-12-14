import os
from gtts import gTTS

def zapret_bykvi(name):   
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    str = name + ' запретил букву'
    lst = []
    for i in alf:
        if i in str:

            lst.append(str + ' ' + i +'\n')
            str = str.replace(i, '')
            str= ' '.join(str.split())
    a = ''.join(lst)
    return a
name = input()
print(zapret_bykvi(name))

text =  (f"{zapret_bykvi(name)}")
obj = gTTS(text, lang='ru')
obj.save(r'C:\stardiatka_proekt\python\mp3\zapret_bukva.mp3')
os.system(r'C:\stardiatka_proekt\python\mp3\zapret_bukva.mp3')