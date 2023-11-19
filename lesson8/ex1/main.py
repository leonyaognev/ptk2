import telebot

TOKEN = '6300342207:AAFBgMVVmFI5Gp3UOe5F51AjXcODrEpOMlU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'меня зовут абоба')
    bot.send_message(massage.chat.id, 'я нулевый чел и ничего не умею')
    bot.send_message(massage.chat.id, 'есть у меня команды /start и /help, первая тебя приветствует, а вторая - хз, она просто есть ')

print('сервер запущен')
bot.polling(
    none_stop=True,
    interval=1
)