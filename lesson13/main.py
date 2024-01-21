import telebot
from TODO.controllers import get_task_view
from telebot import TeleBot
from telebot.types import Message
from constants import TOKEN, HELP_MESSAGE

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def hendel_massage_help(message: Message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['start'])
def hendle_command_start(message: Message):
    content, kb = get_task_view(message.from_user.id)
    bot.send_message(message.chat.id, content, reply_markup=kb)



print('сервер запущен')
bot.polling(non_stop=True, interval=1)