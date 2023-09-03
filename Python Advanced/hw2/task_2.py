# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions


class MyFraction:
    def __init__(self, data: str):
        splitted = data.split('/')
        if len(splitted) == 2 and all((splitted[0].isalnum(),
                                              splitted[1].isalnum())):
            self._numerator = int(splitted[0])
            self._denominator = int(splitted[1])
        else:
            raise ValueError('Введена некорректная дробь. Дробь должна быть в виде a/b')
        if self._denominator == 0:
            raise ZeroDivisionError('Введена некорректная дробь. Знаменатель не должен быть нолем.')

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return str(self._numerator) + '/' + str(self._denominator)

    def __add__(self, other):
        if isinstance(other, MyFraction):
            self.simplification()
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return MyFraction(str(numerator) + '/' + str(denominator)).simplification()
        elif isinstance(other, int):
            numerator = self.numerator + other * self.denominator
            return MyFraction(str(numerator) + '/' + {self.denominator}).simplification()
        else:
            raise TypeError('Дробь сейчас можно перемножать только с дробью или целым числом')

    def __mul__(self, other):
        if isinstance(other, MyFraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return MyFraction(str(numerator) + '/' + str(denominator)).simplification()
        elif isinstance(other, int):
            numerator = self.numerator * other
            return MyFraction(str(numerator) + '/' + {self.denominator}).simplification()
        else:
            raise TypeError('Дробь сейчас можно перемножать только с дробью или целым числом')

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value: int):
        if isinstance(value, int):
            self._numerator = value
        else:
            raise TypeError('Числитель должен быть целым числом')

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if isinstance(value, int):
            if value != 0:
                self._denominator = value
            else:
                raise ValueError('Знаменатель не должен быть нолём')
        else:
            raise TypeError('Знаменатель должен быть целым числом')

    # Упрощение дроби с рекурсией
    def simplification(self):
        old = self.__str__()
        i = 2
        while i <= max(self._numerator, self._denominator):
            while self._numerator % i == 0 and self._denominator % i == 0:
                self._numerator //= i
                self._denominator //= i
            i += 1

        if old != self.__str__():
            return self.simplification()
        return self


# СЛОЖЕНИЕ
a = '5/8'
b = '3/14'
# Мой класс
f1 = MyFraction(a)
f2 = MyFraction(b)
print(f'MyFraction сложение: {f1} + {f2} = {f1 + f2}')

# fractions
f1 = fractions.Fraction(a)
f2 = fractions.Fraction(b)
print(f'fraction сложение: {f1} + {f2} = {f1 + f2}')

# УМНОЖЕНИЕ
a = '2/3'
b = '3/4'
# Мой класс
f1 = MyFraction(a)
f2 = MyFraction(b)
print(f'MyFraction умножение: {f1} * {f2} = {f1 * f2}')

# fractions
f1 = fractions.Fraction(a)
f2 = fractions.Fraction(b)
print(f'fraction умножение: {f1} * {f2} = {f1 * f2}')
