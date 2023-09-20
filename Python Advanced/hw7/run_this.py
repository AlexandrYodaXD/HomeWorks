import file_worker

if __name__ == '__main__':
    # Генерируем файлы
    file_worker.generate_files('.mp3', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.oog', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.mp4', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.wav', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.jpg', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.gif', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.doc', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.pdf', dir='./Files', min_size=5, max_size=10, file_count=11)
    file_worker.generate_files('.zip', dir='./Files', min_size=5, max_size=10, file_count=11)

    # Раскидываем файлы по папкам
    file_worker.sort_files_by_folders('./Files')

    # Групповое переименование файлов
    file_worker.group_renaming('./Files/', '.zip', 'renamed',
                   '.rar', 2, (1, 3))