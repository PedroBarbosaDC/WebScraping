from email import header
from nturl2path import url2pathname
import requests
from bs4 import BeautifulSoup

url = 'https://pedaocds.wixsite.com/curriculo'

header = {
    'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}

site = requests.get(url_pag, headers=header)
soup = BeautifulSoup(site.content, 'html.parser')
infos_dados = soup.find_all('div',class_='mesh-layout')
