# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
from os import path

# функция для преобразования вида степени (из 12 в '¹²', например)
def convert_degree(degree: int) -> str:
    dict_degrees = \
    {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
    result = ''
    while degree:
        result = dict_degrees[degree % 10] + result
        degree //= 10
    return result

# функция для создания строки уравнения
def create_an_equation(k: int):
    members_list = []
    for i in range(k, -1, -1):
        rnd_int = random.randint(-10, 10)
        # нахождение коэфициента
        if rnd_int == 0:
            continue
        else:
            coeff = str(rnd_int)
        # нахождение иксовой части со степенью
        x = f'X{convert_degree(i)}'
        # получение члена выражения конкатенацией и занесение в список
        members_list.append(coeff + x)
    # сборка строки уравнения
    equation = ' + '.join(members_list) + ' = 0'
    equation = equation.replace('1X', 'X')\
                        .replace(' + -', ' - ')\
                        .replace('X ', ' ')\
                        .replace('X¹ ', 'X ')
    return equation 

run_path = path.abspath(__file__) # получение абсолютного пути запущенного скрипта
dir_path = run_path[:run_path.rindex('\\') + 1] # вычленение папки с запущенным скриптом
# сделано это для того чтобы файлы создавались всегда в папке скрипта, независимо от того в какой директории в консоли мы сейчас работаем

with open(dir_path + 'output.txt', 'w', encoding='UTF-8')  as file:
    # k = int(input('Введите значение k >: '))
    k = random.randint(2, 13)
    file.write(create_an_equation(k))