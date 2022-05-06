from bs4 import BeautifulSoup
import requests

url = 'https://www.terabyteshop.com.br'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('div',class_ = 'commerce_columns_item_inner')

print(soup)


