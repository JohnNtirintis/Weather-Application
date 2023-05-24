from flask import Flask, url_for, redirect, render_template, session, jsonify
from flask import request

app = Flask(__name__)

class User:
    def __init__(self, username, theme):
        self.username = username
        self.theme = theme

def get_current_user():
    # In a real application, you would retrieve the user from a database or data source based on the session or authentication mechanism
    # Here, we are using a mock user object
    return User('JohnDoe', 'dark')

def get_all_users():
    # In a real application, you would retrieve all users from a database or data source
    # Here, we are using a mock list of user objects
    return [
        User('JohnDoe', 'dark'),
        User('JaneSmith', 'light'),
        User('AliceWonderland', 'dark')
    ]

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        'username': user.username,
        'theme' : user.theme,
    }

@app.route('/users')
def users_api():
    users = get_all_users()
    return jsonify([user.__dict__ for user in users])