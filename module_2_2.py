first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second and first == third:
    print('Все 3 числа совпали.')
elif first == second or first == third or second == third:
    print('Из введенных чисел 2 совпали.')
else:
    print('Из введенных чисел совпали 0.')