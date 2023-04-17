from flask import Flask

# Создаем экземпляр класса Flask
app = Flask(__name__)

# Добавляем представление (view функция)
@app.route("/")
def index():
    return "index"

# Создаём еще одно представление
@app.route("/about")
def about():
    return "<h1>О сайте</h1>"

if __name__ == '__main__':
    # Запускаем приложение
    app.run(debug=True)
    