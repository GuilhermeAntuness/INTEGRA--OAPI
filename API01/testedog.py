#Criar um programa que:
#Peça um usuário para digitar a quantidade de cachorros que ele deseja buscar.
#Crie um limitador para controlar o input do usuário, não deixe que ele digite mais do que 5
#Faça um consulta de formato de lista na API da TheDogAPI, para buscar imagens aleatórias de cachorros.
#Mostre as informações de forma organizada para o usário
 
import requests
import os
from dotenv import load_dotenv
 
def encontrar_imagem():
    # Carregar variáveis de ambiente do .env
    load_dotenv()
 
    # Obter a API Key do ambiente
    api_key = os.getenv('KEY_DOG')
 
    #Verificar a existência da API
    if not api_key:
        raise ValueError('API Key não foi localizada nas variáveis de ambiente.')
 
    # URL da rota de busca de imagem
    url = 'https://api.thedogapi.com/v1/images/search'
 
    headers = {
       'x-api-key' : api_key
    }
    params = {
        'has_breeds' : 1
    }
   
    # Realizar a requisição GET
    while True:
         x = int(input('Digite quantas imagens você deseja pesquisar: '))
         if x > 5:
          print('Não é possível pesquisar mais do que 5 imagens!')
         
         elif x == 0:
          print('É necessário pesquisar ao menos 1 imagem!')
         
         elif x < 0:
          print('Não é possível digitar números minúsculos')
       
         else:
           for i in range(x):
            resposta = requests.get(url, headers=headers, params=params)
            print(resposta.status_code)
            resposta = resposta.json()
           
            print(f"Imagem {i + 1}: {resposta[0]['url']}")
 
         break
       
def menu():
    #Exibe o menu principal com as opções disponíveis para o usuário.
    print('\n MENU')
    print('-'*30)
    print('0 - SAIR')
    print('1 - Realizar pesquisa de imagens')
   
 
    opcao = input('Escolha uma das opções acima: ')
 
    return opcao
 
 
while True:
 
    opcao = menu()
 
    if opcao == '1':
        encontrar_imagem()
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('É necessário digitar uma opção válida!')
   
 
   