#  Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов

data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9]

new_data = []
for item in data:
    if data.count(item) > 1 and item not in new_data:
        new_data.append(item)

print(data)
print(new_data)