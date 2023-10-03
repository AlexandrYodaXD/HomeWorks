# Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:
# Инициализация матрицы. Конструктор класса должен принимать количество строк rows и количество столбцов cols и
# создавать матрицу с нулевыми значениями.
# Операция сложения матриц. Реализуйте метод __add__, который позволяет складывать две матрицы одинаковых размеров.
# Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две матрицы с согласованными
# размерами (количество столбцов первой матрицы должно быть равно количеству строк второй матрицы).
# Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.
# Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает строковое представление матрицы,
# где элементы строки разделены пробелами, а строки сами разделены символами новой строки.
# Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__, который возвращает
# строку, которую можно использовать для создания нового объекта класса Matrix.
import copy


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __add__(self, other):
        if isinstance(other, Matrix):
            if all((self.rows == other.rows,
                    self.cols == other.cols)):
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = copy.deepcopy(self.data)
                for i in range(self.rows):
                    for j in range(self.cols):
                        new_matrix.data[i][j] += other.data[i][j]
                return new_matrix
            else:
                raise AttributeError('Матрицы должны быть одинаковой размерности')
        else:
            raise AttributeError('Складывать матрицу можно только с матрицей')

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                new_matrix = Matrix(self.rows, other.cols)
                for i in range(new_matrix.rows):
                    for j in range(self.cols):
                        for k in range(other.rows):
                            new_matrix.data[i][j] += self.data[i][k] * other.data[k][j]

                return new_matrix
            else:
                raise AttributeError('Матрицы должны быть согласованными')

        elif isinstance(other, int):
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = copy.deepcopy(self.data)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.data[i][j] *= other

            return new_matrix

        else:
            raise ValueError('Умножать матрицу можно только на другую матрицу, либо целое число')

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if all((self.rows == other.cols,
                    self.cols == other.rows)):
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.data[i][j] != other.data[i][j]:
                            return False
                    else:
                        return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in row]) for
                          row in self.data])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rows},{self.cols})"


if __name__ == '__main__':
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)

    print(matrix2)

    # Сравниваем матрицы
    print(matrix1 == matrix2)

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)
