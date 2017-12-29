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


exec(stdin.read())
