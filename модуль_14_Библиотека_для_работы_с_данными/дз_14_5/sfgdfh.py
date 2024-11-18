import sqlite3
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import get_all_products

api = 'ДАННЫЕ УДАЛЕНЫ'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

def initiate_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Users
                 (id INTEGER PRIMARY KEY,
                  username TEXT NOT NULL,
                  email TEXT NOT NULL,
                  age INTEGER NOT NULL,
                  balance INTEGER NOT NULL)''')
    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)",
              (username, email, age))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = int(message.text)
    add_user(username, email, age)
    await message.answer(f'Регистрация завершена. Пользователь {username} добавлен в базу данных.')
    await state.finish()


if __name__ == '__main__':
    initiate_db()
    executor.start_polling(dp, skip_updates=True)
