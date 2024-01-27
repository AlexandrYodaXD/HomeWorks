from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistryForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired(), Length(max=32)])
    second_name = StringField('Фамилия', validators=[DataRequired(), Length(max=32)])
    gender = SelectField('Пол', choices=[('M', 'Мужской'), ('F', 'Женский')])
    email = StringField('Эл. почта', validators=[DataRequired(), Email()])
    username = StringField('Логин', validators=[DataRequired(), Length(max=32)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8, max=32)])
    password_confirm = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
