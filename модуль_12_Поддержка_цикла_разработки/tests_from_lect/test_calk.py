import unittest
from модуль_12_Поддержка_цикла_разработки.tests_from_lect import calc_12_modul as calc


class CalkTest(unittest.TestCase):

    # def setUp(self):
    #     print('Я setUp')
    #
    # @classmethod
    # def setUpClass(cls):
    #     print('Я setUpClass')
    #
    # def tearDown(self):
    #     print('Я tearDown')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('Я tearDownClass')

    def test_add(self):
        """
        Проверка функции сложения
        """
        self.assertEqual(calc.add(2, 3), 5)

    def test_div(self):
        """
        Проверка функции деления
        """
        self.assertEqual(calc.div(10, 2), 5)

    def test_mul(self):
        """
        Проверка функции умножения
        """
        self.assertEqual(calc.mul(2, 3), 6)

    def test_sub(self):
        """
        Проверка функции вычитания
        """
        self.assertEqual(calc.sub(5, 3), 2)


if __name__ == '__main__':
    unittest.main()
