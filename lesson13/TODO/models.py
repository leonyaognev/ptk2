from database import Database

class Todo:
    def __init__(self, id, user_id, text, status):
        self.id = id
        self.user_id = user_id
        self.text = text
        self.status = status

        self.__db = Database()
    def chahge_status(self):
        if self.status == 1:
            self.status = 0
        else: self.status = 1

        self.__db.execute(f"""
                update tasks set status  = {self.status}
                where id = {self.id}
                """)
        self.__db.commit()
    def update(self, new_text):
        self.text = new_text

        self.__db.execute(f"""
        update tasks set text = {self.text} 
        where id = {self.id}
        """)
        self.__db.commit()

class Todolist:
    def __init__(self, user_id):
        self.tasks: list[Todo] = []
        self.user_id = user_id

        self.__db = Database()
        self.__init_list()

    def __init_list(self):
        qwery = self.__db.execute(f'select *from tasks where userId = {self.user_id}')
        data = qwery.fetchall()

        for id, user_id, text, status in data:
            self.tasks.append(Todo(id, user_id, text, status))

    def add_text(self, new_text):
        self.__db.execute(
            f"""
            insert into tasks (userId, text)
            values ({self.user_id}, '{new_text}')
            """)
        self.__db.commit()

    def delete_task(self, task_id):
        self.__db.execute(
                f"""
                delete from tasfs where id = {task_id}
                """)
        self.__db.commit()

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None


