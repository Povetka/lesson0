import unittest
from модуль_12_Поддержка_цикла_разработки.tests_from_lect import calc_12_modul as calc


class NewTest(unittest.TestCase):

    def test_sqrt(self):
        """
        Проверка функции квадратного корня
        """
        self.assertEqual(calc.sqrt(16), 4)

    @unittest.skip('Пока не нужен')
    def test_pov(self):
        """
        Проверка функции возведения в степень
        """
        self.assertEqual(calc.pov(2, 3), 8)
