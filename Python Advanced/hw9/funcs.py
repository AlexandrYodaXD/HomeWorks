import csv
import functools
import json
import math
import random


def quadratic_roots(a: float, b: float, c: float) -> tuple[float]:
    """
    Функция для нахождения корней квадратного уравнения
    :param a: Первый коэффициент квадратного уравнения
    :param b: Второй коэффициент квадратного уравнения
    :param c: Третий коэффициент квадратного уравнения
    :return: Кортеж корней квадратных уравнений, если уравнение имеет решение, либо None
    """

    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        return tuple(x1)
    else:
        return None


def generate_csv(filename, num_rows):
    """
    Функция для генерации CSV файла
    Создается CSV файл, в него генерируется num_rows строк по три целых числа от 100 до 1000
    :param filename: Имя для CSV файла
    :param num_rows: Количество строк для генерации
    """
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(['a', 'b', 'c'])
        for _ in range(num_rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            csv_writer.writerow(row)


def csv_input_decorator(csv_filename):
    """
    Декоратор для выполнения функции с каждой тройкой чисел из CSV файла
    :param csv_filename: Путь до CSV файла с коэффициентами квадратного уравнения
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            with open(csv_filename, 'r') as csvfile:
                csv_reader = csv.DictReader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
                for row in csv_reader:
                    a, b, c = row['a'], row['b'], row['c']
                    roots = func(a, b, c)
                    result_entry = {
                        'a': a,
                        'b': b,
                        'c': c,
                        'roots': roots
                    }
                    results.append(result_entry)
            return results

        return wrapper

    return decorator


def save_to_json_decorator(json_filename):
    """
    Декоратор для сохранения параметров и результатов в JSON файл
    :param json_filename:
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(json_filename, 'w') as jsonfile:
                json.dump(result, jsonfile, indent=4)
            return result

        return wrapper

    return decorator
