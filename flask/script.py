from flask import Flask, flash, request, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jhljheovfefk349f8fj32'

@app.route('/', methods=['POST', 'GET'])
def index():
    name = request.form.get('username')
    if name:
        if len(name) > 2:
            flash('Успех', category='success')
            
        else:
            flash('Ошибка', category='error')
        
    return render_template('index.html')

@app.route('/<message>')
def page(message):
    return f'<h2>{message}</h2>'

if __name__ == '__main__':
    app.run(debug=True)