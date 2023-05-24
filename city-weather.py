import requests
import json

with open('api_key.txt','r') as file:
   APPID = file.read().strip()

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

location = {
      "name":"Chelsea",
      "local_names":{
         "id":"Chelsea, London",
         "en":"Chelsea",
         "el":"Τσέλσι",
      },
      "lat":51.4875167,
      "lon":-0.1687007,
      "country":"GB",
      "state":"England"
   }

def get_weather_by_city(city):
   params = {
      'q' : city,
      'appid' : APPID,
      'units' : 'metric'
   }

   response = requests.get(BASE_URL, params=params)
   data = response.json()

   # Checking to see if the request was successful
   if response.status_code == 200:
      print(f"Temperature: {data['main']['temp']} °C")
      print(f"Weather: {data['weather'][0]['description']}")
      print(f"Wind Speed: {data['wind']['speed']}")
   else:
      print(f"Error: {data['message']}")


get_weather_by_city(location['name'])
