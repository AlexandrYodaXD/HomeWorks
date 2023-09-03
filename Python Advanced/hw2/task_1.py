# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

data_num = 1234

hex_string = '0123456789abcdef'

temp = data_num
res_num = ''
while temp:
    residue = temp % 16
    # остаток от деления будет индексом в hex_string и указывать на соответствующий символ
    res_num = hex_string[residue] + res_num
    temp //= 16

print(hex(data_num))
print('0x' + res_num)
