class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


if __name__ == '__main__':
    runner = Runner('John Doe')
    print(runner)

    runner.run()
    print(f'{runner.name} ran {runner.distance} meters')

    runner.walk()
    print(f'{runner.name} walked {runner.distance} meters')
