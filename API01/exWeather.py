## Pedir 3 cidades
## Cada cidade faça uma requisiçã API da OpenWeather (clima e temperatura)
## Apresente as informações de cada cidade de maneira formatada ao usuario
## Faça uma lógica que analise e diga quais das cidades está mais quente

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_weather = os.getenv('KEY_WEATHER')
weather = []
def get_clima(city):
    """
    Consultar clima da cidade
    recebe a cidade
    adiciona a cidade na lista

    """



    url = f'https://api.openweathermap.org/data/2.5/weather?'


    params={
        'q': city,
        'lang': 'pt_br',
        'units': 'metric',
        'appid': api_weather

    }
    try:
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        data = response.json()
    
        if 'error' in data:
         print('Cidade não encontrada')
        else:
         
         new_city = {
            'cidade': data.get('name'),
            'temp_max': data['main']['temp_max'],
            'temp': data['main']['temp'],

         }
         weather.append(new_city.copy())


    except KeyboardInterrupt:
       print('Programa finalizado pelo usuário')

    except requests.exceptions.HTTPError:
        print('Cidade não encontrada')

    except requests.exceptions.RequestException as e:
        print('Erro de conexão ', e)
    
def solicitar_cidade():
    """
    Solicita a quantidade de cidade e a cidade ao usuario
    envia a cidade para get_clima()
    """


    while True:
        try:
            cont_city = int(input('Quantas cidades você deseja ver o clima? '))
            
            while len(weather) < cont_city:

                city = input(f'Digite o nome da {len(weather)+1}º cidade: ')
                get_clima(city)

            break   

        except Exception as e:
            print('Digite um numero valido')

def maior_temperatura():
   """
   Calcula a maior temperatura dos cidades dentro da lista
   mostra uma mensagem ao usuario formatada com a cidade com a temperatura mais alta
   """

   key = 'temp'
   valor_maximo = max(weather, key= lambda d: d[key])
   linha()
   print(f"{valor_maximo['cidade']} está com a maior temperatura com {valor_maximo['temp']}º")
      
def main():
    """
    Chama a função solicitar_cidade
    mostra a cidade formatada 
    chama a função maior_temperatura
    """
    solicitar_cidade()
    for i in weather:
       print('-='*15)
       for k,v in i.items():
          print(f'{k} : {v}')

   
    maior_temperatura()

def linha():
   print('-='*30)

def menu():
   linha()
   print(' 0 - Sair\n 1 - Comparar Cidades')
   print()
   try:
    opcao = input('Digite a opção: ')
    linha()
    return opcao
   except KeyboardInterrupt:
      print('\nPrograma finalizado pelo usuario')
      exit()


while True:

        opcao = menu()

        if opcao == "0":
            linha()
            print("Até Mais!!")
            linha()
            break
        elif opcao == "1":
            main()

   
