# Декоратор errorhandler, функции redirect и abort

from flask import Flask, render_template, request, flash, session, url_for, redirect, abort

app = Flask(__name__, template_folder='templates/lesson5-7')

app.config['SECRET_KEY'] = 'jhljheovfefk349f8fj32'

menu = [{"name": "Главная", "url": "/"},
        {"name": "Установка", "url": "/install-flask"},
        {"name": "Первое приложение", "url": "/first-app"},
        {"name": "Обратная связь", "url": "/contact"},
        {"name": "Вход", "url": "/login"}]

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

# Создаём обработчик для кода 404, используя декоратор errorhandler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404
    # при разработке реальных сайтов, лучше возвращать код 200
    # return render_template('page404.html', title="Страница не найдена", menu=menu)

@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template('base.html', menu=menu, title=f'Пользователь {username}')

@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form.get('username') == "denis" and request.form.get('psw') == "123":
        session['userLogged'] = request.form.get('username')
        return redirect(url_for('profile', username=session['userLogged']))
 
    return render_template('login.html', title="Авторизация", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)