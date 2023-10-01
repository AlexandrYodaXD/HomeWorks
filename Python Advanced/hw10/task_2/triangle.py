import math


class Triangle:
    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self._check_exists():
            raise ValueError(f'Треугольник со сторонами ({self.side_a}, {self.side_b}, {self.side_c}) не существует.')

    def _check_exists(self):
        if all((
                (self.side_a + self.side_b > self.side_c),
                (self.side_b + self.side_c > self.side_a),
                (self.side_c + self.side_a > self.side_b)
        )):
            return True
        return False

    def perimeter(self):
        return sum((self.side_a, self.side_b, self.side_c))

    def area(self):
        p = self.perimeter()
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
