import sqlite3
from flask import url_for
def get_planets_list():
    con = sqlite3.connect('static/data/data.db')

    select = """select id, name from planets"""
    qwery = con.execute(select)
    data = qwery.fetchall()

    return data

def get_planet_by_id(id):
    con = sqlite3.connect('static/data/data.db')

    select = F"select *  from planets where id={id}"
    qwery = con.execute(select)
    data = qwery.fetchone()

    return data

