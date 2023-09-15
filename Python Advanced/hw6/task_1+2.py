# Создайте модуль и напишите в нём функцию, которая получает на вход дату
# в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или ложь,
# если такая дата невозможна. Для простоты договоримся, что год может быть
# в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует
# Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

import argparse


def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999 and 1 <= month <= 12:
        if month == 2:
            if is_leap_year(year):
                return 1 <= day <= 29
            else:
                return 1 <= day <= 28
        elif month in [4, 6, 9, 11]:
            return 1 <= day <= 30
        else:
            return 1 <= day <= 31
    return False


def main():
    parser = argparse.ArgumentParser(description="Это программа для проверки даты.")
    parser.add_argument("date", type=str, help="Дата в формате DD.MM.YYYY")
    args = parser.parse_args()

    if is_valid_date(args.date):
        print(f"Дата {args.date} может существовать.")
    else:
        print(f"Дата {args.date} не может существовать.")


if __name__ == "__main__":
    main()

# python task_1+2.py 29.02.2020
