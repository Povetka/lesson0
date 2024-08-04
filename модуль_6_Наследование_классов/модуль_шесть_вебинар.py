# это с вебинара по модулю
class Geom:
    name = 'Geom'
    def __init__(self, x1, y1, x2, y2, fill=None):
        print(f'Инициализация родительского класса для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
class Line(Geom):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        print(f'Инициализация Line')
    def draw(self):
        print('Рисование линии')

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print(f'Инициализация Rect')
    def draw(self):
        print('Рисование прямоугольника')

l = Line(0, 0, 10, 20)
l.draw()
print(l.name)
print(l.x1, l.y1, l.x2, l.y2)
r = Rect(5, 5, 15, 15, fill='red')
r.draw()

print(r.x1, r.y1, r.x2, r.y2)