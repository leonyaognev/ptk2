from TODO.models import Todolist
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def todo_list_view(todo_list: Todolist):
    kb = InlineKeyboardMarkup()

    i = 1
    for task in todo_list.tasks:
        btn_task = InlineKeyboardButton(
            text=f'{i}, {task.text}',
            callback_data=f'vieu/{task.id}'
        )
        kb.row(btn_task)
        i += 1

    btn_add_task = InlineKeyboardButton(
        text='добавить задачу',
        callback_data='add'
    )

    kb.row(btn_add_task)
    message_text = 'ваш список задач: '
    return message_text, kb