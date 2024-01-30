import multiprocessing
import time
from random import randint


# Функция заполнения списка случайными числами. Расширяет список _common_list.
def fill_random_list(_common_list, count):
    _common_list.extend([randint(0, 100) for _ in range(count)])


if __name__ == '__main__':
    start_time = time.time()  # Время начала работы программы

    common_list = multiprocessing.Manager().list()  # Список, общий для всех процессов
    processes = []  # Список процессов
    processes_count = 7  # Количество процессов
    target = 10_000_000  # Целевое количество чисел в списке
    chunks_size = target // processes_count  # Размер части списка для каждого процесса

    # Запуск процессов, заполняющих список случайными числами
    for i in range(processes_count):
        p = multiprocessing.Process(target=fill_random_list, args=(common_list, chunks_size,))
        p.start()
        processes.append(p)

    # Ожидание завершения всех процессов
    for p in processes:
        p.join()

    # Дозаполнение списка оставшимися элементами. Список может быть меньше target,
    # если target // processes_count * processes_count != target
    while len(common_list) < target:
        common_list.append(randint(0, 100))

    rnd_lst_time = time.time() - start_time  # Время формирования списка
    print(f'Формирование списка заняло: {rnd_lst_time:.3f} сек.')

    pool = multiprocessing.Pool(processes=processes_count)  # Создание пула процессов
    sums = pool.map(sum, [common_list[i * chunks_size:(i + 1) * chunks_size] for i in range(processes_count)])  # Подсчет сумм
    pool.close()  # Закрытие пула
    pool.join()  # Ожидание завершения всех процессов
    total_sum = sum(sums)  # Общая сумма
    lst_sum_time = time.time() - start_time - rnd_lst_time  # Время подсчета общей суммы
    print(f'Подсчет общей суммы заняло: {lst_sum_time:.3f} сек.')

    total_time = time.time() - start_time  # Время работы программы
    print(f'Всего времени заняло: {total_time:.3f} сек.')
