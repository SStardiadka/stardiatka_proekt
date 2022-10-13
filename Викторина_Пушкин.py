# Викторина_Пушкин
from gtts import gTTS
import pyglet
text = 'Введите год рождения А.С. Пушкина'
obj = gTTS(text, lang='ru')
obj.save('hw2.mp3')
golos = pyglet.media.load(r'C:\stardiatka_proekt\hw2.mp3')
golos.play()
question = input('Введите год рождения А.С. Пушкина: ')
while question != '1799':
    text = 'НЕ верно. Попробуй еще'
    obj = gTTS(text, lang='ru')
    obj.save('hw1.mp3')
    golos = pyglet.media.load(r'C:\stardiatka_proekt\hw1.mp3')
    golos.play()
    question = input('НЕ верно. Попробуй еще')
if question == '1799':
    text = 'Классно!!! А день и месяц его рождения знаешь?'
    obj = gTTS(text, lang='ru')
    obj.save('hw3.mp3')
    golos = pyglet.media.load(r'C:\stardiatka_proekt\hw3.mp3')
    golos.play()
    print('Классно!!! А день и месяц его рождения знаешь?')
birthday = input()
while birthday != '6.06' and birthday != '6 июня':
    text = 'Неверный день рождения.Подумай еще.'
    obj = gTTS(text, lang='ru')
    obj.save('hw4.mp3')
    golos = pyglet.media.load(r'C:\stardiatka_proekt\hw4.mp3')
    golos.play()
    birthday = input('Неверный день рождения.Подумай еще.')
if birthday == ('6.06') or birthday == ('6 июня'):
    text = 'Верно. Молодец!'
    obj = gTTS(text, lang='ru')
    obj.save('hw5.mp3')
    golos = pyglet.media.load(r'C:\stardiatka_proekt\hw5.mp3')
    golos.play()
    print('Верно. Молодец')
print('end')