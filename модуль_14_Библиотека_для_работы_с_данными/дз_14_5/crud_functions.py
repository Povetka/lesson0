import sqlite3


def initiate_db():
    connection = sqlite3.connect('product_.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


initiate_db()


# connection = sqlite3.connect('product_.db')
# cursor = connection.cursor()
# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
#                    (f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
# connection.commit()
# connection.close()


def get_all_products():
    connection = sqlite3.connect('product_.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('product_.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, 1000)',
                   (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('product_.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result
