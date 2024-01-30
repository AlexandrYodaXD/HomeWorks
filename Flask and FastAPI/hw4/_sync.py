import time
from random import randint


def get_random_list(count):
    return [randint(0, 100) for _ in range(count)]


if __name__ == '__main__':
    start_time = time.time()

    rnd_lst = get_random_list(10_000_000)  # Список случайных чисел
    rnd_lst_time = time.time() - start_time  # Время формирования списка
    print(f'Формирование списка заняло: {rnd_lst_time:.3f} сек.')

    lst_sum = sum(rnd_lst)  # Сумма элементов списка
    lst_sum_time = time.time() - start_time - rnd_lst_time  # Время подсчета общей суммы
    print(f'Подсчет списка заняло: {lst_sum_time:.3f} сек.')

    total_time = time.time() - start_time
    print(f'Всего времени заняло: {total_time:.3f} сек.')
