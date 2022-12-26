from os import path
from generator import *

def add_to_res(data: str):
    data = data.upper()\
        .replace(' ', '')\
        .replace('=0', '')\
        .replace('-', ' -')\
        .replace('+', ' ')\
        .replace('-X', '-1X')\
        .replace(' X', ' 1X')\
        .replace('X ', 'X1 ')
    
    # замена верхних степеней на числа
    for key, value in degree_int_to_upper_str.items():
        while value in data:
            data = data.replace(value, str(key))
    
    for item in data.split():
        if 'X' in item:
            value, key = item.split('X')
        else:
            value, key = item, 0
        value, key = int(value), int(key)
        dict_result.setdefault(key, 0)
        dict_result[key] += value

def convert_degree(degree: int):
    result = ''
    while degree:
        result = degree_int_to_upper_str[degree % 10] + result
        degree //= 10
    return result

def create_an_equation_from_dict(members_dict: dict):
    members_list = []
    for key in sorted(members_dict.keys(), reverse=True):
        if dict_result[key] == 0:
            continue
        elif dict_result[key] == 1:
            left_member = ''
        else:
            left_member = dict_result[key]
        
        if key == 0:
            right_member = ''
        elif key == 1:
            right_member = 'X'
        else:
            right_member = f'X{convert_degree(key)}'
        
        member = str(left_member) + right_member
        if member != '':
            members_list.append(member)

    return ' + '.join(members_list) + ' = 0'

dict_result = dict()

run_path = path.abspath(__file__)
dir_path = run_path[:run_path.rindex('\\') + 1]

with open(dir_path + 'input_1.txt', 'r', encoding='UTF-8') as file:
    data = file.readline()
    print(f'Первое уравнение: {data}')
    add_to_res(data)

with open(dir_path + 'input_2.txt', 'r', encoding='UTF-8') as file:
    data = file.readline()
    print(f'Второе уравнение: {data}')
    add_to_res(data)

res = create_an_equation_from_dict(dict_result)
print(f'Результат сложения: {res}')