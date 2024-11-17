import sqlite3

connection = sqlite3.connect('database.db')  # Соединение с базой данных
cursor = connection.cursor()  # Мышка в базе данных

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')  # Что такое этот индекс? Его так и не обсудили

connection.commit()  # Сохраняет все изменения, фиксирует текущее состояние.
connection.close()  # Закрывает соединение с базой данных, чтобы освободить ресурсы.
