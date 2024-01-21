import sqlite3

class Database:
    def __init__(self):
        self.__con = sqlite3.connect('data.db')

        self.__con.execute('''
        create table if not exists tasks (
            id integer primary key,
            userId integer, 
            text text,
            status integer default 0 not null
        )
        ''')
        self.__con.commit()

    def execute(self, sql_request):
        return self.__con.execute(sql_request)

    def commit(self):
        self.__con.commit()