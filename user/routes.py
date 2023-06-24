from flask import Flask
from main import app
from user.models import User

# User related routes

@app.route('/user', methods=['GET', 'POST'])
def signup_form():
  return User().signup_form()

@app.route('/user/signup/', methods=['GET', 'POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/add_city_to_favorites', methods=['GET', 'POST'])
def add_city_to_favorites():
  return User().add_city_to_favorites()

@app.route('/get_favorite_cities', methods=["GET"])
def get_favorite_cities():
  return User().get_favorite_cities()

@app.route('/remove_city_from_favorites', methods=['GET', 'POST'])
def remove_city_from_favorites():
  return User().remove_city_from_favorites()