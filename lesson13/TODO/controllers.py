from TODO.views import todo_list_view, todo_menu_view
from TODO.models import Todolist, Todo

def get_task_view(user_id: int):
    todo_list = Todolist(user_id)
    return todo_list_view(todo_list)

def add_task(user_id, text):
    todo_list = Todolist(user_id)
    todo_list.add_task(text)
    return get_task_view(user_id)

def delete_task(user_id: int, task_id: id):
    todo_list = Todolist(user_id)
    todo_list.delete_task(task_id)
    return get_task_view(user_id)

def change_status(user_id: int, task_id: int):
    todo_list = Todolist(user_id)
    task = todo_list.get_task_by_id(task_id)
    task.change_status()
    return todo_menu_view(task)

def change_text(user_id: int, task_id: int, text):
    todo_list = Todolist(user_id)
    task = todo_list.get_task_by_id(task_id)
    task.update(text)
    return todo_menu_view(task)

def get_task_menu(user_id: int, task_id: int):
    todo_list = Todolist(user_id)
    task = todo_list.get_task_by_id(task_id)
    return todo_menu_view(task)