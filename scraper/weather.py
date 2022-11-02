import requests

def Weather():
    city = 'Krakow'
    country = 'pl'
    k = 'dd17c95c83727622bc8ce33a17e0428d'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={k}"
    
    response = requests.get(url).json()

    skyAppearance = {
        'Clouds':'skycloudy.jpg',
        'Clear':'sunysky.jpg',
        'Rain':'rainycloudy.jpg',
    }

    weather = {
        'sky': response['weather'][0]['main'],
        'temp': str(round((response['main']['temp'] - 273),2)),
        'temp_min': str(round((response['main']['temp_min'] - 273),2)),
        'temp_max': str(round((response['main']['temp_max'] - 273),2)),
        'humidity': str(response['main']['humidity']),
        'skyAppearance':skyAppearance[response['weather'][0]['main']]
    }

    return weather