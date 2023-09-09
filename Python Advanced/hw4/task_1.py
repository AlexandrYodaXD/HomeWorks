# Напишите функцию для транспонирования матрицы

def print_matrix(matrix: list[list]):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
    print()


def matrix_transpose(matrix: list[list]):
    row_size = len(matrix)
    col_size = len(matrix[0])
    matrix_size = max(row_size, col_size)

    while len(matrix) < matrix_size:
        matrix.append([None for _ in range(matrix_size)])

    if col_size < matrix_size:
        for i in range(matrix_size):
            matrix[i].append(None)

    for i in range(matrix_size):
        for j in range(i, matrix_size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_size):
        if set(matrix[i]) is {None}:
            matrix.remove(i)
        else:
            while None in matrix[i]:
                matrix[i].remove(None)


matrix1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]

print('Пример с матрицей 3х2', end='\n')
print_matrix(matrix2)
matrix_transpose(matrix2)
print_matrix(matrix2)

print('\nПример с матрицей 2х3', end='\n')
print_matrix(matrix1)
matrix_transpose(matrix1)
print_matrix(matrix1)
