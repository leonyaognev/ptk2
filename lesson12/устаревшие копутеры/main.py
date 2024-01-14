import sqlite3

con = sqlite3.connect('movavishop.db')

SQL_del = """
    update computers 
    set price = price - price * 0.15
    where gpu like 'geforce RTX%'
"""

con.execute(SQL_del)
con.commit()

con.close()