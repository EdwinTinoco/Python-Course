from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=False)
    user_password = db.Column(db.String(10), unique=False)
    user_email = db.Column(db.String(50), unique=False)

    def __init__(self, user_name, user_password, user_email):       
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_name', 'user_password', 'user_email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Endpoint to create a new user
@app.route('/user', methods=["POST"])
def add_user():    
    user_name = request.json['user_name']
    user_password = request.json['user_password']
    user_email = request.json['user_email']

    new_user = User(user_name, user_password, user_email)

    db.session.add(new_user)
    db.session.commit()    

    user = User.query.get(new_user.user_id)

    return user_schema.jsonify(user)


# Endpoint to query all users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Endpoint for querying a single user
@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)


# Endpoint for updating a user
@app.route("/user/<user_id>", methods=["PUT"])
def user_update(user_id):
    user = User.query.get(user_id)
    user_name = request.json['user_name']
    user_password = request.json['user_password']
    user_email = request.json['user_email']

    user.user_name = user_name
    user.user_password = user_password
    user.user_email = user_email

    db.session.commit()
    return user_schema.jsonify(user)


# Endpoint for deleting a user
@app.route("/user/<user_id>", methods=["DELETE"])
def user_delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return "User was successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)

