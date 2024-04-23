'''Незаконченный проект по парсингу wildberries'''
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=priceup&search=iphone'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
iphone_all = soup.find_all('article')
print(soup)
