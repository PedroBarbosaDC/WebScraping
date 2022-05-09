from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('div',class_ = 'widget-title')

#soup.find_all('div', class_ = 'widget-title').h2.next_sibling
print(soup)

