#Парсинг с помощью BeautifulSoup и requests
from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/' #Получить страницу
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser') # Парсинг страницы

# Ищет всё на сайте, что мы запросим
links = soup.find_all('a') # Ищет все ссылки c тегом a
for link in links: # Перебираем все
    print(link) # Вывести ссылки все