# Инкапсулированный атрибут __file_name = 'products.txt'. Инкапсулированный, это как?
class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"'{self.name}', {self.weight}, '{self.category}'"  # вот это еще сама написать догадалась


class Shop():  # вот не совсем понимаю про инит. Написала я инит, в нем селф, а в этой ситуации дальше что писать?
    def __init__(self):
        self.__file_name = 'products.txt'  # почему это тут, а не в def get_products?

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_from_file = file.read()
        file.close()
        return products_from_file

    # def get_products(self):
    #     open(self.__file_name, 'r')
    #     products_from_file = self.__file_name.read()
    #     self.__file_name.close()
    #     return products_from_file
    #     Не пойму, почему этот вариант не работает.

    def add(self, *products):
        self.file = open(self.__file_name, 'a')  # почему тут self.file, а не file,
        # раньше просто файл написала и было ок, а тут без селф не работает.
        for product in products:
            if product.name not in self.get_products():  # не доходит, почему тут нейм и метод get_products()
                # еще и с селф, я думала сюда нужно писать снова файл, снова его открывать.
                # Смутно догадываюсь почему так, но вот понять все еще не могу
                self.file.write(str(product) + '\n')
                self.file.seek(0)
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


# Домашнее задание по теме "Режимы открытия файлов"
#
# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
#
# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name,
# закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
#
# Пример результата выполнения программы:
# Пример работы программы:
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# p3 = Product('Potato', 5.5, 'Vegetables')
#
# print(p2) # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())
#
# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Как выглядит файл после запусков:
#
#
#
# Примечания:
# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.
