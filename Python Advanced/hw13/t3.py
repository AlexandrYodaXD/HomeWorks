# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет
# следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное
# число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным
# положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество,
# Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и
# InvalidAgeError, если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его
# ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.

class StringValidation:
    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) == 0:
            raise InvalidNameError(value)
        setattr(instance, self.name, value)


class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid name: {self.value}. Name should be a non-empty string.'


class PositiveIntegerValidation:
    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise InvalidAgeError(value)
        setattr(instance, self.name, value)


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid age: {self.value}. Age should be a positive integer.'


class IdValidation:
    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise InvalidAgeError(value)
        setattr(instance, self.name, value)


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid id: {self.value}. Id should be a positive integer.'


class Person:
    surname = StringValidation()
    name = StringValidation()
    patronymic = StringValidation()
    age = PositiveIntegerValidation()

    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    id_ = IdValidation()

    def __init__(self, surname, name, patronymic, age, id_):
        super().__init__(surname, name, patronymic, age)
        self.id_ = id_

    def get_level(self):
        tmp = self.id_
        res = 0
        while tmp:
            res += tmp % 7
            tmp %= 7
        return res


if __name__ == '__main__':
    p1 = Person('Иванов', 'Иван', 'Иванович', 42)
