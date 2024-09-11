import requests 
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json'

api_key = os.getenv("api_key")

# Parâmetros da requisição
params = {
    'api-key': api_key
}

response = requests.get(url, params=params)

# Verificando o status da requisição
if response.status_code == 200:
    data = response.json()
    # Exibir os dados recebidos
    print(data)
else:
    print(f"Erro na requisição: {response.text}")