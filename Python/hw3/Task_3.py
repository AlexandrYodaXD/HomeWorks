# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []
my_list_size = 10

for i in range(my_list_size):
    if random.choice([True, False]):
        random_num = random.uniform(0, 10)
        random_num = round(random_num, 2)
    else:
        random_num = random.randint(0, 10)
    my_list.append(random_num)

floats_list = []

for item in my_list:
    if isinstance(item, float):
        floats_list.append(item % 1)

res = round(max(floats_list) - min(floats_list), 2)
print(f'{my_list} => {res}')