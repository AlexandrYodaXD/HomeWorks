# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_renaming(source_path: str, source_extension: str, target_name: str,
                   target_extension: str = None, particle_size: int = 1, original_name_retained_range: tuple[int] = None):
    """
    Функция для группового переименования файлов в указанной директории.

    :param source_path: Путь к директории, в которой нужно переименовать файлы.
    :param source_extension: Расширение исходных файлов, которые нужно переименовать.
    :param target_name: Желаемое конечное имя для переименованных файлов.
    :param target_extension: Расширение конечных файлов после переименования.
    :param particle_size: Количество цифр в порядковом номере для добавления к конечному имени.
    :param original_name_retained_range: Диапазон символов, которые нужно сохранить из исходного имени файла
    (границы включительно).
    """
    if os.path.exists(source_path) and os.path.isdir(source_path):
        # Список, содержащий все подходящие по расширению файлы
        file_list = []

        # Наполнение списка
        files = os.listdir(source_path)
        for file in files:
            _, extension = os.path.splitext(file)
            if extension == source_extension:
                file_list.append(file)

        # Обновление значения particle_size
        # Если окажется что кол-во символов для числового суффикса в particle_size меньше,
        # чем требуется по кол-ву файлов, то он будет скорректирован в большую сторону
        particle_size = len(str(max((10 ** (particle_size - 1)), len(file_list))))

        # Цикл для работы с файлами из получившегося списка
        for i in range(len(file_list)):
            file = file_list[i]
            file_name, extension = os.path.splitext(file)

            # Список, из которого в результате будет собрано новое имя файла
            new_file_name_list = []

            # Если указан срез для имени из исходного файла, то добавляем его в список
            if original_name_retained_range is not None:
                start = original_name_retained_range[0] - 1
                end = original_name_retained_range[1]
                new_file_name_list.append(file_name[start:end])

            # Добавляем целевое имя
            new_file_name_list.append(target_name)

            # Добавляем числовой суффикс
            particle = str(i + 1)
            while len(particle) < particle_size:
                particle = '0' + particle
            new_file_name_list.append(particle)

            # Если целевое расширение не было передано, то будет использовано исходное расширение
            if target_extension is None:
                new_file_name = '_'.join(new_file_name_list) + source_extension
            else:
                new_file_name = '_'.join(new_file_name_list) + target_extension

            # Собираем новое имя файла и путь воедино
            source_file_destination = os.path.join(source_path, file)
            new_file_destination = os.path.join(source_path, new_file_name)

            # Переименование
            print(f'{source_file_destination} -> {new_file_destination}')
            os.rename(source_file_destination, new_file_destination)

    else:
        print(f"Путь '{source_path}' не существует или не является папкой.")


if __name__ == '__main__':
    group_renaming('../Files/', '.zip', 'new',
                   '.rar', 2, (1, 3))
