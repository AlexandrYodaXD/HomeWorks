# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

def fill_backpack(stuff, max_load):
    sorted_stuff = sorted(stuff, key=lambda x: x[1], reverse=True)

    backpack = []
    cur_load = 0

    for item in sorted_stuff:
        if cur_load + item[1] <= max_load:
            backpack.append(item)
            cur_load += item[1]

    return backpack


max_load = 20
stuff = {
    "Тент": 5,
    "Спальный мешок": 3.1,
    "Газовая горелка": 2.3,
    "Еда": 4.5,
    "Вода": 3,
    "Кружка": 0.5,
    "Вилка": 0.1,
    "Нож": 0.25
}

backpack = fill_backpack(stuff.items(), max_load)
cur_load = sum([stuff[item[0]] for item in backpack])
print("Вещи в рюкзаке:")
for item in backpack:
    print(f'\t{item[0]}')
print(f'Рюкзак забит на {cur_load} из {max_load} кг')
