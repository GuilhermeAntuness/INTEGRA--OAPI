import requests
import json

def criar_posts():
    """
    """
    try:

        url = "https://jsonplaceholder.typicode.com/posts"

        #headers = { 'Contant-type': }
        data = {
            "title": 'Meu titulo',
            "body": 'conteúdo teste',
            "userId": 1,

        }

        resposta = requests.post(url, json=data)
        print(resposta.status_code)
        resposta_api = resposta.json()
        print(resposta_api)


    except Exception as e:
        print('Erro!', e)

def atualizar_post():
    """
    """
    try:

        url = "https://jsonplaceholder.typicode.com/posts/1"

        #headers = { 'Contant-type': }
        data = {
            "title": 'Meu titulo',
            "body": 'conteúdo',
            "userId": 2,

        }

        resposta = requests.patch(url, json=data)
        print(resposta.status_code)
        resposta_api = resposta.json()
        print(resposta_api)


    except Exception as e:
        print('Erro!', e)

def mostrar_post():
    """
    """
    try:

        url = "https://jsonplaceholder.typicode.com/posts/1"

        resposta = requests.get(url)
        print(resposta.status_code)
        resposta_api = resposta.json()
        print(resposta_api)


    except Exception as e:
        print('Erro!', e)


mostrar_post()
atualizar_post()
mostrar_post()