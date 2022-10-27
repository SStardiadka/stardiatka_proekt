
from gtts import gTTS
import os
text = 'Введите год рождения А.С. Пушкина'
# obj = gTTS(text, lang='ru')
# obj.save('hw2.mp3')
os.system(r'C:\stardiatka_proekt\python\mp3\viktorina_pychkin\hw1.mp3')
question = input('Введите год рождения А.С. Пушкина:')
while question != '1799':
    print('НЕ верно. Попробуй еще')
    text = 'НЕ верно. Попробуй еще'
    # obj = gTTS(text, lang='ru')
    # obj.save('hw1.mp3')
    os.system(r'C:\stardiatka_proekt\python\mp3\viktorina_pychkin\hw2.mp3')
    question = input('НЕ верно. Попробуй еще')
if question == '1799':
    text = 'Классно!!! А день и месяц его рождения знаешь?'
    # obj = gTTS(text, lang='ru')
    # obj.save('hw3.mp3')
    os.system(r'C:\stardiatka_proekt\python\mp3\viktorina_pychkin\hw3.mp3')
    print('Классно!!! А день и месяц его рождения знаешь?')
birthday = input()
while birthday != '6.06' and birthday != '6 июня':
    print('Неверный день рождения.Подумай еще')
    text = 'Неверный день рождения.Подумай еще.'
    # obj = gTTS(text, lang='ru')
    # obj.save('hw4.mp3')
    os.system(r'C:\stardiatka_proekt\python\mp3\viktorina_pychkin\hw4.mp3')
    birthday = input('Неверный день рождения.Подумай еще')
if birthday == ('6.06') or birthday == ('6 июня'):
    text = 'Верно. Молодец!'
    # obj = gTTS(text, lang='ru')
    # obj.save('hw5.mp3')
    os.system(r'C:\stardiatka_proekt\python\mp3\viktorina_pychkin\hw5.mp3')
    print('Верно. Молодец')
print('end')