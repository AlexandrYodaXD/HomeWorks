# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Получение валидного по условию задачи числа
def get_valid_number() -> int:
    while True:
        input_data = input('Введите число: ')
        try:
            num = int(input_data)
            if 0 < num < 100000:
                return num
            else:
                print('ОШИБКА: Введите положительное целое число до 100000!')
        except ValueError:
            print('ОШИБКА: Введено не число!')


# Проверка числа на простоту
def check_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                print(f'{num} не является простым числом!')
                return False
        else:
            print(f'{num} является простым числом!')
            return True
    else:
        print(f'{num} не является простым числом!')
        return False


# Вызов функций
n = get_valid_number()
check_prime(n)
