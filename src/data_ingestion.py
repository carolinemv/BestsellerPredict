import requests
from dotenv import load_dotenv
import json
import os
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv
import json
import os

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
# sundays = generate_sundays(start_date, end_date)

# print(sundays)

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
        extracted_info =[]
        response = requests.get(url, params=params)
        data = response.json()
        results = data['results']
        books = results['books'][1]
        extracted_info.append({
                    'List Name': results['list_name'],
                    'Bestsellers Date': results['bestsellers_date'],
                    'Published Date': results['published_date'],
                    'Rank': books['rank'],
                    'Weeks on List': books['weeks_on_list'],
                    'Publisher': books['publisher'],
                    'Title': books['title'],
                    'Author': books['author'],
                    'isbn13': books['primary_isbn13']
                })

        return extracted_info
    
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# Exemplo de uso
date = '2020-01-05'
list_name = 'hardcover-fiction'  # Exemplo de lista, ajuste conforme necessário

data = get_best_sellers(date, list_name)

with open('best_sellers.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Dados coletados para {list_name} em {date}.")
