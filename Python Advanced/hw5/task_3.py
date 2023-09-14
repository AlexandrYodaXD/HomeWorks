# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os


def split_path(file_path):
    directory, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)

    return directory, filename, extension


file_path = "C:/folder/myfile.txt"
result = split_path(file_path)
print(result)
