import sqlite3
from pprint import pprint

def get_films_by_genres(genre):
    conection = sqlite3.connect('films.db')
    cursor = conection.cursor()
    SQL = f"""
        SELECT id from genres where name = '{genre}'
    """
    query = cursor.execute(SQL)
    data = query.fetchone()

    SQL = f"""
        SELECT * from movies
        where genre_id = {data[0]}
    """
    query = cursor.execute(SQL)
    data = query.fetchall()
    conection.close()
    return data

pprint(get_films_by_genres('фантастика'))