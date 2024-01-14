import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

SQL_del = """
    delete from computers 
    where id = 5
"""

con.execute(SQL_del)
con.commit()

con.close()