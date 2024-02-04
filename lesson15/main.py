import requests
from pprint import pprint

# def city_wether(city: str, days: int):
#     params = {
#         f"q": city,
#         'appid': '1e29b1de4251866ff15108fd103bd241',
#         'cnt': days,
#         'units': 'metric',
#         'lang': 'ru'
#     }
#     URL = 'https://api.openweathermap.org/data/2.5/weather'
#
#     resp = requests.get(URL, params)
#
#     if not resp.ok:
#         return f'не удалось выполнить подключение. код ошибки: {resp.status_code}'
#
#     data = resp.json()
#     list_dicts = data['list']
#
#     for day in list_dicts:
#         temp = day['main']['temo']
#         desc = day['weather'][0]['description']
#         data_time = day['dt_txt']
#         print(f'{data_time}: {temp}C, {desc}')
#
# print(city_wether('новосибирск', 10))
#
#
# def film(name: str):
#     URL = 'http://www.omdbapi.com/'
#     params = {
#         'apikey': 'c400d4d8',
#         't': name
#     }
#
#     resp = requests.get(URL, params)
#
#     if not resp.ok:
#         return f'не удалось выполнить подключение. код ошибки: {resp.status_code}'
#
#     data = resp.json()
#     print(f'информакция о фильме "{name}":\nгод выпуска: {data["Year"]}\nрейтинг: {data["imdbRating"]}\nсюжет: {data["Plot"]}')
#
# film('The Shawshank Redemption')

def crypto(cripto: str, currency: str):
    params = {
        'ids': cripto,
        'vs_currencies': currency
    }
    url = 'https://api.coingecko.com/api/v3/simple/price'
    resp = requests.get(url, params)
    data = resp.json()
    print(f'стоимость {cripto} в {currency.upper()}: {data[cripto][currency]}')

crypto('bitcoin', 'rub')