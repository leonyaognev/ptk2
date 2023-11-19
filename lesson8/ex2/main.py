import telebot

TOKEN = '6300342207:AAFBgMVVmFI5Gp3UOe5F51AjXcODrEpOMlU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'я калькулятор!')
@bot.message_handler(content_types=['text'])
def start(massage):
    try:
        bot.send_message(massage.chat.id, eval(massage.text))
    except:
        bot.send_message(massage.chat.id, 'ты что вводишь, дурак')

print('сервер запущен')
bot.polling(
    none_stop=True,
    interval=1
)