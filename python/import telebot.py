import telebot
bot = telebot.TeleBot('5665309474:AAHXzsdWimYznYy0KBOarFrEHW_wXO12zdc')

@bot.message_handler(content_types='text')

def get_text_messages(message):
    if not message.text in 'МолодецКрасавчегПривет/help':
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    a = ['Молодец', 'Красавчег', 'Привет', "/help"]
    for i in a:
        if i == "/help" and i in message.text:
            bot.send_message(message.from_user.id, '''Напиши Привет
            или Напиши Молодец
            или Напиши Красавчег''')
        if i == 'Молодец' and i in message.text:
            bot.send_message(message.from_user.id, "Я знаю!")
        if i == 'Красавчег' and i in message.text:
             bot.send_message(message.from_user.id, "Еще какой!")
        if i == 'Привет' and i in message.text:
                bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
   
        

bot.polling(none_stop=True, interval=0)