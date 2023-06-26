from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\x8b\xf3\x08\xba\xe5CT\x8f\n\xd2V\xafL\x9a\xf8'

# Localhost Database
client = pymongo.MongoClient('localhost', 27017) 
db = client['users']

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

from user import routes
from weather import weather_routes

# Home page
@app.route('/')
def home_page():
  app.logger.info('Current user: %s', session.get('user'))
  return render_template('home.html', user=session.get('user'))

@app.route('/user', methods=["POST", "GET"])
def user():
  return render_template("user.html")

@app.route("/dashboard/", methods=["GET"])
@login_required
def dashboard():
  return render_template("user_dashboard.html")