import sqlite3
from flask import url_for

def create_connection():
    URL_DB = '.' + url_for('static', filename='data.db')
    return sqlite3.connect(URL_DB)

def create_tables():
    con = create_connection()
    sql = """
        create teble if not exists films (
            id integer primary key,
            title text,
            rating real,
            description text,
            year integer,
            poster_url text,
            genres text,
            country text,
            duration integer,
            short_description text,
            age_rating integer,
            video_url text
        )
    """

    con.execute(sql)

def get_films_list():
    con = create_connection()
    SQL = 'select id, title, poster_url, short_description from films'
    qwery = con.execute(SQL)
    return qwery.fetchall()

def get_film_by_id(film_id):
    con = create_connection()
    SQL = 'select * from films where id = ?'
    qwery = con.execute(SQL, [film_id])
    return qwery.fetchall()

def add_new_film(title, rating, description, year, poster_url, genres, country, duration, short_description, age_rating, video_url):
    con =create_connection()
    SQL = """
    insrt into films(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    con.execute(SQL, (title, rating, description, year, poster_url, genres, country, duration, short_description, age_rating, video_url))











