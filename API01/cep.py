import requests
import json

def consultar_cep(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(url.status_code)
    response = url.json()


    if url.status_code == 200:
        print('Cep - ', response['cep'])
        print('Logradouro - ', response['logradouro'])
        print('Bairro - ', response['bairro'])
        print('Localidade - ', response['localidade'])
        print('UF - ', response['uf'])
        print('Estado - ', response['estado'])
        print('Região - ', response['regiao'])
        print('DDD - ', response['ddd'])
    
    else:
        print('Erro! ')


while True:
    cep = input('Digite o CEP que você deseja consultar: ')
    if cep == 0:
        break

    consultar_cep(cep)

