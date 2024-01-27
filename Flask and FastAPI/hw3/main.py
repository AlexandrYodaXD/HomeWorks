from secrets import token_hex

from flask import Flask, render_template, flash, request, make_response, redirect, url_for

from models import db, User

app = Flask(__name__)
app.secret_key = token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Database initialized')


@app.route('/', methods=['GET', 'POST'])
def index():
    # username = request.cookies.get('username')
    #
    # title = 'Главная'
    # content = {
    #     'username': username
    # }
    #
    # if request.method == 'POST':
    #     if username:
    #         flash('Ты съел свою печеньку и мы забыли твоё имя...', 'danger')
    #         response = make_response(redirect(url_for('index')))
    #         response.delete_cookie('username')
    #         return response
    #
    # return render_template('index.html', title=title, content=content)
    return None


if __name__ == '__main__':
    app.run()
