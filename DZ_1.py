a = [[3, 2, 5], [1, 1, 1]]
b = [[6, 9, 1], [2, 5, 9]]
c = [[6, 4, 1], [1, 3, 2]]

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
            return '\n'.join(map(str, self.matrix))


    def __add__(self, other):
        q=[]
        for i in range(len(self.matrix)):
            q.append([])
            for j in range(len(self.matrix[0])):
                q[i].append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(q)


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
matrix_3 = Matrix(c)
print(f"Матрица №1\n{matrix_1}\n")
print(f"Матрица №2\n{matrix_2}\n")
print(f"Матрица №3\n{matrix_3}\n")
print(f"Сложение предыдущих матриц\n{matrix_1 + matrix_2 + matrix_3}")
