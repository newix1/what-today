import telebot
from datetime import date

from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('TOKEN')

'''
У меня в профиле ещё есть репозиторий hey-popey-tb-bot

Там код для бота кофейни с бонусной системой в виде кружек https://github.com/newix1/hey-popey-tb-bot/blob/main/main.py
'''


@bot.message_handler(commands=['start'])
def start(message):
    current_date = date.today()
    current_weekday = date.today().weekday()
    weekday_dict = {0: 'Понедельник',
                    1: 'Вторник',
                    2: 'Среда',
                    3: 'Четверг',
                    4: 'Пятница',
                    5: 'Суббота',
                    6: 'Воскресенье'}
    bot.send_message(message.chat.id, f'Дата сегодня: {current_date}\nДень недели: {weekday_dict[current_weekday]}',
                     parse_mode='html')


bot.infinity_polling()
