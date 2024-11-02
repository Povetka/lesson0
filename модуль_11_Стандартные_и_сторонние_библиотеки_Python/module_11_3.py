import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}

    # Узнаем тип объекта
    info['type'] = type(obj).__name__

    # узнаем атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    # Узнаем методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Узнаем в каком модуле находится объект
    module = inspect.getmodule(obj)
    info['module'] = module.__name__ if module else None

    # Другие интересные свойства =)
    if isinstance(obj, (int, float, str)):
        info['value'] = obj
    elif isinstance(obj, list):
        info['length'] = len(obj)
    elif isinstance(obj, dict):
        info['keys'] = list(obj.keys())
    elif hasattr(obj, 'shape'):
        info['shape'] = obj.shape

    return info


# Пример работы:
number_info = introspection_info(42)
pprint(number_info)

# Домашнее задание по теме "Интроспекция"
# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
# и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания
