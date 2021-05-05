import telebot
import random

bot = telebot.TeleBot("1700111375:AAGALPjf0pvIBBKQg1ivhUxCC5ZLkEw95uk")

buttuns = telebot.types.ReplyKeyboardMarkup(row_width=1)
btn1 = telebot.types.KeyboardButton('بازی حدس اعداد')

buttuns.add(btn1)

@bot.message_handler(commands=['start'])
def say_welcome(message):
    bot.send_message(message.chat.id,'سلام خوش اومدی تو این بازی باید یک عدد بین 0 تا 20 انتخاب کنی')

a = random.randint(0, 20)

@bot.message_handler(func=lambda message: True)
def start_game(message):
    if message.text == 'بازی حدس اعداد':
        bot.send_message(message.chat.id, 'بین 0 تا 20 یک عدد انتخاب کن :')
    if message.text.isnumeric():
        if a == int(message.text):
            bot.reply_to(message, 'شما برنده شدید')
        elif int(message.text) < a:
            bot.reply_to(message, 'برو بالا')
        elif int(message.text) > a:
            bot.reply_to(message, 'برو پایین')
        else:
            bot.reply_to(message,'Error!!!')

bot.polling()
