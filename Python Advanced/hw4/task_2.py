# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# Сначала решил однострочником
def my_func(**kwargs) -> dict:
    return {(k if getattr(k, '__hash__', None) else ', '.join(map(str, k))): v for v, k in kwargs.items()}


# Потом решил расписать на полнотелую функцию
def long_my_func(**kwargs) -> dict:
    my_dict = dict()
    for v, k in kwargs.items():
        if not getattr(k, '__hash__', None):
            k = ', '.join(map(str, k))
        my_dict[k] = v
    return my_dict


print(my_func(first='a', second=['Foo', 'Buzz'], third=3))
print(long_my_func(first='a', second=['Foo', 'Buzz'], third=3))
