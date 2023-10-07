# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
# недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе
# взятых.
import copy
import csv


class CapitalizedAlphaString:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise ValueError("Значение должно быть строкой")

        if not value.isalpha() and not value.istitle():
            raise ValueError("Строка должна начинаться с заглавной буквы и содержать только буквы.")

        setattr(instance, self.name, value)


class RangedNumber:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value: int):
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        if value not in range(self.min_value, self.max_value + 1):
            raise ValueError(f"Значение должно быть в заданном диапазоне ({self.min_value}-{self.max_value}).")

        setattr(instance, self.name, value)


class DefaultDict(dict):
    def __init__(self, keys_collection, default=None):
        self.keys_collection = set(keys_collection)
        super().__init__()
        self.default = default

    def __getitem__(self, key):
        if key not in self.keys_collection:
            raise ValueError(f"Предмет {key} не найден")
        super().setdefault(key, copy.deepcopy(self.default))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if key not in self.keys_collection:
            raise ValueError(f"Предмет {key} не найден")
        super().setdefault(key, copy.deepcopy(self.default))
        super().__setitem__(key, value)


class Student:
    name = CapitalizedAlphaString()
    grade = RangedNumber(2, 5)
    test_score = RangedNumber(0, 100)

    def __init__(self, name, subjects_file):
        self.name = name
        with open(subjects_file, 'r', encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            self.subjects = DefaultDict(next(csv_reader), {'grades': [], 'test_score': []})

    def __str__(self):
        return (f'Студент: {self.name}\n'
                f'Предметы: {", ".join(self.subjects)}')

    def add_subject(self, subject, grade, test_score):
        """
        Метод для добавления информации о предмете, оценке и результате теста.
        :param subject: Предмет
        :param grade: Оценка по предмету
        :param test_score: Результат теста
        :return:
        """

    def add_grade(self, subject, grade):
        """
        Метод для добавления оценки по предмету
        :param subject:
        :param grade:
        :return:
        """
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        """
        Метод для добавления результата теста по предмету
        :param subject:
        :param test_score:
        :return:
        """
        self.subjects[subject]['test_score'].append(test_score)

    def get_average_grade(self):
        """
        Метод, возвращающий средний балл студента по всем предметам.
        :return: Средний балл студента по всем предметам
        """
        res = 0
        cnt = 0
        for subject, marks in self.subjects.items():
            if marks['grades']:
                res += sum(marks['grades'])
                cnt += len(marks['grades'])
        return res / cnt

    def get_average_test_score(self, subject):
        """
        Метод, возвращающий средний результат тестов по предмету
        :param subject: Предмет
        :return: Средний результат тестов по предмету
        """
        subj = self.subjects[subject]['test_score']
        if subj:
            return sum(subj) / len(subj)

    def get_subjects(self):
        """
        Метод, возвращающий список всех предметов, по которым есть информация у студента.
        :return: Список всех предметов, по которым есть информация у студента
        """
        for subject, marks in self.subjects.items():
            if marks['grades']:
                print(f'{subject}: {marks["grades"]}')


def get_average_grades(students):
    """
    Функция принимает список студентов и выводит информацию о средних баллах для каждого студента.
    :param students:
    :return:
    """
    pass


def get_subject_average(students, subject):
    """
    Функция принимает список студентов и название предмета, и выводит информацию о среднем балле по этому предмету
    для каждого студента.
    :param students:
    :param subject:
    :return:
    """


def get_top_student(students, subject):
    """
    Функция принимает список студентов и название предмета, и выводит информацию о студенте с наивысшим средним
    баллом по этому предмету.
    :param students:
    :param subject:
    :return:
    """


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
