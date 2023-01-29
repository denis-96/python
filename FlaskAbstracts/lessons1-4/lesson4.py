# Функция url_for и переменные URL-адреса
# Вызов данной функции непосредственно связан с контекстом запроса и вне его она просто не будет работать.

from flask import Flask, render_template, url_for
 
app = Flask(__name__, template_folder='templates/lesson2-4')
 
menu = ["Установка", "Первое приложение", "Обратная связь"]
 
@app.route("/")
def index():
    print( url_for('index') )
    return render_template('index.html', menu = menu)
 
@app.route("/about")
def about():
    print( url_for('about') )
    return render_template('about.html', title = "О сайте", menu = menu)

# Способы описания URL

# @app.route("/url/<variable>")
@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"
# При необходимости мы можем добавлять конверторы при определении переменных, 
# например, указать, что следует использовать только целые числа:
# @app.route("/profile/<int:username>")

# В качестве конверторов можно использовать следующие обозначения:
# int – должны присутствовать только цифры;
# float – можно записывать число с плавающей точкой;
# path – можно использовать любые допустимые символы URL плюс символ слеша ‘/’.
 
# Создания искусственного контекста запроса для запуска функции url_for. 
with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username="denis"))
    
if __name__ == "__main__":
    app.run(debug=True)