import requests
import json


def qtd_posts(x):
    """
    Consulta o site e mostra os posts
    Recebe a quantidade de posts que o usuario deseja ver
    Mostra os posts
    """
    try:
        resposta = requests.get("https://jsonplaceholder.typicode.com/posts")
        # print("Status code", resposta.status_code)
        posts = resposta.json()

        for post in posts[:x]:
            print()
            print('Titulo: ', post['title'])
            print('ID', post['Id'])
            print('Texto: ', post['body'])
            linha()
            print()

    except Exception as e:
        print('Erro!', e)

def linha():
    print('-='*30)


while True:

    try:
        linha()
        usuario = int(input('Quantos posts você deseja ver? [0 para sair]: '))
        #user = input('Digite o numero do  usuario ')
        linha()
        if usuario == 0:
            print('Até mais!!')
            break
        qtd_posts(usuario)

    except Exception as e:
        print('Erro', e)
