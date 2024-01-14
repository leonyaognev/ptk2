import sqlite3
import telebot
from telebot.types import Message

connection = sqlite3.connect('chat.db')
cursor = connection.cursor()

SQL_CREATE = """
CREATE TABLE IF NOT EXISTS chat ( 
id integer PRIMARY KEY,
chat_id text ,
txt text
)
"""


cursor.execute(SQL_CREATE)
connection.close()

TOKEN = "6300342207:AAFBgMVVmFI5Gp3UOe5F51AjXcODrEpOMlU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'привееет!')

@bot.message_handler(content_types=['text'])
def text(massage: Message):
    connection = sqlite3.connect('chat.db')
    cursor = connection.cursor()


    SQL_SELECT = f"""
    SELECT txt from chat 
    where chat_id = {massage.from_user.id}
    """
    qwery = cursor.execute(SQL_SELECT)
    data = qwery.fetchall()

    if (massage.text, ) in data:
        bot.send_message(massage.chat.id, 'такое сообщение уже было')
    else:
        SQL_UPDATE =  f"""
        INSERT INTO chat(chat_id, txt) 
          VALUES ({massage.chat.id}, '{massage.text}')
        """
        cursor.execute(SQL_UPDATE)
        connection.commit()
        bot.send_message(massage.chat.id, 'я запомнил')



    connection.close()



print('сервер запущен')
bot.polling(non_stop=True, interval=1)