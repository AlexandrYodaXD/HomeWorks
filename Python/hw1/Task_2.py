# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = input('Введите X: ')
# y = input('Введите Y: ')
# z = input('Введите Z: ')

x, y, z = [input(f'Введите {i}: ') for i in ['x', 'y', 'z']]

res = not (x or y or z) == (not x and not y and not z)

print(res)