import random


class Matrix():
    def __init__(self, m_data):
        self.__matrix = m_data

    def __add__(self, other):
        result = []
        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


m1 = [[random.randrange(0, 9) for i in range(5)] for j in range(4)]
m2 = [[random.randrange(0, 9) for i in range(5)] for j in range(4)]

matrix1 = Matrix(m1)
matrix2 = Matrix(m2)
print(matrix1, '\n=====================')
print(matrix2, '\n=====================')
print(matrix1 + matrix2)
