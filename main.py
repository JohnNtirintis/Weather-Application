from flask import Flask, url_for, redirect, render_template, request
import requests as http_requests
from requests import get
import json
from datetime import datetime

#TODO: DOCUMENTATION / COMMENTS :)

app = Flask(__name__)

# Read API key from a txt file
with open('api-key.txt', 'r') as file:
    API_KEY = file.readline().strip()

# API URL's
URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
FIVE_DAY_FORECAST = "http://api.openweathermap.org/data/2.5/forecast?id={}&appid={}&units=metric"

# Home page
@app.route('/')
def home_page():
    return render_template('home.html')

# Service Functions

@app.route("/weather/<string:city>")
def by_city(city):
    response = http_requests.get(URL.format(city , API_KEY))
    data = response.json()

    # Checking to see if the request was successful 
    if response.status_code == 200:

        # Storing the specific weather icon in a var to display it to the user
        # Thus, providing different icons based on the weather
        icon_code=data['weather'][0]['icon']

        # Using week_forecast func to store the data in a dict 
        # then use the data in html with jinja
        week_data = week_forecast(data['id'])
        #weekly_data_icon = week_data['weather']['0']['icon']
        return render_template('weather.html', city=city, week_data=week_data, icon_url= f"http://openweathermap.org/img/w/{icon_code}.png" ,temp=data['main']['temp'], humidity=data['main']['humidity'], 
                               weather_desc=data['weather'][0]['description'], wind_speed=data['wind']['speed'])
    # In case of error, print the error message to notify the user
    else:
        return render_template('weather.html', error=data['message'])
    
# This function locates the user, using their IP 
# Using the API of IPAPI.
# Then uses the location to provide the current weather forecast for their location
# Note: Unfortunately, it's not very accurate but it does the job and its completely free.
@app.route("/weather/")
def by_ip():
    loc = get('https://ipapi.co/json/')
    data = loc.json()
    return by_city(data['city'])

# This function and route is the basis of the search function
@app.route('/search')
def search():
    # Correlates to the name attribute of the html code
    city = request.args.get('city')
    # If the city the user entered doesnt exist
    # Redirect them to the home page
    # TODO: Implement a better error handling.
    if not city:
        return render_template('home.html')
    return by_city(city)

# 5 day week forecast
def week_forecast(city):

    # Init an empty dict to store the forecast data
    daily_data = {}

    response =  http_requests.get(FIVE_DAY_FORECAST.format(city , API_KEY))
    data = response.json()
    if response.status_code == 200:

        # Loop over each item in the 'list' key of the data dictionary
        for item in data['list']:

             # Parse the date from the 'dt_txt' key and convert it to a date object
            date = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S').date()

            # We need to create another datetime_object that doesnt use the .date()
            # because .date() drops the time part, so when we call it, the hour is always 00:00
            # So i've added this instead
            datetime_object = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')

            # Must convert to a string to use it as a dict key
            date_str = date.strftime('%d/%m')
            hour_str = datetime_object.strftime('%H:%M')

            item['hour'] = hour_str
            # If this date is not already a key in the dictionary, add it with an empty list as its value
            if date_str not in daily_data:
                daily_data[date_str] = []

            daily_data[date_str].append(item)
        return daily_data
    else:
        return render_template('weather.html', error=data['message'])

