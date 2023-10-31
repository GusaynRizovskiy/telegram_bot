import telebot
from telebot import types
bot = telebot.TeleBot("5962275064:AAHwDaIP0pJQFaWwOJP6dHUEUFeE3DVWF-8")
@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id,mess,parse_mode="html")

@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website = types.KeyboardButton("Веб сайт")
    start = types.KeyboardButton("Start")
    markup.add(website,start)
    bot.send_message(message.chat.id,"Перейдите на сайт",reply_markup=markup)
bot.polling(none_stop=True)
@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup("Посетить веб сайт", url="https://itproger.com"))
    bot.send_message(message.chat.id,"Перейдите на сайт",reply_markup=markup)

