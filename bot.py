import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8625694060:AAGWp6m0BGYlGaeHvPwP59cSMt_BnCjYEVs'
bot = telebot.TeleBot(TOKEN)

def get_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    r = requests.get(url).json()
    return f"USD: 1\nEUR: {r['rates']['EUR']:.2f}\nGBP: {r['rates']['GBP']:.2f}\nRUB: {r['rates']['RUB']:.2f}"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Курсы валют:", reply_markup=menu())

def menu():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Обновить", callback_data='update'))
    return kb

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'update':
        bot.edit_message_text(get_rates(), call.message.chat.id, call.message.message_id, reply_markup=menu())
import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return "OK"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

Thread(target=run_flask).start()
bot.polling()
