import telebot
import json

TOKEN = "6300342207:AAFBgMVVmFI5Gp3UOe5F51AjXcODrEpOMlU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    but1 = telebot.types.InlineKeyboardButton('поставить оценку', callback_data='set_mark')
    but2 = telebot.types.InlineKeyboardButton('рейтинг преподавателей', callback_data='rate')
    keyboard.row(but1, but2)

    bot.send_message(message.chat.id, 'доступные команды', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    if call.data == 'set_mark':
        with open('./db/courses.json', 'r', encoding='UTF-8') as file:
            courses = json.load((file))

            for key, cours in courses.items():
                btn = telebot.types.InlineKeyboardButton(cours, callback_data=f'set_mark&selected_cours={key}')
                keyboard.row(btn)

    if 'set_mark' in call.data and 'selected_cours' in call.data:
        with open('./db/teachers.json', 'r', encoding='UTF-8') as file:
            teachers = json.load((file))

        selectead_course = call.data.split('=')[-1]
        seleted_teachers = []
        for t in teachers:
            if selectead_course in t.get('courses'):
                seleted_teachers.append(t)

        for j, t in enumerate(seleted_teachers):
            btn = telebot.types.InlineKeyboardButton(
                f'{t.get("name")} {t.get("lastname")}',
                callback_data=f'set_mark&selected_teacher={j}'
            )
            keyboard.row(btn)

    if 'set_mark' in call.data and 'selected_teacher' in call.data:
        with open('./db/teachers.json', 'r', encoding='UTF-8') as file:
            teachers = json.load((file))
        tn = int(call.data.split('=')[-1])
        like = telebot.types.InlineKeyboardButton('лайк', callback_data=f'like={tn}')
        dislike = telebot.types.InlineKeyboardButton('дизайк', callback_data=f'dis_like={tn}')
        keyboard.row(like, dislike)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f'преподаватель: {teachers[tn]["name"]} {teachers[tn]["lastname"]}\n'
                 f'рейтинг преподавателя: {teachers[tn]["rating"]}'
        )

    if 'like' in call.data:
        with open('./db/teachers.json', 'r', encoding='UTF-8') as file:
            teachers = json.load((file))
        tn = int(call.data.split('=')[-1])

        if 'dis_like' in call.data:
            teachers[tn]["rating"] -= 1
        else:
            teachers[tn]["rating"] += 1

        with open('./db/teachers.json', 'w', encoding='UTF-8') as file:
            json.dump(teachers, file, ensure_ascii=False, indent=4)
        # handle_start(call.message)

    bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=keyboard)

print('сервер запущен')
bot.polling(non_stop=True, interval=1)