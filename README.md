# Web Scraping no Mercado Livre 🌐🛒

Este script Python foi desenvolvido para realizar web scraping no Mercado Livre, extraindo informações sobre produtos de diferentes páginas da lista de pesquisa.

## Como Funciona 🚀

1. **Importando Bibliotecas:**
   - `requests`: Para fazer a solicitação HTTP.
   - `BeautifulSoup`: Para analisar o HTML da página.
   - `csv`: Para lidar com arquivos CSV.

```python
import requests
from bs4 import BeautifulSoup
import csv
```

2. **Função de Scraping do Mercado Livre:**
   - A função `scrape_mercadolivre` aceita uma URL do Mercado Livre como entrada e retorna uma lista de listas contendo nome e preço dos produtos.

```python
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
```

3. **Executando o Scraping e Escrevendo em um Arquivo CSV:**
   - O código principal faz uma iteração através de diferentes páginas da lista de pesquisa no Mercado Livre, executa a função de scraping e escreve os dados em um arquivo CSV chamado 'produtos.csv'.

```python
with open('produtos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Nome do Produto', 'Preço'])

    for i in range(1, 4):
        url = f'https://lista.mercadolivre.com.br/{i*50}'
        data = scrape_mercadolivre(url)
        writer.writerows(data)
```

## Executando o Código 🏃‍♂️

1. Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install requests beautifulsoup4
```

2. Execute o script Python.

```bash
python seu_script.py
```

3. Verifique o arquivo 'produtos.csv' para obter os nomes e preços dos produtos.

**Observação:** Certifique-se de cumprir os termos de serviço do Mercado Livre ao realizar web scraping.

Desfrute da exploração de produtos no Mercado Livre! 🛍️✨
