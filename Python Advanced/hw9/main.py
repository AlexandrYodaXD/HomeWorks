# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import funcs_pack

CSV_FILENAME = 'random_numbers.csv'
JSON_FILENAME = 'results.json'


@funcs_pack.save_to_json_decorator(JSON_FILENAME)
@funcs_pack.csv_input_decorator(CSV_FILENAME)
def demo_func(a, b, c):
    """
    Функция для демонстрации работы декораторов
    Для наглядности решил сделать отдельную функцию и задекорировать её ¯\_(ツ)_/¯
    """
    return funcs_pack.quadratic_roots(a, b, c)


if __name__ == '__main__':
    funcs_pack.generate_csv(CSV_FILENAME, 100)
    demo_func()
