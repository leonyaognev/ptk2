import sqlite3

con = sqlite3.connect('movavifon.db')
cur = con.cursor()

SQL_del = """
    update sim_card 
    set operator = 'Movavifon'
    where phone like '8912%' or phone like '8913%' or phone like '8914%'
"""

con.execute(SQL_del)
con.commit()

con.close()