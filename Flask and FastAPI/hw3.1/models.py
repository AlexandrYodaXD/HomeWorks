from datetime import datetime, UTC

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    hashed_password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))

    def __repr__(self):
        return f'User({self.id}, {self.first_name}, {self.second_name}, {self.gender}, {self.email}, {self.created_at})'

