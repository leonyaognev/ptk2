from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index_page():
    if request.method  == "GET":
        return """
        <form action="/" method="post">
            <div>ваше имя: <input type="text", name="username"></div>
            <div>ваше пароль: <input type="password", name="password"></div>
            <div>
                <button type="submit">отправить</button>
                <button type="reset">очистить</button>
            </div>
        </form>
        """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"""
            <h1></h2>
            <p><b>ваши данные:</b> {username} {password}</p>
        """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)