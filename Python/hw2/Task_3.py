# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int
from random import randint

my_list = [randint(1, 99) for x in range(10)]
print(f'Изначальный список:  {my_list}')

# берется случайный индекс элемента из левой и правой части списка и меняются местами
# shuffle_coeff отвечает за колличество перемешиваний (по-идее хватает одного, случайность на то и случайность что элементы могут остаться нетронутыми, либо переместиться дважды (второй раз обратно), но всегда можно накинуть по-больше :) )
def ListShuffle(inc_list, shuffle_coeff=1):
    list_len = len(inc_list)
    half_list_len = list_len // 2
    
    for _ in range(list_len * shuffle_coeff):
        rnd_1 = randint(0, half_list_len - 1)
        rnd_2 = randint(half_list_len, list_len - 1)
        inc_list[rnd_1],inc_list[rnd_2] = inc_list[rnd_2],inc_list[rnd_1]

ListShuffle(my_list)
print(f'После перемешивания: {my_list}')