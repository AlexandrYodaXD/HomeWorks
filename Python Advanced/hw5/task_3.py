# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def split_file_path(file_path):
    directory, file_name = file_path.rsplit('/', 1)
    name, extension = file_name.rsplit('.', 1)

    return directory, name, '.' + extension


file_path = "C:/folder/myfile.txt"
result = split_file_path(file_path)
print(result)
