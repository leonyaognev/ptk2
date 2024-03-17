from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    {"title": "Сделать ДЗ", "status": "не выполнено"},
    {"title": "Разморозить курицу", "status": "не выполнено"},
    {"title": "Поиграть в комп", "status": "выполнено"}
]

@app.route('/')
def index():
    return render_template(
        'index.html', task_list=tasks
    )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8070)
