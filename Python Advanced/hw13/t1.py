# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается при
# некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.
class Rectangle:
    def __init__(self, width: int, height: int = None):
        if height is None:
            height = width
        if width < 0:
            raise NegativeValueError(width, height)
        self.width = width
        if height < 0:
            raise NegativeValueError(width, height)
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        weight = self.width + other.width
        height = self.height + other.height
        return Rectangle(weight, float(height))

    def __sub__(self, other):
        weight = self.width - other.width
        height = self.height - other.height
        return Rectangle(weight, float(height))

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"

class NegativeValueError(Exception):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width < 0:
            return f'Ширина должна быть положительной, а не {self.width}'
        if self.height < 0:
            return f'Высота должна быть положительной, а не {self.height}'

if __name__ == '__main__':
    r = Rectangle(-2)