import os

print('Текущая директория: ', os.getcwd())
if os.path.exists('second'):  # это, чтобы не было ошибки, если директория уже существует
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория: ', os.getcwd())
# os.makedirs('third\\fours')
print(os.listdir())
for i in os.walk('.'):  # Точка обозначает текущую директорию
    print(i)
os.chdir(r'C:\Users\Василий\PycharmProjects\praktika_obychenie\praktika_obychenie\модуль_7_Работа_с_файлами_и_форматированный_вывод')
print('Текущая директория: ', os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]  # почему не работает как в уроке модуля 7 Файлы в операционной системе.
dirs = [d for d in os.listdir() if os.path.isfile(d)]
print(file)
print(dirs)
# https://urban-university.ru/members/courses/course999421818026/20231116-0000fajly-v-operacionnoj-sisteme-560779924863
# примерно 8:40 время видео.
# в результате вижу: 
# ['module_7_1.py', 'module_7_2.py', 'module_7_3.py', 'module_7_4.py', 'module_7_5.py', 'products.txt', 'sample.txt', 'sample2.txt', 'test.txt', 'вебинар.py', 'лорпа.py', 'прост.txt']
# ['module_7_1.py', 'module_7_2.py', 'module_7_3.py', 'module_7_4.py', 'module_7_5.py', 'products.txt', 'sample.txt', 'sample2.txt', 'test.txt', 'вебинар.py', 'лорпа.py', 'прост.txt']
