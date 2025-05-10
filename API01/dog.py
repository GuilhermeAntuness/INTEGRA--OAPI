import requests
import json
from dotenv import load_dotenv
import os
from colorama import Fore, Style, Back, init

# Inicializa o Colorama (necessário no Windows)
init(autoreset=True)

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError(Fore.RED + "API KEY não encontrada!!")

url = f'https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key={api_key}'
r = requests.get(url)
print(r.status_code)
response = r.json()


if r.status_code == 200:
    print('LINK DA IMAGEM: ')
    print(Style.DIM + Back.BLUE + Fore.YELLOW + response[0]['url'])
    print()