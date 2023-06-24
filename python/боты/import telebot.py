import telebot
from telebot import types

bot = telebot.TeleBot('5886302868:AAEZQcT2E_bjtXPyIIAqJo8_0CBdtYfX5dA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Рад тебя приветствовать в моем телеграм боте введи /help")   


@bot.message_handler(content_types='text')
def get_text_text(message):
    a = ['Молодец', 'Красавчег', 'Привет', 'молодец', 'красавчег', 'привет', "/help"]
    if not message.text in 'МолодецКрасавчегПриветмолодецкрасавчегпривет/help' and '?' not in message.text:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    if '?' in message.text:
        bot.send_message(message.from_user.id, '''Это очень интересный вопрос 
мы соберем всех наших мудрецов
обсудим его основательно
и обязательно пришлем вам ответ!''')
    # a = ['Молодец', 'Красавчег', 'Привет', 'молодец', 'красавчег', 'привет', "/help"]
    else:
        for i in a:
            if i == "/help" and i in message.text:
                bot.send_message(message.from_user.id, '''Напиши Привет
                или Напиши Молодец
                или Напиши Красавчег
                или отправь фотку
                или введи   /start
                или задай вопрос''')
            if (i == 'Молодец' or i == 'молодец') and i in message.text:
                bot.send_message(message.from_user.id, "Я знаю!")
            if (i == 'Красавчег' or i == 'красавчег') and i in message.text:
                bot.send_message(message.from_user.id, "Еще какой!")
            if (i == 'Привет' or i == 'привет') and i in message.text:
                bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#             if '?' in message.text:
#                 bot.send_message(message.from_user.id, '''Это очень интересный вопрос 
# мы соберем всех наших мудрецов
# обсудим его основательно
# и обязательно пришлем вам ответ!''')
                
 
   
@bot.message_handler(content_types='photo')       
def get_text_photo(message):
    bot.send_message(message.from_user.id, '''Вау крутая фотка
Есть еще что интересненькое?''')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти', url='https://www.youtube.com/channel/UCQFGE9LvAdlEXCTr5rnBj2A'))
    bot.send_message(message.from_user.id, "Посетите мой канал", reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=4)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(start, website)
    bot.send_message(message.from_user.id, "Посетите мой канал", reply_markup=markup)


bot.polling(none_stop=True, interval=0)