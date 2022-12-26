from os import path
import generator
# функция для добавления данных в результирующий словарь, из которого в последствии сформируется результат (сумма многочленов)
def add_to_result(data: str):
    data = data.upper()\
        .replace(' ', '')\
        .replace('=0', '')\
        .replace('-', ' -')\
        .replace('+', ' ')\
        .replace('-X', '-1X')\
        .replace(' X', ' 1X')\
        .replace('X ', 'X1 ')
    # замена верхних степеней на числа
    for key, value in generator.dict_degrees.items():
        while value in data:
            data = data.replace(value, str(key))
    # разбор членов уравнения на составляющие
    for item in data.split():
        if 'X' in item:
            value, key = item.split('X')
            if not value:
                value = 1
            if not key:
                key = 1
        else:
            value, key = item, 0
        value, key = int(value), int(key)
        dict_result[key] = dict_result.get(key, 0) + value

# функция для сборки уравнения из словаря
def create_an_equation_from_dict(members_dict: dict):
    members_list = []
    for key, value in sorted(members_dict.items(), key=lambda x: x[0], reverse=True):
        if value == 0:
            continue
        else:
            coeff = str(value)
        x = f'X{generator.convert_degree(key)}'
        members_list.append(coeff + x)
    # сборка строки уравнения
    equation = ' + '.join(members_list) + ' = 0'
    equation = equation.replace('1X', 'X')\
                        .replace(' + -', ' - ')\
                        .replace('X ', ' ')\
                        .replace('X¹ ', 'X ')
    return equation 

dict_result = dict()

if __name__ == '__main__':
    run_path = path.abspath(__file__)
    dir_path = run_path[:run_path.rindex('\\') + 1]
    with open(dir_path + 'input_1.txt', 'r', encoding='UTF-8') as file:
        data = file.readline()
        print(f'Первое уравнение: {data}')
        add_to_result(data)

    with open(dir_path + 'input_2.txt', 'r', encoding='UTF-8') as file:
        data = file.readline()
        print(f'Второе уравнение: {data}')
        add_to_result(data)

result = create_an_equation_from_dict(dict_result)
print(f'Результат сложения: {result}')
