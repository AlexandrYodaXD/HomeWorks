import time
import math
import random

def get_c():
    a = time.perf_counter()
    b = float(str(a)[::-1])
    c = math.log(a) / math.sqrt(b)
    return c

count_dict = dict()

for _ in range(10000):
    last_digit = str(get_c())[-1]
    # last_digit = int(last_digit)
    count_dict[last_digit] = count_dict.setdefault(last_digit, 0) + 1

for k, v in sorted(count_dict.items(), key=lambda x: x[1]):
    print(f'{k} - {v}')