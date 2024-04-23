'''Тест работы с базами данных с python sqlite3'''
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('h_news.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM links LIMIT 1")
result = cursor.fetchall()

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
for i in result:
    print(i[1], i[2])
