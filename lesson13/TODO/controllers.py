from TODO.views import todo_list_view
from TODO.models import Todolist

def get_task_view(user_id: int):
    todo_list = Todolist(user_id)
    return todo_list_view(todo_list)