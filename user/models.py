from flask import Flask, jsonify, request, session, redirect, render_template, url_for
from passlib.hash import pbkdf2_sha256
from main import db
import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    # ensure favorite cities is init
    user.setdefault('favorite_cities', [])
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "email": request.form.get('email'),
      "password": request.form.get('password'),
      "favorite_cities": []
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.hash(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  # Must create url for signup?
  def signup_form(self):
    # signup_url = url_for("/user/signup")
    return render_template("user.html")

  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({"error": "Invalid login credentials" }), 401
  
  def add_city_to_favorites(self):
    data = request.get_json()
    city = data.get("city")

    user_email = session['user']["email"]
    db.users.update_one({"email": user_email}, {"$push": {"favorite_cities": city}})

    # Fetch the updated user object
    updated_user = db.users.find_one({"email": user_email})

    # Update the session with the new user data
    session['user'] = updated_user

    return jsonify({"success" : "Added city to favorites"}), 200
  
  def get_favorite_cities(self):
    user_email = session['user']['email']
    user = db.users.find_one({"email": user_email})

    # Extract the favorite cities from the users data
    favorite_cities = user.get('favorite_cities', [])

    return jsonify(favorite_cities)
  
  def remove_city_from_favorites(self):
    data = request.get_json()
    city = data.get("city")
    user_email =  session['user']['email']

    # Pull removes all instances of that city
    db.users.update_one({"email": user_email}, {"$pull": {"favorite_cities": city}})

    # Fetch the updated user object
    updated_user = db.users.find_one({"email": user_email})

    # Update the session with the new user data
    session['user'] = updated_user

    return jsonify({"success" : "Removed city from favorites"}), 200
