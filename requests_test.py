import requests
import pandas as pd

token = '19c8a977a4b95b626d35ba4b697e4b14'
curr = 'EUR,RUB'
start_date = '2010-03-01'
end_date = '2010-04-01'
URL = f'https://api.currencylayer.com/timeframe?access_key={token}&currencies={curr}&start_date={start_date}&end_date={end_date}'

cash_info = []

days_cash = {
        'date': 'null',
        'USDRUB': 0,
        'USDEUR': 0
    }

r = requests.get(url=URL)

resul = r.json()
list_cash = resul.get('quotes')

for date in list_cash:

    days_cash['date'] = date
    days_cash['USDRUB'] = list_cash[date].get('USDRUB')
    days_cash['USDEUR'] = list_cash[date].get('USDEUR')

    cash_info.append(days_cash)


df1 = pd.DataFrame(cash_info)
df1.to_csv("from_pandas.csv", index=False)

df2 = pd.read_csv("from_pandas.csv")

print(df2)
