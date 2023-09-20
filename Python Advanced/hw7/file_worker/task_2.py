# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os

CATEGORIES_DICT = {'Videos': ['.mp4', '.avi', '.mov', '.flv', '.aaf', '.mkv', '.wmv', '.mpeg'],
                   'Pictures': ['.jpg', '.jpeg', '.gif', '.png', '.raw', '.psd', '.tiff'],
                   'Music': ['.mp3', '.flac', '.oog', '.wav', '.midi', '.m4a'],
                   'Documents': ['.pdf', '.doc', '.docs', '.csv', '.xls', '.xlsx', '.txt']}


def categorize_file(file_name: str, categories_dict: dict) -> str:
    """
    Функция для определения категории файла по его расширению.

    :param file_name: Название файла с расширением.
    :param categories_dict: Словарь с категориями файлов и их расширениями.
    :return: Категория файла или 'Other', если не найдено совпадений.
    """
    _, file_extension = os.path.splitext(file_name)
    for category, extensions in categories_dict.items():
        if file_extension in extensions:
            return category
    return "Other"


def sort_files_by_folders(source_path: str):
    """
    Функция для сортировки файлов в указанной папке по категориям.

    :param source_path: Путь к исходной папке с файлами.
    """
    if os.path.exists(source_path) and os.path.isdir(source_path):
        report_dict = dict()

        # Получаем данные по папке: её путь, вложенные папки и файлы
        files = os.listdir(source_path)
        for file in files:
            file_category = categorize_file(file, CATEGORIES_DICT)
            if file_category in CATEGORIES_DICT:
                move_file(source_path, file, file_category)
            report_dict[file_category] = report_dict.get(file_category, 0) + 1

        moved_files_report(report_dict)
    else:
        print(f"Путь '{source_path}' не существует или не является папкой.")


def move_file(source_path: str, file_name: str, file_category: str):
    """
    Функция для перемещения файла в соответствующую категорию.

    :param source_path: Путь к исходной папке.
    :param file_name: Имя файла.
    :param file_category: Категория файла.
    """
    source_file_destination = os.path.join(source_path, file_name)
    new_file_destination = os.path.join(source_path, file_category)

    if not (os.path.exists(new_file_destination) and os.path.isdir(new_file_destination)):
        os.mkdir(new_file_destination)

    new_destination_path = os.path.join(new_file_destination, file_name)
    os.rename(source_file_destination, new_destination_path)


def moved_files_report(report_dict: dict):
    """
    Функция для вывода отчета о перемещенных файлах.

    :param report_dict: Словарь с информацией о перемещенных файлах.
    """
    if report_dict:
        total_count = 0
        print('Были перемещены файлы следующих типов:')
        for file_category, count in report_dict.items():
            print(f'\t{file_category}: {count} файла(-ов);')
            total_count += count
        print(f'Всего перемещено {total_count} файла(-ов).')
    else:
        print('Файлы не были перемещены. Возможно, нет файлов для перемещения.')


if __name__ == '__main__':
    sort_files_by_folders('../Files')
