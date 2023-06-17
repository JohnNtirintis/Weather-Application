from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)

# Read Mongo API key from a txt file
with open('db-api-key.txt', 'r') as file:
    uri = file.readline().strip()

client = pymongo.MongoClient(uri)
db = client.user_login_system

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
    return render_template('home.html')

@app.route("/dashboard")
@login_required
def dashboard():
  #TODO: Dashboard Template
  return "Dashboard"