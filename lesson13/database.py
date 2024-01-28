import sqlite3


class Database:
    def __init__(self):
        self.__con = sqlite3.connect('data.db')

        self.__con.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                userId INTEGER,
                text TEXT,
                status INTEGER DEFAULT 0 NOT NULL         
            )
        """)
        self.__con.commit()

    def execute(self, sql_request):
        return self.__con.execute(sql_request)

    def commit(self):
        self.__con.commit()