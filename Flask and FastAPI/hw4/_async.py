import asyncio
import time
from random import randint


async def fill_random_list(_common_list, count):
    _common_list.extend([randint(0, 100) for _ in range(count)])


async def calculate_sum(chunk):
    return sum(chunk)


async def main():
    start_time = time.time()  # Время начала работы программы

    common_list = []  # Список случайных чисел, который будет заполняться потоками
    async_count = 7  # Количество асинхронных потоков
    target = 10_000_000  # Целевое количество чисел в списке
    chunks_size = target // async_count

    await asyncio.gather(*[fill_random_list(common_list, chunks_size) for _ in range(async_count)])  # Запуск
    # асинхронного заполнения списка

    chunks = [common_list[i * chunks_size:(i + 1) * chunks_size] for i in range(async_count)]  # Разбитие списка на
    # части

    rnd_lst_time = time.time() - start_time  # Время формирования списка
    print(f'Формирование списка заняло: {rnd_lst_time:.3f} сек.')

    sums = await asyncio.gather(*[calculate_sum(chunk) for chunk in chunks])  # Вычисление суммы в чанках
    total_sum = sum(sums)  # Вычисление суммы из чанков

    lst_sum_time = time.time() - start_time - rnd_lst_time  # Время подсчета общей суммы
    print(f'Подсчет списка заняло: {lst_sum_time:.3f} сек.')

    total_time = time.time() - start_time  # Время работы программы
    print(f'Всего времени заняло: {total_time:.3f} сек.')


asyncio.run(main())
