class Matrix:
    def __init__(self, mat):
        self.matrix = mat
        self.r = len(mat)
        self.c = len(mat[0])

    def display_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print()

    def __add__(self, other):
        if self.r == other.r and self.c == other.c:
            result = []
            for i in range(self.r):
                row = []
                for j in range(self.c):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    row.append(self.matrix[i][j])
                result.append(row)
            return self.display_matrix(result)

        else:
            return "The following matrices can't be added"


a = [[1, 2, 3], [2, 4, 5]]
b = [[2, 3, 5], [4, 4, 4]]
m1 = Matrix(a)
m2 = Matrix(b)

print(m1 + m2)




