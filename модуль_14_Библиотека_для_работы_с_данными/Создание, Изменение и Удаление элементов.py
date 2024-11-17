import sqlite3

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

# cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)',
#                ('newuser', 'ex@email.com', '28'))
# for i in range(30):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)',
#                    (f'newuser{i}', f'{i}ex@email.com', f'28'))

# cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (32, 'newuser'))

# cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser0',))

connection.commit()
connection.close()
