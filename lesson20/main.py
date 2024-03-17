from flask import Flask
from utils import get_planets_list, get_planet_by_id

app = Flask(__name__)

@app.route('/')
def index_pag():
    data = get_planets_list()
    links = [
        f'<li><a href="/planet/{id}">{name}</a></li>' for id, name in data
    ]
    return '<ul>' + ''.join(links) + '</ul><a href="/planet/add" style=display >добавить</a>'

@app.route('/planet/add')
def add_page():
    return ''

@app.route('/planet/<int:id>')
def planet_page(id):
    info = get_planet_by_id(id)
    return f'''
        <h1>{info[1]}</h1>
        <p><b>расстояние от солнца:</b>{info[2]}</p>
        <p><b>диаметр:</b>{info[3]}</p>
        <p><b>масса:</b>{info[4]}</p>
        <p><b>состав планеты:</b>{info[5]}</p>
        <p><b>уникальные особенноести:</b>{info[6]}</p>
        <p><b>геологическа активность:</b>{info[7]}</p>
        <p><b>спутники:</b>{info[8]}</p>
        <p><b>климат и погода:</b>{info[9]}</p>
        <a href='/' > список планет </a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)