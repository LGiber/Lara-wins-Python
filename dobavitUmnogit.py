from sys import stdin
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(
            ['\t'.join(['%d' % i for i in row]
                       ) for row in self.matrix])

    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)

        return rows, cols

    def __add__(self, other):
        matrixnew = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summ = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summ)
                if len(numbers) == len(self.matrix):
                    matrixnew.append(numbers)
                    numbers = []
        return Matrix(matrixnew)

    def __mul__(self, alpha):
        matrixnew2 = []
        numbers2 = []
        if type(alpha) == int or type(alpha) == float:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    proizvedenie = self.matrix[i][j] * alpha
                    numbers2.append(proizvedenie)
                    if len(numbers2) == len(self.matrix):
                        matrixnew2.append(numbers2)
                        numbers2 = []
            return Matrix(matrixnew2)
        else:
            return Matrix(self.matrix)

    __rmul__ = __mul__


exec(stdin.read())
