import sqlite3
from pprint import pprint

def get_films_age_rating():
    conection = sqlite3.connect('films.db')
    cursor = conection.cursor()
    SQL = f"""
        SELECT title, age_rating, year from movies
        where age_rating >= 16
    """
    query = cursor.execute(SQL)
    data = query.fetchall()

    conection.close()
    return data

pprint(get_films_age_rating())
