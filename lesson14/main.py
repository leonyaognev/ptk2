import requests

def get_weather(city: str, days: int):
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': '1e29b1de4251866ff15108fd103bd241',
        'units': 'metric',
        'cnt': days
    }
    resp = requests.get(URL, params)

    if not resp.ok:
        return f'не удалось выполнить подключение. код ошибки: {resp.status_code}'


    data = resp.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    return f'текущая температура в горороде {city}: {temp}C', {description}

city_name = 'новосибирск'
print(get_weather(city_name, 1))

print('=' * 20)

city_name = 'обовоылызжас'
print(get_weather(city_name))