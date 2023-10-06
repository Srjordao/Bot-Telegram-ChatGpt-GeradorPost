import openai
import telebot
from api import *

API_KEY = "chave do bot do telegram aqui"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler()
def response(message):
        bot.reply_to(message,'oiii')

bot.polling()