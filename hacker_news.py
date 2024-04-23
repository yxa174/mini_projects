import requests
from bs4 import BeautifulSoup
from translate import Translator
import pyshorteners
import sqlite3
shortener = pyshorteners.Shortener()
url = 'https://news.ycombinator.com/newest'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

head = soup.find_all('tr', class_='athing')

conn = sqlite3.connect('h_news.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS links
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, link INTEGER)''')


translator = Translator(to_lang='ru')

for header in head:
   s = translator.translate(header.text)
   words =s.split()
   result = " ".join(words[1:])
   link = header.find('span', class_='titleline').find('a').get('href')
   if 'http' in link:
    link_data = [
        ( result, link),
    ]
    cursor.executemany('INSERT INTO links (title, link) VALUES (?, ?)', link_data)
   else:
    link_data = [
        (result, "https://news.ycombinator.com/" + link)
    ]
   cursor.executemany('INSERT INTO links (title, link) VALUES (?, ?)', link_data)

cursor.execute("DELETE FROM links WHERE rowid NOT IN (SELECT MIN(rowid) FROM links GROUP BY title)")
cursor.execute("DELETE FROM links WHERE id >= 30;")


conn.commit()
conn.close()
