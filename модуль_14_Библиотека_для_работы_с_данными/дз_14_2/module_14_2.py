import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))
connection.commit()

cursor.execute('UPDATE Users SET balance = 500 WHERE id IN (SELECT id FROM Users WHERE id % 2 = 1)')
connection.commit()

cursor.execute('DELETE FROM Users WHERE id IN (SELECT id - 2 FROM Users WHERE id % 3 = 0)')
connection.commit()

cursor.execute('DELETE FROM Users WHERE id = 6')
connection.commit()

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(f'Средний баланс всех пользователей: {all_balances/total_users}')

# # Так было бы короче:
# cursor.execute('SELECT AVG(balance) FROM Users')
# avg_b = cursor.fetchone()[0]
# print(f'Средний баланс всех пользователей: {avg_b}')

connection.close()


# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
#
# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователей.
#
#
#
# Пример результата выполнения программы:
# Выполняемый код:
# # Код из предыдущего задания
# # Удаление пользователя с id=6
# # Подсчёт кол-ва всех пользователей
# # Подсчёт суммы всех балансов
# print(all_balances / total_users)
# connection.close()
#
# Вывод на консоль:
# 700.0
