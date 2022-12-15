import telebot
from telebot import types
from config import BOT_TOKEN_ST

bot = telebot.TeleBot(BOT_TOKEN_ST)

@bot.message_handler(content_types=['text'])
def get_text_text(message):
    if not message.text in 'МолодецКрасавчегПривет/start':
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    a = ['Молодец', 'Красавчег', 'Привет', "/help", '/start']
    for i in a:
        if i == "/help" and i in message.text:
            bot.send_message(message.from_user.id, '''Напиши Привет
            или Напиши Молодец
            или Напиши Красавчег
            или отправь фотку
            или введи   /start''')
        if i == '/start' and i in message.text:
            bot.send_message(message.from_user.id, "Рад тебя приветствовать в моем телеграм боте введи /help")
        if i == 'Молодец' and i in message.text:
            bot.send_message(message.from_user.id, "Я знаю!")
        if i == 'Красавчег' and i in message.text:
            bot.send_message(message.from_user.id, "Еще какой!")
        if i == 'Привет' and i in message.text:
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
   
@bot.message_handler(content_types='photo')       
def get_text_photo(message):
    bot.send_message(message.from_user.id, "Вау крутая фотка")

bot.polling(none_stop=True, interval=0)