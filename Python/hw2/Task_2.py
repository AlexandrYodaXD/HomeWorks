# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input('Input a number: '))
res_list = []

for i in range(1, number + 1):
    res_list.append(round((1 + 1 / i) ** i, 2))

print(res_list)
print(f'Сумма {sum(res_list)}')