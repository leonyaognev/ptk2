from TODO.models import Todolist, Todo
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def todo_list_view(todo_list: Todolist) -> object:
    kb = InlineKeyboardMarkup()

    i = 1
    for task in todo_list.tasks:
        btn_task = InlineKeyboardButton(
            text=f'{i}, {task.text}',
            callback_data=f'view/{task.id}'
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


def todo_meny_view(todo: Todo):
    kb = InlineKeyboardMarkup()

    btn_change_status = InlineKeyboardButton(
        text="изменить статус",
        callback_data=f"change_status/{todo.id}"
    )
    btn_change_text = InlineKeyboardButton(
        text="изменить текст",
        callback_data=f"change_text/{todo.id}"
    )
    btn_delete = InlineKeyboardButton(
        text="удалить",
        callback_data=f"delete/{todo.id}"
    )
    btn_back = InlineKeyboardButton(
        text="<- назад",
        callback_data=f"back"
    )

    kb.add(
        btn_change_status, btn_change_text, btn_delete, btn_back,
        row_width=1
    )

    massage_text = f'{todo.text}\n\nстатус:{"✅" if todo.status else "❌"}'
    return massage_text, kb