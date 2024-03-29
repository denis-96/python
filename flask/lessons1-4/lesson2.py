# Использование шаблонов страниц сайта

from flask import Flask, render_template

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]
@app.route('/')
def index():
    title = 'Главная страница'
    return render_template('index.html', title=title, menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)