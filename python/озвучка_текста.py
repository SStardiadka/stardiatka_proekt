from gtts import gTTS
text = '''it's a voice acting program
text'''
obj = gTTS(text, lang='en')
obj.save('hw2.mp3')