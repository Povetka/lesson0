class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            elevator_path = range(1, new_floor + 1)
            return print(*elevator_path, sep='\n')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return bool(self.number_of_floors == other.number_of_floors)

    def __lt__(self, other):
        if isinstance(other, House):
            return bool(self.number_of_floors < other.number_of_floors)

    def __le__(self, other):
        if isinstance(other, House):
            return bool(self.number_of_floors <= other.number_of_floors)

    def __gt__(self, other):
        if isinstance(other, House):
            return bool(self.number_of_floors > other.number_of_floors)

    def __ge__(self, other):
        if isinstance(other, House):
            return bool(self.number_of_floors >= other.number_of_floors)

    def __ne__(self, other):
        if isinstance(other, House):
            return bool(self.number_of_floors != other.number_of_floors)

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
if __name__ == '__main__':
    h1.go_to(5)
    h2.go_to(10)


# Само задание:
#
# Домашняя работа по уроку "Атрибуты и методы объекта."
# Цель: применить на практике знания о классах, объектах и их атрибутах.
#
# Задача "Developer - не только разработчик":
# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.
#
# Пример результата выполнения программы:
# Исходные данные:
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"
# Примечания:
# self - это переменная указывающая на объект. Используйте её для обращения к атрибутам или методам объекта.
# Обращение к атрибутам или методам объекта/класса происходит при помощи "."
# Метод __init__ вызывается в момент создания объекта.
