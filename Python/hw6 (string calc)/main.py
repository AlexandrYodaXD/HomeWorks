data_1 = '(-1 + (2 * 3)) / (-4 - 5 * (6 - 7))' # 5
data_2 = '((-12 / (2 + 4)) * (2 - (6 / 2) + 5))'  # -8
data_3 = '(25 - 4) / 7 + 5 * (12 - 3)'  # 48
data_4 = '14 / 2 * (17-8) + 3' # 66
data_5 = '1-2*3'
operations_dict = {
    '+': lambda x, y: int(x) + int(y),
    '-': lambda x, y: int(x) - int(y),
    '/': lambda x, y: int(x) / int(y),
    '*': lambda x, y: int(x) * int(y),
}


def parsing(data: str) -> list:
    print(f'Входящие данные: {data}')
    data = data.replace(' ', '') \
        .replace('(', ' ( ') \
        .replace(')', ' ) ')
    data = ' ' + data
    # print('1-я замена.', data)
    data = data.replace(' -', '#') \
        .replace('+', ' + ') \
        .replace('-', ' + -') \
        .replace('#', ' -') \
        .replace('/', ' / ') \
        .replace('*', ' * ') \
        .replace(' + - ( ', ' - ( ') \
        .replace('  ', ' ')
    # print('2-я замена.', data)
    xdata = data
    data = data.split()
    # print(f'Предобработка: {data}')
    for i in range(len(data)):
        try:
            data[i] = int(data[i])
        except ValueError:
            continue
    # print(f'После преобразования к int: {data}')
    while ')' in data:
        end = data.index(')')
        start = len(data[:end]) - data[:end][::-1].index('(') - 1
        data = data[:start] + [data[start + 1:end]] + data[end + 1:]
    print(f'После разбиения: {data}')
    return data


def calc(data: list):
    print('Calc: вх. данные: ', data)
    for operation in '/*-+':
        while operation in data:
            idx = data.index(operation)
            left = data[idx - 1]
            right = data[idx + 1]
            res = operations_dict[operation](left, right)
            print(f'Результат операции {left} {operation} {right} = {res}')  # для отладки
            print('Новый список:', data[:idx - 1] + [res] + data[idx + 2:])  # для отладки
            data = data[:idx - 1] + [res] + data[idx + 2:]
    return data[0]


def rec_sum(data: list):
    print('Rec_sum: вх. данные: ', data)
    for i in range(len(data)):
        if isinstance(data[i], list):
            print('Найден вложенный список, вызываю рекурсию', data[i])
            data[i] = rec_sum(data[i])
    return calc(data)


parsed_data = parsing(data_4)
print('res', rec_sum(parsed_data))
