import copy


class Matrix:
    def __init__(self, matrix: list):
        self.matrix: list = copy.deepcopy(matrix)
        if not self._check_exists():
            raise AttributeError('Неверный формат переданной матрицы')

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for
                          row in self.matrix])

    def _check_exists(self):
        check_1 = min(map(len, self.matrix)) == max(map(len, self.matrix))
        check_2 = None
        for row in self.matrix:
            if not all((isinstance(num, int) for num in row)):
                check_2 = False
                break
            else:
                check_2 = True
        return all((check_1, check_2))

    def _consistency_check(self, other):
        return len(self.matrix[0]) == len(other.matrix)

    def __mul__(self, other):
        if isinstance(other, Matrix) and self._consistency_check(other):
            new_matrix = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    for k in range(len(other.matrix)):
                        new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

            return Matrix(new_matrix)

        elif isinstance(other, int):
            new_matrix = copy.deepcopy(self.matrix)
            for i in range(len(self.matrix)):
                for k in range(len(self.matrix[0])):
                    new_matrix[i][k] *= other

            return Matrix(new_matrix)

        else:
            raise ValueError('Умножать матрицу можно только на другую матрицу, либо целое число')
