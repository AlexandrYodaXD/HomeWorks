# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# Проверка на существование
def existence_check(side_a: int, side_b: int, side_c: int) -> bool:
    if any((
            side_a + side_b >= side_c,
            side_b + side_c >= side_a,
            side_c + side_a >= side_b
    )):
        print(f'Треугольник со сторонами {side_a}, {side_b} и {side_c} существует!')
        return True
    else:
        print(f'Треугольник со сторонами {side_a}, {side_b} и {side_c} не существует!')
        return False


# Проверка типа треугольника
def type_check(side_a: int, side_b: int, side_c: int) -> str:
    result = []
    if side_a == side_b == side_c:
        result.append('равносторонний')
    if any((
            side_a == side_b,
            side_b == side_c,
            side_c == side_a
    )):
        result.append('равнобедренный')
    if any((
            side_a ** 2 + side_b ** 2 == side_c ** 2,
            side_b ** 2 + side_c ** 2 == side_a ** 2,
            side_c ** 2 + side_a ** 2 == side_b ** 2
    )):
        result.append('прямоугольный')
    if side_a != side_b != side_c:
        result.append('разносторонний')

    if len(result) > 1:
        return f'А ещё он {", ".join(result[:-1])} и {result[-1]}!'
    elif len(result) == 1:
        return f'А ещё он {result[0]}!'


# Задание сторон
a: int = 3
b: int = 4
c: int = 5

# Вызов функции
if existence_check(a, b, c):
    print(type_check(a, b, c))
