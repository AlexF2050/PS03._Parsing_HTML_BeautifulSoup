#Парсинг с помощью BeautifulSoup и requests
#print(link.get('href')) #Выводим ссылки которые есть на сайте

from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/' #Получить страницу
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser') # Парсинг страницы

# создадим функцию text в которой будут хранится все статьи

#text = soup.find('span', class_='text') # find ищет первое совпадение по span
text = soup.find_all('span', class_='text') # find ищет всё по span
author = soup.find_all('small', class_='author')

for i in range(len(text)): #Выводим все статьи несколько раз
    print(f'Цитата номер - {i+ 1}')
    print(text[i].text)
    print(f'Автор цитаты - {author[i].text}\n') #Выводим все статьи

# \n - перенос строки для разделения и удобства чтения