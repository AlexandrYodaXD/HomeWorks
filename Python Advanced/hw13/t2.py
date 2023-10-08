# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или
# является пустой строкой.
# И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с
# плавающей запятой.
from typing import Union


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or len(text) == 0:
            raise InvalidTextError(text)
        self.text = text
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(number)
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


class InvalidTextError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid text: {self.value}. Text should be a non-empty string.'


class InvalidNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid number: {self.value}. Number should be a positive integer or float.'
