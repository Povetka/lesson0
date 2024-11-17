from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from keyboard import *
from admin import *
from db import *
import texts
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


# Для ответов картинками, видео, файлами:
# message.answer_photo
# .answer_video
# .answer_file

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Бобро поржаловать, {message.from_user.username}! ' + texts.start, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def price(message):
    with open('photo/правдоруб.jpg', 'rb') as img:
        await message.answer_photo(img, texts.about, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def info(message):
    await message.answer(texts.choice, reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')  # вот с этой перестали работать
async def buy_m(call):
    await call.message.answer(texts.Mgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='big')
async def buy_l(call):
    await call.message.answer(texts.Lgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    await call.message.answer(texts.XLgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer(texts.choice, reply_markup=catalog_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
