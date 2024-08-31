def all_variants(text):
    for size in range(len(text)):
        for l in range(len(text)-size):
            yield text[l:l+size+1]


a = all_variants("abc")
for i in a:
    print(i)


# Домашнее задание по теме "Генераторы"
# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
#
# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:
# Пример работы функции:
# a = all_variants("abc")
# for i in a:
# print(i)
# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc
#
# Примечания:
# Для функции генератора используйте оператор yield.



# Марк Фабрицкий
# 19:48
# for i in range(1, len(text)+1):
#         for k in range(len(text)):
#             if k + i > len(text):
#                 continue
#             yield text[k:k+i]
# Алексей Мурыгин
# 19:48
# def all_variants(text):
#     for i in range(1, len(text) + 1):
#         for j in range(len(text) - i + 1):
#             yield(text[j:j+i])
#
# if __name__ == '__main__':
#     a = all_variants("abc")
#     print(a)
#     for i in a:
#         print(i)
