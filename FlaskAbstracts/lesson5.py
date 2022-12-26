# Подключение внешних ресурсов и работа с формами

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates/lesson5-7')

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
def index():
    return render_template('base.html', menu = menu, title='Главная страница')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form.get('username'))
    return render_template('contact.html', menu = menu, title='Обратная связь')

if __name__ == "__main__":
    app.run(debug=True)
    