from gtts import gTTS
text = '''дунаев иди ты к черту
а иди ты все я пиво хочу миша
скажи за меня что ни будь пошел я жарить каштаны я кабан.'''
obj = gTTS(text, lang='ru')
obj.save('hw2.mp3')