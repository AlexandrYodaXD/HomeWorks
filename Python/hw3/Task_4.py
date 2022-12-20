# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = 46
# print(str(bin(num)[2:]))
res = []

while num:
    bit = num % 2
    res.append(bit)
    num //= 2

res.reverse()
print(*res, sep='')