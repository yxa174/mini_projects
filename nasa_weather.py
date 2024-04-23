
'''Парсинг погоды на марсе с сайта nasa'''
import re
import requests
from bs4 import BeautifulSoup
import pprint
# for i in range(13):
#     url = 'https://weakpass.com/wordlist/small?page={}'.format(int(i)+1)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')

#     with open("output.txt", "a") as file:
#         linksall = soup.find_all('footer', class_="card-footer")
#         print("Number of footers found:", len(linksall))  # Отладочный вывод
#         for footer in linksall:
#             links = footer.find_all('a')
#             for link in links:
#                 if not re.search(r'torrent', link['href']):
#                     print("Writing link to file:", link['href'])  # Отладочный вывод
#                     # Записываем каждую ссылку в файл
#                     file.write(link['href'] + "\n")
# url = 'https://mars.nasa.gov/msl/mission/weather/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# s = soup.find_all('div')
# for i in s:
#     print(i)
s = requests.get('https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json')
data = s.json()

s1 = data["soles"]
s2 = s1[0]['max_temp']
print(f"сегодня: {s1[0]['terrestrial_date']},\nтемпература на марсе: {s2}°С")
bot_token = '5910001413:AAHPJArd-innwC9TmAIbMvioQIK5eqRcTMc'
chat_ID = '61775513'
requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_ID}&text=hello')
