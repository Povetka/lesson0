my_dict = {'Вася': 1995, 'Вика': 1992, 'Бааааарсик': 'хороший кот'}
print(my_dict)
print(my_dict['Бааааарсик'])
print(my_dict.get('Ииииигорь', 'Такого тут нет'))
my_dict.update({'Маша': 2015, 'Борис': 2007})
a = my_dict.pop('Вася')
print(a)
print(my_dict)
my_set = {1, 1, 2, 2, 3, 4, 1, 5, 4, 1, 2, 4, 3, 1, 4, 5, 2, 3, 1, 4, 2,
          'f', 'h', 'g', 'h', 'd', 'j', 'g', 'd', 'g', 'j'}
print(my_set)
my_set.update({9, 'P'})
my_set.remove(1)
print(my_set)