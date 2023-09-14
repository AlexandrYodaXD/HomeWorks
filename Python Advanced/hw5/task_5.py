# Создайте функцию генератор чисел Фибоначчи(см.Википедию).

def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibo_gen()
for _ in range(10):
    print(next(fib_gen))
