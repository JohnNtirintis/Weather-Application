from flask import Flask, url_for, redirect, render_template
import requests
from requests import get

app = Flask(__name__)

# Read API key from a txt file
with open('api-key.txt', 'r') as file:
    API_KEY = file.readline().strip()

URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

# Home page
@app.route('/')
def home_page():
    return render_template('home.html')

# Service Functions

@app.route("/weather/<string:city>")
def by_city(city):
    #city = input("Enter your city: ").strip()
    response = requests.get(URL.format(city , API_KEY))
    data = response.json()
    # Checking to see if the request was successful 
    if response.status_code == 200:
        return render_template('weather.html', city=city, temp=data['main']['temp'], weather_desc=data['weather'][0]['description'],
                         wind_speed=data['wind']['speed'])
        # print_data(data)
    else:
        return render_template('main.html', error=data['message'])
        #print(f"Error: {data['message']}")
    

@app.route("/weather/")
def by_ip():
    loc = get('https://ipapi.co/json/')
    data = loc.json()
    return by_city(data['city'])

"""
def print_data(data):
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Wind Speed: {data['wind']['speed']}")
    # Can also print the latidute and longitude of the user with:
    print(f"Latidute: {data['coord']['lat']}")
    print(f"Longitude: {data['coord']['lon']}")
"""

