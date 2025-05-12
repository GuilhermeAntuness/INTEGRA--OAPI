import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_news = os.getenv("KEY_NEWS")

url = "https://newsapi.org/v2/everything"

headers = {
    'X-Api-Key' : api_news
}

response = requests.get(url, headers=headers)

try:
    print(response.status_code)
    
except requests.exceptions.RequestException as e:
    print(e)