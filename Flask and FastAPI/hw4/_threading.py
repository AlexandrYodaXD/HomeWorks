import threading
import time
from random import randint


# Функция заполнения списка случайными числами. Расширяет список _common_list.
def fill_random_list(_common_list, count):
    _common_list.extend([randint(0, 100) for _ in range(count)])


if __name__ == '__main__':
    start_time = time.time()  # Время начала работы программы

    common_list = []  # Список случайных чисел, который будет заполняться потоками
    threads = []  # Список потоков
    threads_count = 7  # Количество потоков
    target = 10_000_000  # Целевое количество чисел в списке

    # Запуск потоков, заполняющих список случайными числами
    for i in range(threads_count):
        t = threading.Thread(target=fill_random_list, args=(common_list, (target // threads_count),))
        t.start()
        threads.append(t)

    # Ожидание завершения всех потоков
    for t in threads:
        t.join()

    # Дозаполнение списка оставшимися элементами. Список может быть меньше target,
    # если target // threads_count * threads_count != target
    while len(common_list) < target:
        common_list.append(randint(0, 100))

    rnd_lst_time = time.time() - start_time  # Время формирования списка
    print(f'Формирование списка заняло: {rnd_lst_time:.3f} сек.')

    lst_sum = sum(common_list)  # Сумма элементов списка
    lst_sum_time = time.time() - start_time - rnd_lst_time  # Время подсчета общей суммы
    print(f'Подсчет общей суммы заняло: {lst_sum_time:.3f} сек.')

    total_time = time.time() - start_time  # Время работы программы
    print(f'Всего времени заняло: {total_time:.3f} сек.')
