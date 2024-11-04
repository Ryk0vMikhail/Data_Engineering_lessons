import requests
import pandas as pd
wth_full_info = []

def get_wether(city, date):

    wth_info = {
        'location': None,
        'date': None,
        'min_temp': None,
        'max_temp': None,
        'avg_temp': None,
    }

    URL = f'http://api.weatherapi.com/v1/future.json?key=ddaed6ca34ee4664b86203047240411&q={city}&dt={date}'
    r = requests.get(url=URL)

    resul = r.json()

    wth_info['location'] = resul.get('location').get('name')
    wth_info['date'] = resul.get('forecast').get('forecastday')[0].get('date')
    wth_info['max_temp'] = resul.get('forecast').get('forecastday')[0].get('day').get('maxtemp_c')
    wth_info['min_temp'] = resul.get('forecast').get('forecastday')[0].get('day').get('mintemp_c')
    wth_info['avg_temp'] = resul.get('forecast').get('forecastday')[0].get('day').get('avgtemp_c')

    wth_full_info.append(wth_info)
    return wth_info

    # Если бы использовали библиотеку glom
    # spec = {
    #     'location': ('location:name'),
    #     'date': ('forecast:forecastday:0:date'),
    #     'max_temp': ('forecast:forecastday:0:day:maxtemp_c'),
    #     'min_temp': ('forecast:forecastday:0:day:mintemp_c'),
    #     'avg_temp': ('forecast:forecastday:0:day:avgtemp_c'),
    # }
    #
    # wth_info = glom.glom(resul, spec, default=None)

get_wether('Moscow', '2024-12-05')
get_wether('Moscow', '2024-12-06')
get_wether('Moscow', '2024-12-07')
get_wether('Moscow', '2024-12-08')

df1 = pd.DataFrame(wth_full_info)
df1.to_csv("wether_info.csv", index=False)

get_df1 = pd.read_csv("wether_info.csv")
print(get_df1)
