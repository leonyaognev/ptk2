import sqlite3

con = sqlite3.connect('data.db')

SQL_update = """
    update computers 
    set cpu = 'Ryzen 7 5800X'
    where name = 'CyberNexus HorizonX'
"""

con.execute(SQL_update)
con.commit()

con.close()