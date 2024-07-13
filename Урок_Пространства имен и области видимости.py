def test_function():
    print('Я из объемлющей области для функции inner_function')  # добавила для своего удобства

    def inner_function():
        print('Я в области видимости функции test_function')

    return inner_function()


print(test_function())  # без запроса вернуть inner_function() возвращает только свою строку принт
# но без проблем может обращаться к функции inner_function(), если указать строчку return inner_function()

print(inner_function())  # при попытке обратиться к этой функции из глобального пространства, получаем ошибку
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# тк эта функция находится вне области видимости.
# Мы можем внутри этой функции обратиться к значениям из объемлющей или глобальной области, наоборот не получится.
