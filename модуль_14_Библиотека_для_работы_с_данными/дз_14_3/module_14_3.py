from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = 'ключ улетел, но обещал вернуться'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kbr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

kbi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)

kbi_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product3', callback_data='product_buying'),
            InlineKeyboardButton(text='Product4', callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kbr)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kbi)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    formula = 'Формула Миффлина-Сан Жеора для расчета калорий для мужчин:\n' \
              'Калории = 10 * вес + 6.25 * рост - 5 * возраст + 5'
    await call.message.answer(formula)
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Упрощенный вариант формулы Миффлина-Сан Жеора для расчета калорий (для мужчин)
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


# часть дз 14_3 ___________________________________________________________________________________


@dp.message_handler(text='Купить')
async def buy_products(message):
    for i in range(1, 5):
        product_info = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        await message.answer(product_info)
        with open(f'product_photo/product{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kbi_products)


@dp.callback_query_handler(text='product_buying')
async def confirm_purchase(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# Домашнее задание по теме "Доработка бота"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
# Цель: подготовить Telegram-бота для взаимодействия с базой данных.
#
# Задача "Витамины для всех!":
# Подготовка:
# Подготовьте Telegram-бота из последнего домашнего задания 13 модуля сохранив код с ним в файл module_14_3.py.
# Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"
# Создайте хэндлеры и функции к ним:
# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи
# 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
# После каждой надписи выводите картинки к продуктам.
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
#
# Пример результата выполнения программы:
# Обновлённое главное меню:
#
# Список товаров и меню покупки:
#
#
#
# Примечания:
# Название продуктов и картинок к ним можете выбрать самостоятельно. (Минимум 4)
