#!/usr/local/bin/python3

# Chapter 14 – Working with CSV Files and JSON Data

# ATBS-14_weather.py 

import sys, json, requests
from pprint import pprint

# compute location from command line arg
if len(sys.argv) < 2:
    print("Usage: ATBS-14_weather.py location")
    sys.exit()
 
# set location variable
location = " ".join(sys.argv[1:])

# api key for OpenWeather
api_key = "d965d929c2790f6feec5ba493f9dd2f9"

# set URL for requests to use
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}"

# make HTTP POST using location and API key
response = requests.post(url)

# raise exception for HTTP status errors
response.raise_for_status()

# convert response to json
weather = json.loads(response.text)

# demo API
print(weather)

#convert temp from Kelvin to Fahrenheit
temp = round(1.8 * ((weather['main']['temp']) - 273) + 32,1)

# print results
print()
print(f"Current weather in {weather['name']}: ")
print(f"{weather['weather'][0]['main']} - {weather['weather'][0]['description']}")
print(f"Temp - {temp}")
