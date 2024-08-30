import os
import telebot
from telebot.util import quick_markup

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
bot_info = bot.get_me()
BOT_USERNAME = bot_info.username
BOT_NAME = bot_info.first_name
print("Bot online!\n" + f"+ {BOT_USERNAME}\n" + f"+ {BOT_NAME}")

@bot.message_handler(commands=['start', 'hi', 'hello', 'ohayo'])
def reply_greeting(message):
    bot.reply_to(message, "I' M  A L I V E")


# Handler para responder a menções tanto do nome quanto do username (o @) do bot.
@bot.message_handler(
    func=lambda message: BOT_USERNAME in message.text or BOT_NAME in message.text
)
def reply_mention(message):
    response = f"Fui mencionada! Só não entendo ainda o que você falou, {message.from_user.first_name}..."
    bot.reply_to(message, response)


@bot.message_handler(commands=['help'])
def help(message):
    """
    Creates button below the message!
    """
    markup = quick_markup({
        'PLanilha': {'url': 'https://docs.google.com/spreadsheets/d/1jyEm-JE7tNSfgApNyirumc4XNRQOW34jcP8CUArRfBs/edit?usp=sharing'},
        'Back': {'callback_data': 'whatever'}
    }, row_width=2)
    bot.reply_to(message,"PLACEHOLDER TEXT", reply_markup=markup)


bot.infinity_polling()
