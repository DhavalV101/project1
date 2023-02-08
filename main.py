import random
import string
import json
import jsonschema
from flask import Flask, request
from jsonschema import validate
from schemas import LoginSchema, UpdateSchema
import jwt
from cryptography.fernet import Fernet
from flask_marshmallow import Marshmallow
from models import User, create_a_user, db, app

from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow(app)
key = 'ziXLML7v3bfK7-HtGUzDpy1qj_r9LDyG1dGxPRCc7JU='
print(key)
fernet = Fernet(key)


# db.create_all()

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ("username", "birthdate", "firstname", "lastname", "email", "is_active", "password")


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)


# db.create_all()

# Create a User

@app.route('/post', methods=['POST'])
def create_user_admin():
    username = request.json['username']
    birthdate = request.json['birthdate']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    password = create_password(7)
    # if validate_user(username):
    encpassword = fernet.encrypt(password.encode())
    creating_a_user = User(username, birthdate, firstname, lastname, email, True, encpassword)
    print(password)
    db.session.add(creating_a_user)
    try:
        db.session.commit()
    except Exception as e:
        return e
    project_schema.jsonify(creating_a_user)
    # encoded_jwt = jwt.encode({
    #     'username': username,
    #     'firstname': firstname,
    #     'lastname': lastname,
    #     'email': email
    # }, "secret", algorithm="HS256")
    # print(encoded_jwt)
    return json.dumps({"username": username})


def create_password(length):
    result = ''.join(
        (random.choice(string.ascii_lowercase) for x in range(length)))
    return result


@app.route('/signup', methods=['POST'])
def usersignup():
    username = request.json['username']
    birthdate = request.json['birthdate']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    password = request.json['password']
    encpassword = fernet.encrypt(password.encode())

    creating_a_user = User(username, birthdate, firstname, lastname, email, False, encpassword)
    create_a_user()

    return json.dumps({"username": username})


#
#     if email_authentication(email):
#         creating_a_user.is_active = True
#
#
# def email_authentication(email):
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login("itsoptimusprime1001@gmail.com", "OptimusPrime@1001")
#     message = "Please click the below link to activate your account."
#     s.sendmail("itsoptimusprime1001@gmail.com", email, message)
#     s.quit()
#

@app.route('/login', methods=['POST'])
def user_login():
    username = request.json['username']
    password = request.json['password']
    # encpassword = fernet.encrypt(password.encode())

    findUser = db.session.query(User).filter_by(username=username).first()
    print(findUser.password)
    decpassword = fernet.decrypt(str(findUser.password)).decode()
    print (decpassword)
    if password == decpassword:
        encoded_jwt = jwt.encode({
            'username': username,
            'firstname': findUser.firstname,
            'lastname': findUser.lastname,
            'email': findUser.email
        }, "secret", algorithm="HS256")
        print(encoded_jwt)
        return encoded_jwt


@app.route('/update/<username>/<field>', methods=['PUT'])
def user_update(username, field):
    headers = request.headers
    print(headers)
    token = headers['Authorization'].split()[1]
    decoded_jwt = jwt.decode(token, 'secret', algorithms=['HS256'])
    if decoded_jwt['username'] == username:
        if field == 'birthdate':
            jsonschema.validate(field, UpdateSchema)
            birthdate = request.json['birthdate']
            findUser = db.session.query(User).filter_by(username=username).first()
            findUser.birthdate = birthdate
            return decoded_jwt

        elif field == 'firstname':
            jsonschema.validate(field, UpdateSchema)
            firstname = request.json['birthdate']
            findUser = db.session.query(User).filter_by(username=username).first()
            findUser.firstname = firstname
            return decoded_jwt

        elif field == 'lastname':
            jsonschema.validate(field, UpdateSchema)
            lastname = request.json['lastname']
            findUser = db.session.query(User).filter_by(username=username).first()
            findUser.lastname = lastname
            return decoded_jwt

        elif field == 'email':
            jsonschema.validate(field, UpdateSchema)
            email = request.json['email']
            findUser = db.session.query(User).filter_by(username=username).first()
            findUser.email = email
            return decoded_jwt


if __name__ == "__main__":
    app.run(debug=True)
