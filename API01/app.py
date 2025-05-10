from dotenv import load_dotenv
import os

# Carrega as variaveis do arquivo .env
load_dotenv()

# Acessa as variaveis do ambiente
api_key = os.getenv('API_KEY')

print(api_key)