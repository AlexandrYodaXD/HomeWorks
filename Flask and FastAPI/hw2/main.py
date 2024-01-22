from secrets import token_hex

from flask import Flask, render_template, flash, request, make_response, redirect, url_for

app = Flask(__name__)
app.secret_key = token_hex()


@app.route('/', methods=['GET', 'POST'])
def index():
    username = request.cookies.get('username')

    title = 'Главная'
    content = {
        'username': username
    }

    if request.method == 'POST':
        if username:
            flash('Ты съел свою печеньку и мы забыли твоё имя...', 'danger')
            response = make_response(redirect(url_for('index')))
            response.delete_cookie('username')
            return response

    return render_template('index.html', title=title, content=content)


@app.get('/sign_up/')
def sign_up_get():
    return render_template('sign_up.html', title='Регистрация')


@app.post('/sign_up/')
def sign_up_post():
    flash('Ты получил свою именную печеньку!', 'success')
    username = request.form.get('name')
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', username)
    return response


if __name__ == '__main__':
    app.run()
