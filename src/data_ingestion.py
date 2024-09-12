import requests
from dotenv import load_dotenv
import json
import os
from datetime import datetime, timedelta

load_dotenv()

url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json'
api_key = os.getenv("api_key")

# Função para gerar domingos
def generate_sundays(start_date, end_date):
    sundays = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 6:  # 6 é o código para domingo
            sundays.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return sundays

# Definindo o período de interesse
start_date = datetime(2020, 1, 5)  # Primeiro domingo de 2020
end_date = datetime(2023, 12, 31)

# Gerar domingos para o período de interesse
sundays = generate_sundays(start_date, end_date)

#literary genre
url = "https://api.nytimes.com/svc/books/v3/lists/names.json"

params = {
            'api-key': api_key
        }
response = requests.get(url, params=params)
print(response)
data = response.json()
results = data.get('results', [])
list_names = []         
for result in results:
    list_name = result.get('list_name_encoded')
    if list_name:
        list_names.append(list_name)

# print(list_names)
import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

# URL base da API
url_base = 'https://api.nytimes.com/svc/books/v3/lists/{date}/{list}.json'

# Sua chave de API
api_key = os.getenv("api_key")

def get_best_sellers(date, list_name):
    url = url_base.format(date=date, list=list_name)
    params = {
        'api-key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP
        
        # Obter o JSON da resposta
        data = response.json()
        return data
    
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# Exemplo de data e lista
date = '2023-09-01'  # Data no formato YYYY-MM-DD
list_name = 'hardcover-fiction'  # Nome da lista

best_sellers_data = get_best_sellers(date, list_name)

# Salvar os dados em um arquivo JSON
with open('best_sellers.json', 'w') as f:
    json.dump(best_sellers_data, f, indent=4)

print(f"Dados coletados para {list_name} em {date}.")
