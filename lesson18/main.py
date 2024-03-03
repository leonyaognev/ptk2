from flask import  Flask

app = Flask(__name__)

films_list = [
    'Побег из Шоушенка',
    'Зеленая миля',
    'Властелин колец: Братство кольца',
    'Интерстеллар',
    'Звёздные войны: Эпизод V - Империя наносит ответный удар',
    'В джазе только девушки',
    'Шерлок Холмс',
    'Парк Юрского периода',
    'Американская история Х',
    'Гарри Поттер и философский камень',
]

@app.route('/')
def home_page():
    films_view = []
    for i, film_name in enumerate(films_list):
        films_view.append(f'<a href="/film/{i}">{film_name}</a>')
    return f'<br>'.join(films_view)

@app.route('/film/<int:film_id>')
def film_page(film_id):
    try:
        return f'название фильма: {films_list[film_id]}'
    except IndexError:
        return 'Фильм не найден'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)