import unittest
from модуль_12_Поддержка_цикла_разработки.tests_from_lect import test_calk, test_calk_2

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calk.CalkTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calk_2.NewTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)

