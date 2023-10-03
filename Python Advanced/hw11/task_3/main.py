# Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет
# представлять прямоугольник с заданными шириной и высотой.
#
# Класс Rectangle должен иметь следующие атрибуты и методы:
#
# Атрибуты:
#
# width (int): ширина прямоугольника.
# height (int): высота прямоугольника.
#
# Методы:
#
# perimeter(): метод для вычисления периметра прямоугольника. Возвращает периметр как целое число.
# area(): метод для вычисления площади
# прямоугольника. Возвращает площадь как целое число. __add__(other): метод, позволяющий складывать два
# прямоугольника. Возвращает новый прямоугольник с шириной и высотой, равными сумме соответствующих атрибутов
# исходных прямоугольников.
# __sub__(other): метод, позволяющий вычитать один прямоугольник из другого. Возвращает новый прямоугольник с шириной
# и высотой, равными разности соответствующих атрибутов исходных прямоугольников.
# __lt__(other): метод, определяющий, является ли текущий прямоугольник меньше по площади, чем другой прямоугольник.
# Возвращает True, если площадь текущего прямоугольника меньше площади другого, и False в противном случае.
# __eq__(other): метод, определяющий, равны ли два прямоугольника по площади. Возвращает True, если площади равны,
# и False в противном случае.
# __le__(other): метод, определяющий, меньше или равен текущий прямоугольник по площади, чем другой прямоугольник.
# Возвращает True, если площадь текущего прямоугольника меньше или равна площади другого, и False в противном случае.
# __str__(): метод для получения строкового представления прямоугольника. Возвращает строку с информацией о ширине и
# высоте прямоугольника.
# __repr__(): метод для получения строкового представления прямоугольника, которое может быть использовано для
# создания нового объекта.

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
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

if __name__ == '__main__':
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))
