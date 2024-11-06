# Вывод тоже не соответствует. Имена есть, но не пойму как указать номера участников.
import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrew", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            runner_names = [str(runner) for runner in v.values()]
            print(f"{k}: {', '.join(runner_names)}")

    def test_1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        self.all_results[1] = tour.start()
        self.assertTrue(self.all_results[1][2] == "Nick")

    def test_2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        self.all_results[2] = tour.start()
        self.assertTrue(self.all_results[2][2] == "Nick")

    def test_3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results[3] = tour.start()
        self.assertTrue(self.all_results[3][3] == "Nick")


if __name__ == '__main__':
    unittest.main()
