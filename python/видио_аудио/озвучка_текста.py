from gtts import gTTS
text = '''ты падла мамочка!!!'''
obj = gTTS(text, lang='ru')
obj.save('hw2.mp3')