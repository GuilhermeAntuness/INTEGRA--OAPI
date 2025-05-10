import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def confirm_api():

    NEWS_KEY = os.getenv('KEY_NEWS')

    if not NEWS_KEY:
        print(f'Erro com a chave API ')

    url = f'https://newsapi.org/v2/everything'

    headers = {
        'Authorization': NEWS_KEY
    }
    params = { 
        'q': 'IA',
        'language': 'pt'
    }
    return url, headers, params

def get_news(x):
    
    url, headers, params = confirm_api()
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    news = response.json()
    print(news)

    for i in news['articles'][:x]:
        print()
        print(f"Author: {i['author']}")
        print(f"Titulo: {i['title']}")
        print(f"Texto: {i['description']}")


solicitar_texto = int(input('Quantos '))
get_news(solicitar_texto)