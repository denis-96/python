# Мгновенные сообщения - flash, get_flashed_messages
# flash() – формирование сообщения пользователю;
# get_flashed_messages() – обработка сформированных сообщений в шаблоне документа.

# Их синтаксис, следующий:
# flask.flash(message, category=’message’)
# flask.get_flashed_messages(with_categories=False, category_filter=[])

# message – текст сообщения;
# category – категория сообщения;
# with_categories – разрешает использование категорий при извлечении сообщений;
# category_filter – список разрешенных категорий при выборке сообщений.

from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
def index():
    return render_template('base.html', menu = menu, title='Главная страница')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if len(request.form.get('username')) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
    return render_template('contact.html', menu = menu, title='Обратная связь')

if __name__ == "__main__":
    app.run(debug=True)