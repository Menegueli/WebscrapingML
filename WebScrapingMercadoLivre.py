import requests
from bs4 import BeautifulSoup
import csv

def scrape_mercadolivre(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('li', {'class': 'ui-search-layout__item'})

    data = []
    for product in products:
        name = product.find('h2', {'class': 'ui-search-item__title'}).text
        price = product.find('span', {'class': 'andes-money-amount__fraction'}).text
        data.append([name, price])
    return data

with open('produtos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Nome do Produto', 'Preço'])

    for i in range(1, 4):
        url = f'https://lista.mercadolivre.com.br/{i*50}'
        data = scrape_mercadolivre(url)
        writer.writerows(data)
