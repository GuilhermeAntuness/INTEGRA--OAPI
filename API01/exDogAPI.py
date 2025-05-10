import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('KEY_DOG')

if not API_KEY:
    raise KeyError('Chave invalida consulte a pasta .env')


def get_image():

    url = 'https://api.thedog.com/v1/images/'

    headers = {
        'x-api-key' : API_KEY 
    }

    params = {
        'limit' : 'x'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        img = response.json()
        print(img)
        print()


        while True:
            try:
                number_images = int(input('Digite a quantidade de imagens que você quer: '))

                while 0 > number_images > 5:
                    print('A quantidade de imagens deve ser menor que 5!')

                if number_images == 0:
                    print('Até mais!!')
                    break

                if number_images < 5:
                    for i in range(number_images):
                        print(img[i]['url'])
                


            except Exception as e:
                print('Qantidade invalida',e)

    except requests.exceptions.RequestException as e:
        print('Erro inesperado', e)




get_image()