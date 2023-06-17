from flask import Flask
from main import app
from weather.weather_models import Weather




@app.route("/weather/<string:city>")
def weather_by_city(city):
    Weather().weather_by_city(city)

@app.route("/weather/")
def weather_by_ip():
    Weather().weather_by_ip()

@app.route("/search")
def search():
    Weather().search()
