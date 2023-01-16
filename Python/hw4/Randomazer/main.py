import time
from math import log, sqrt

def rand_int():
    p_c = str(time.perf_counter()).replace('.', '')
    t_c = str(time.perf_counter()).replace('.', '')
    res1 = list(map(int, p_c[-4:]))
    res2 = list(map(int, t_c[-4:]))
    res = sum(res1+res2)
    # res = res1 + res2
    return res % 10

def rand_num(size):
    num = rand_int()
    while len(str(num)) < size:
        num *= 10
        num += rand_int()
    return num

def rand_min_max(max=100, min=0):
    min_len = len(str(min))
    max_len = len(str(max))
    my_list = list(range(min_len, max_len + 1))
    # print(my_list)
    # size = my_list[rand_int() % len(my_list)]
    min_c = 10**min_len - min
    max_c = max - (10 ** (max_len - 1) - 1)
    my_str =  '1'*min_c + '2'*(10**2-1 - 10**1) + '3'*max_c
    # my_str = '*' * (max - min)
    len_my_str = len(my_str)
    idx = rand_num(int(len(str(len_my_str)))) % len_my_str
    res_len = int(my_str[idx])
    res = rand_num(res_len)
    # res = abs((rand_num(max_len) - rand_num(min_len)))
    # print(idx, end=' ')
    '''
    size = int(my_str[idx])
    res = rand_num(size)
    '''
    while res < min or res > max:
        res = rand_num(res_len)
    # print(res)
    return(res)

# rand_min_max(634, 24)
# print(rand_num(4))
# print(rand_int(can_be_negative=True))

'''
min = 0
max = 101

min_c = 10**1 - min
max_c = max - (10**2-1)
my_str =  '1'*min_c + '2'*(10**2-1 - 10**1) + '3'*max_c
len_my_str = len(my_str)
idx = rand_num(len_my_str) % len_my_str
res = my_str[idx]
print(my_str)
res = ''
for _ in range(100):
    idx = rand_num(len_my_str) % len_my_str
    res = res + ' ' + my_str[idx]
    # print(f'idx: {idx}', end=', ')
print(res)
# 0 101
# 1 2 3
# [1, 1, 1, 2, 2, 2, 2, 2..., 3, 3]
# len(list)
# list[rnd % len]
'''




# lst_1 = [rand_min_max() for _ in range(20)]
# print(lst_1)


# exit()
count_dict = dict()
for _ in range(100000):
    # rnd = rand_int()
    rnd = rand_num(2)
    count_dict[rnd] = count_dict.setdefault(rnd, 0) + 1

for k, v in sorted(count_dict.items(), key=lambda x: x[1]):
    print(f'{k} - {v}')
    
print(time.perf_counter())
print(time.perf_counter_ns())