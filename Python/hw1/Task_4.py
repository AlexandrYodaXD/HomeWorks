# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

try:
    quarter = input('Введите номер четверти на координатной плоскости: ')

    if quarter == 1:
        print('(x >= 0 and y > 0) or (x > 0 and y >= 0)')
    elif quarter == 2:
        print('(x <= 0 and y > 0) or (x < 0 and y >= 0)')
    elif quarter == 3:
        print('(x <= 0 and y < 0) or (x < 0 and y <= 0)')
    elif quarter == 4:
        print('(x >= 0 and y < 0) or (x > 0 and y <= 0)')
    else:
        print('Введен некорректный номер четверти.')
except:
    print('Введены некорректные данные.')