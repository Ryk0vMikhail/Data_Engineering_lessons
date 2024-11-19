import requests
import pandas as pd
from config import KEYWETHER

key = KEYWETHER

def get_wether(city, days):
    wth_full_info = []
    URL = f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days={days}&aqi=no&alerts=yes'
    r = requests.get(url=URL)

    resul = r.json()

    for i in range(days):
        wth_info = {
            'location': resul.get('location').get('name'),
            'date': resul.get('forecast').get('forecastday')[i].get('date'),
            'min_temp': resul.get('forecast').get('forecastday')[i].get('day').get('maxtemp_c'),
            'max_temp': resul.get('forecast').get('forecastday')[i].get('day').get('mintemp_c'),
            'avg_temp': resul.get('forecast').get('forecastday')[i].get('day').get('avgtemp_c'),
        }

        wth_full_info.append(wth_info)

    return wth_full_info