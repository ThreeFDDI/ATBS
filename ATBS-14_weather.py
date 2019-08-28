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

login = f"http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={api_key}"

response = requests.post(login)

print()
print(response.status_code)
print()
pprint(response.text)


# download json from OpenWeatherMap.org's API
#url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3'

#response = requests.get(url)

#response.raise_for_status()

# TODO load json data into a Python variable




#print(sys.argv[0])
#print(location)