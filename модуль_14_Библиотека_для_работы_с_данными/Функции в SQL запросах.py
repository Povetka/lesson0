import sqlite3
from random import randint

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# SELECT FROM WHERE GROUP BY HAVING ORDER BY

# cursor.execute('SELECT COUNT(*) FROM Users WHERE age > ?', (28,))
# total1 = cursor.fetchone()[0]
# print(total1)

# cursor.execute('SELECT SUM(age) FROM Users')
# total1 = cursor.fetchone()[0]
#
# cursor.execute('SELECT COUNT(*) FROM Users')
# total2 = cursor.fetchone()[0]
#
# print(total1, total1/total2)
#
# cursor.execute('SELECT AVG(age) FROM Users')
# avg_age = cursor.fetchone()[0]
# print(avg_age)

cursor.execute('SELECT MIN(age) FROM Users')
min_age = cursor.fetchone()[0]
print(min_age)

cursor.execute('SELECT MAX(age) FROM Users')
max_age = cursor.fetchone()[0]
print(max_age)


connection.commit()
connection.close()
