# Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
import csv
import json
import os
import pickle


def get_directory_size(path):
    total_size = 0
    for dir_path, dir_names, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dir_path, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def traverse_and_save(directory_path, path_to_save='./'):
    # Создаем пустые списки для сохранения данных
    json_data = []
    csv_data = []
    pickle_data = []

    # Рекурсивно обходим директорию
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            is_directory = False

            if os.path.isdir(file_path):
                is_directory = True
                size = get_directory_size(file_path)
            else:
                size = os.path.getsize(file_path)

            # Чтение данных из файла
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            # Создаем словарь для JSON
            json_entry = {
                'file_path': file_path,
                'is_directory': is_directory,
                'size_bytes': size,
                'content': file_content
            }
            json_data.append(json_entry)

            # Создаем кортеж для CSV
            csv_entry = (file_path, is_directory, size, file_content)
            csv_data.append(csv_entry)

            # Создаем кортеж для Pickle
            pickle_entry = (file_path, is_directory, size, file_content)
            pickle_data.append(pickle_entry)

    # Сохраняем данные в формате JSON
    json_file_path = os.path.join(path_to_save, 'data.json')
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    # Сохраняем данные в формате CSV
    csv_file_path = os.path.join(path_to_save, 'data.csv')
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['file_path', 'is_directory', 'size_bytes', 'content'])
        csv_writer.writerows(csv_data)

    # Сохраняем данные в формате Pickle
    pickle_file_path = os.path.join(path_to_save, 'data.pkl')
    with open(pickle_file_path, 'wb') as pickle_file:
        pickle.dump(pickle_data, pickle_file)

    print("Данные успешно сохранены в JSON, CSV и Pickle файлы.")


traverse_and_save('../example_dir')
