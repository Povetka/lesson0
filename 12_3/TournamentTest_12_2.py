import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

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
            print(f'{k}: {v}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        self.all_results[1] = tour.start()
        self.assertTrue(self.all_results[1][2] == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        self.all_results[2] = tour.start()
        self.assertTrue(self.all_results[2][2] == "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results[3] = tour.start()
        self.assertTrue(self.all_results[3][3] == "Nick")


if __name__ == '__main__':
    unittest.main()
