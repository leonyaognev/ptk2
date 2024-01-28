import telebot.types

from TODO.controllers import add_task
from telebot.types import Message
from telebot import TeleBot

def user_input_add_task(massage: Message, bot: TeleBot):
    task_text = massage.text
    msg_text, kb = add_task(
        user_id=massage.from_user.id,
        text=task_text
    )
    bot.send_message(
        chat_id=massage.chat.id,
        text=msg_text,
        reply_markup=kb
    )

def change_massage(
        text: str,
        bot: TeleBot,
        message: Message,
        kb: telebot.types.InlineKeyboardMarkup
        ):
    bot.edit_message_text(
        text=text,
        chat_id=message.chat.id,
        message_id=message.message_id
    )
    bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=kb
    )