import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather_by_city(city):

    """
    Função para buscar a temperatura da cidade
    Recebe o nome da cidade que o usuario deseja saber o clima
    Mostra o clima com fr
    """


    api_weather = os.getenv('KEY_WEATHER')

    url = f'https://api.openweathermap.org/data/2.5/weather?'

    params={
        'q': city,
        'lang': 'pt_br',
        'units': 'metric',
        'appid': api_weather

    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    weather = response.json()


    clima = weather['weather'][0]['description']
    temp = weather['main']['temp']
    temp_max = weather['main']['temp_max']
    temp_min = weather['main']['temp_min']
    city = weather['name']
    country = weather['sys']['country']
    print()
    print(weather)
    print(weather.keys())
    print(weather['name'], weather['sys']['country'])
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])
    print()
    print(f'O clima hoje em {city}-{country} está com o {clima} e uma temperatura de {temp}º com maximas de {temp_max}º e minima de {temp_min}º')
    print()


city = str(input('Digite o nome da cidade que você deseja saber o clima: '))
get_weather_by_city(city)