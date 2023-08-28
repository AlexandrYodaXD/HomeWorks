# Пользователь загадывает число от 0 до 1000. Программе необходимо угадать число за 10 попыток.
from random import randint


# "глупая" версия с использованием метода "пальцем в небо"
def stupid_guess_the_number(lower_limit: int, upper_limit: int, attempt_number: int = 1):
    estimated_number = randint(lower_limit, upper_limit)
    print(f'Попытка #{attempt_number}\nПрограмма предполагает что ты загадал число {estimated_number}')
    # выход из рекурсии если угадал
    if estimated_number == user_number:
        print(f'Программа угадала твое число {user_number} с {attempt_number} попытки!')
        return
    # выход из рекурсии если не угадал за 10 попыток
    elif attempt_number > 9:
        print(f'Программа не смогла угадать твое число {user_number} за {attempt_number} попыток!')
        return
    # иначе углубляемся в рекурсию
    else:
        if estimated_number > user_number:
            print(f'Ты даешь подсказку что загаданное тобой число меньше {estimated_number}')
            stupid_guess_the_number(lower_limit, estimated_number, attempt_number + 1)
        else:
            print(f'Ты даешь подсказку что загаданное тобой число больше {estimated_number}')
            stupid_guess_the_number(estimated_number, upper_limit, attempt_number + 1)


# "Умная" версия с использованием метода половинного деления.
# Не уверен до конца, что написал оптимально
def smart_guess_the_number(lower_limit: int, upper_limit: int, attempt_number: int = 1):
    estimated_number = (upper_limit - lower_limit) // 2 + lower_limit
    print(f'Попытка #{attempt_number}\nПрограмма предполагает что ты загадал число {estimated_number}')

    # для отладки
    # print(f'{lower_limit} - {estimated_number} - {upper_limit}')

    # выход из рекурсии если угадал
    if estimated_number == user_number:
        print(f'Программа угадала твое число {user_number} с {attempt_number} попытки!')
        return
    # выход из рекурсии если не угадал за 10 попыток
    elif attempt_number > 9:
        print(f'Программа не смогла угадать твое число {user_number} за {attempt_number} попыток!')
        return
    # иначе углубляемся в рекурсию
    else:
        if estimated_number > user_number:
            print(f'Ты даешь подсказку что загаданное тобой число меньше {estimated_number}')
            smart_guess_the_number(lower_limit, estimated_number, attempt_number + 1)
        else:
            print(f'Ты даешь подсказку что загаданное тобой число больше {estimated_number}')
            smart_guess_the_number(estimated_number, upper_limit, attempt_number + 1)


# вызов функций
user_number = 8
# stupid_guess_the_number(0, 1000)
smart_guess_the_number(0, 1000)
