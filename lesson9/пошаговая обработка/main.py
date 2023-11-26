import telebot

TOKEN = "6300342207:AAFBgMVVmFI5Gp3UOe5F51AjXcODrEpOMlU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = telebot.types.KeyboardButton('леня')
    but2 = telebot.types.KeyboardButton('не леня')
    keyboard.add(but1, but2)
    bot.send_message(message.chat.id,
                     'Привет! Как тебя зовут?',
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, input_user_name)

def input_user_name(message):
    user_name = message.text.strip().title()
    bot.send_message(message.chat.id, f'Приятно познакомиться, {user_name}!')
    bot.send_message(message.chat.id, 'а сколько тебе лет?')
    bot.register_next_step_handler(message, input_user_age)

def input_user_age(massage):
    user_age = massage.text.strip().title()
    if int(user_age) < 25:
        bot.send_message(massage.chat.id, f'{user_age} лет...\nну ты и малявка')
    else:
        bot.send_message(massage.chat.id, f'{user_age} - отличный возраст')

@bot.message_handler(commands=['rickroll'])
def rickroll(message):
    keyboardl = telebot.types.InlineKeyboardMarkup()

    button_link = telebot.types.InlineKeyboardButton(
        'Ссылка',
        url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    )
    button_photo = telebot.types.InlineKeyboardButton('фото', callback_data='get_photo')
    keyboardl.add(button_link, button_photo)

    bot.send_message(message.chat.id,
                     'мемчики:',
                     reply_markup=keyboardl)

@bot.callback_query_handler(func = lambda callback: True)
def callback(callback):
    url_photo = 'https://sun9-64.userapi.com/c235031/u344655852/d30/-3/x_53187957b1.jpg'
    if callback.data == 'get_photo':
        bot.send_photo(callback.message.chat.id, url_photo)

        bot.answer_callback_query(callback.id, 'фото отправлено')

print('сервер запущен')
bot.polling(non_stop=True, interval=1)
