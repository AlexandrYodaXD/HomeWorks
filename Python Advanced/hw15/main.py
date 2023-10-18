# 📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌~~Соберите информацию о содержимом в виде объектов namedtuple.~~
# 📌Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
import os
from collections import namedtuple

# Оставил т. к. в задании он требуется, но без него, мне кажется, проще и лучше
File_info = namedtuple('File_info', ['name', 'extension', 'is_dir', 'parent_dir'])
logger = logging.getLogger(__name__)
logging.basicConfig(filename='files_log.log', filemode='w', encoding='UTF-8', level=logging.INFO, style='{',
                    format='{asctime} - {name} - {levelname} - {message}',
                    datefmt='%Y-%m-%d %H:%M:%S')


def traverse_and_save(directory_path):
    for root, dirs, files in os.walk(directory_path):
        parent_dir = os.path.basename(root)
        for file_name in files:
            file_path = os.path.join(root, file_name)
            full_name, extension = os.path.splitext(file_path)
            base_name = os.path.basename(full_name)
            # Оставил т. к. в задании он требуется, но без него, мне кажется, проще и лучше
            File_info(base_name, extension, False, parent_dir)
            logger.info(msg=f'Name: "{base_name}",'.ljust(32) + '\t'
                            f'Is folder: YES,'.ljust(20) + '\t'
                            f'File extension: {extension},'.ljust(32) + '\t'
                            f'Parent directory: {parent_dir}')
        for dir_name in dirs:
            base_name = os.path.basename(dir_name)
            # Оставил т. к. в задании он требуется, но без него, мне кажется, проще и лучше
            File_info(dir_name, None, True, parent_dir)
            logger.info(msg=f'Name: "{base_name}",'.ljust(32) + '\t'
                            f'Is folder: YES,'.ljust(20) + '\t'
                            f'File extension: folder,'.ljust(32) + '\t'
                            f'Parent directory: {parent_dir}')


traverse_and_save('.')
