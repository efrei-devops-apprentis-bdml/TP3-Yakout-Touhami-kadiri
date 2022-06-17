import requests
import json
import os

LAT = os.environ['LAT']
LONG = os.environ['LONG']
api_key = os.environ['API_KEY']

def get_weather(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (LAT, LONG, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    return data

if __name__ == "__main__":
    print(get_weather(LAT, LONG, api_key))
