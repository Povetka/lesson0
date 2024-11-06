import unittest
import HumanMoveTest as Hum


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Hum.Runner('John Doe')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Hum.Runner('John Doe')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner = Hum.Runner('John Doe')
        runner_2 = Hum.Runner('Jane Doe')
        for i in range(10):
            runner.run()
        for j in range(10):
            runner_2.walk()
        self.assertNotEqual(runner.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
