
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/project1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def create_a_user(creating_a_user):
    db.session.add(creating_a_user)
    try:
        db.session.commit()
    except Exception as e:
        return e


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    birthdate = db.Column(db.String(100))
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(101))

    def __init__(self, username, birthdate, firstname, lastname, email, is_active, password):
        self.username = username
        self.birthdate = birthdate
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.is_active = is_active
        self.password = password
