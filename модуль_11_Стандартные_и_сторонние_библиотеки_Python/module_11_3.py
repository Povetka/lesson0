import inspect
from pprint import pprint


class IntrospectionInfo:
    def __init__(self, obj):
        self.obj = obj
        self.info = {}

        # Узнаем тип объекта
        self.info['type'] = type(self.obj).__name__

        # узнаем атрибуты объекта
        self.info['attributes'] = [attr for attr in dir(self.obj) if not callable(getattr(self.obj, attr))]

        # Узнаем методы объекта
        self.info['methods'] = [method for method in dir(self.obj) if callable(getattr(self.obj, method))]

        # Узнаем в каком модуле находится объект
        module = inspect.getmodule(self.obj)
        self.info['module'] = module.__name__ if module else None

        # Другие интересные свойства =)
        if isinstance(self.obj, (int, float, str)):
            self.info['value'] = self.obj
        elif isinstance(self.obj, list):
            self.info['length'] = len(self.obj)
        elif isinstance(self.obj, dict):
            self.info['keys'] = list(self.obj.keys())
        elif hasattr(self.obj, 'shape'):
            self.info['shape'] = self.obj.shape

    def pprint_info(self):
        pprint(self.info)


# Пример работы:
number_info = IntrospectionInfo(42)
number_info.pprint_info()

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
