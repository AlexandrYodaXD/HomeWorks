# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

try:
    inp_num = int(input('Введите номер дня недели: '))
    
    if inp_num in range(6, 8):
        print('Выходной день.')
    elif inp_num in range(1, 6):
        print('Будний день.')
    else:
        print('Введен некорректный номер дня недели.')
except:
    print('Введены некорректные данные.')
