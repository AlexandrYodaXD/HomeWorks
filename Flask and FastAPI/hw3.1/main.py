from secrets import token_hex

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
from flask_bcrypt import generate_password_hash

from forms import RegistryForm
from models import db, User

secret_key = token_hex()
app = Flask(__name__)
app.secret_key = secret_key
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Database initialized')


@app.cli.command("clear-db")
def clear_db_console():
    db.session.query(User).delete()
    db.session.commit()
    print('Database cleared')


@app.route('/clear_db')
def clear_db():
    db.session.query(User).delete()
    db.session.commit()
    flash('База данных очищена', 'success')
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
    content = {'users_count': len(User.query.all())}
    return render_template('index.html', content=content)


@app.route('/registry', methods=['GET', 'POST'])
def registry():
    form = RegistryForm()
    if request.method == 'POST' and form.validate_on_submit():
        existing_email = User.query.filter_by(email=form.email.data).first()
        existing_username = User.query.filter_by(username=form.username.data).first()
        if existing_email:
            flash('Пользователь с таким email уже существует!', 'danger')
        elif existing_username:
            flash('Пользователь с таким именем уже существует!', 'danger')
        else:
            user = User(
                username=form.username.data,
                first_name=form.first_name.data,
                second_name=form.second_name.data,
                gender=form.gender.data,
                email=form.email.data,
                password=form.password.data,
                hashed_password=generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            flash('Регистрация прошла успешно!', 'success')
            return redirect(url_for('index'))

    return render_template('registry.html', form=form)


@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', content=all_users)


if __name__ == '__main__':
    app.run()
