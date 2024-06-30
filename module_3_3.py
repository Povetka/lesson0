values_list = [3, False, 'Вупсень']
values_dict = {'a': 'Пупсень', 'b': ('d', 'j'), 'c': 7}
values_list_2 = ['Лунтик', 28]

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c = [1,2,3])

# Передайте values_list и values_dict в функцию print_params,
# используя распаковку параметров (* для списка и ** для словаря).

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры

print_params(*values_list_2, 42)

