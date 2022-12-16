# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Input a number: ')
result = 0

for item in number:
    if item.isdigit():
        result += int(item)

print(result)