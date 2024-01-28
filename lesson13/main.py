from TODO import controllers
from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from constants import TOKEN, HELP_MESSAGE
import utils

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def hendel_massage_help(message: Message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['start'])
def hendle_command_start(message: Message):
    content, kb = controllers.get_task_view(message.from_user.id)
    bot.send_message(message.chat.id, content, reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call: CallbackQuery):
    if call.data == 'add':
        bot.send_message(
            chat_id = call.message.chat.id,
            text='ведите текст'
        )
        bot.register_next_step_handler(
            call.message, utils.user_input_add_task, bot=bot
        )
    if 'view' in call.data:
        prefix, task_id = call.data.split('/')
        msg_text, kb = controllers.get_task_menu(
            user_id=call.from_user.id,
            task_id=int(task_id)
        )
        bot.edit_message_text(
            text=msg_text,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
        bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=kb
        )

    if call.data == 'back':
        content, kb = controllers.get_task_view(call.from_user.id)
        utils.change_massage(
            message=call.message,
            bot=bot,
            text=content,
            kb=kb
        )
    if 'delete' in call.data:
        prefix, task_id = call.data.split('/')

    if 'change_text' in call.data:
        prefix, task_id = call.data.split('/')

    if 'change_status' in call.data:
        prefix, task_id = call.data.split('/')
        msg_text, kb = controllers.change_status(
            user_id=call.message.from_user.id,
            task_id=int(task_id)
        )
        utils.change_massage(
            message=call.message,
            bot=bot,
            text=content,
            kb=kb
        )



print('сервер запущен')
bot.polling(non_stop=True, interval=1)