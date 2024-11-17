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

# for i in range(30):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)',
#                    (f'newuser{i}', f'{i}ex@email.com', str(randint(20, 60))))

# cursor.execute('SELECT * FROM Users')
#
# users = cursor.fetchall()
# for user in users:
#     print(user)  # Вывод результата

# SELECT FROM WHERE GROUP BY HAVING ORDER BY

# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (29,))
# users = cursor.fetchall()
# for user in users:
#     print(user)

cursor.execute('SELECT username, age FROM Users GROUP BY AGE')
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
