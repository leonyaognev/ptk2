from flask import Flask, url_for
import sqlite3
from pprint import pprint

app = Flask(__name__)
con  = sqlite3.connect('static/data/data.db')
qwery = con.execute('''select * from planets where id = 1''')
data = qwery.fetchall()

def execute(id):
    return con.execute(f'''select * from planets where id = {id}''').fetchall()


@app.route('/')
def home_page():
    return f'''
        <img src = {url_for('static', filename='imgs/shrek.jpg')} style="width: 250px">
        <br>
        {'<br>'.join()}
        '''

@app.route('/film/<int:film_id>')
def film_page(film_id):
    try:
        return f'название фильма: {}'
    except IndexError:
        return 'Фильм не найден'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)