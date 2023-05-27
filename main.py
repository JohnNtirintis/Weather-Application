from flask import Flask, url_for, redirect, render_template, request
import requests as http_requests
from requests import get

app = Flask(__name__)

# Read API key from a txt file
with open('api-key.txt', 'r') as file:
    API_KEY = file.readline().strip()

URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
FIVE_DAY_FORECAST = "http://api.openweathermap.org/data/2.5/forecast?id={}&appid={}&units=metric"

# Home page
@app.route('/')
def home_page():
    return render_template('home.html')

# Service Functions

@app.route("/weather/<string:city>")
def by_city(city):
    #city = input("Enter your city: ").strip()
    response = http_requests.get(URL.format(city , API_KEY))
    data = response.json()
    # Checking to see if the request was successful 
    if response.status_code == 200:
        icon_code=data['weather'][0]['icon']
        week_data = week_forecast(data['id'])
        return render_template('weather.html', city=city, icon_url= f"http://openweathermap.org/img/w/{icon_code}.png" ,temp=data['main']['temp'], humidity=data['main']['humidity'], 
                               weather_desc=data['weather'][0]['description'], wind_speed=data['wind']['speed'])
    else:
        return render_template('weather.html', error=data['message'])
        #print(f"Error: {data['message']}")
    
@app.route("/weather/")
def by_ip():
    loc = get('https://ipapi.co/json/')
    data = loc.json()
    return by_city(data['city'])

@app.route('/search')
def search():
    # Correlates to the name attribute of the html code
    city = request.args.get('city')
    if not city:
        print(city)
        return render_template('home.html')
    return by_city(city)

# 5 day week forecast
def week_forecast(city):
    response =  http_requests.get(FIVE_DAY_FORECAST.format(city , API_KEY))
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return render_template('weather.html', error=data['message'])

