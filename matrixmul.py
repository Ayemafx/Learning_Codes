def multiply(matrix1, matrix2):
    row1 = len(matrix1)
    col1 = len(matrix1[0])
    row2 = len(matrix2)
    col2 = len(matrix2[0])
    result = []
    if col1 == row2:
        for i in range(row1):
            row = []
            for j in range(col2):
                ans = 0
                for k in range(row2):
                    c = (matrix1[i][k] * matrix2[k][j])
                    ans += c
                    # result[i][j] += (matrix1[i][k] * matrix2[k][j])
                row.append(ans)
            result.append(row)
        return result

    return result


matrix1 = []
matrix2 = []
num_of_row1 = int(input('Enter number of rows for matrix1'))
num_of_col1 = int(input('Enter number of columns for matrix1'))
num_of_row2 = int(input('Enter number of rows for matrix2'))
num_of_col2 = int(input('Enter number of columns for matrix2'))


def input_matrix(matrix, r, c):
    for i in range(r):
        a =[]
        for j in range(c):
            a.append(int(input('Enter element')))
        matrix.append(a)


def print_matrix(matrix, r, c):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print()


input_matrix(matrix1, num_of_row1, num_of_col1)
print_matrix(matrix1, num_of_row1, num_of_col1)
input_matrix(matrix2, num_of_row2, num_of_col2)
print_matrix(matrix2, num_of_row2, num_of_col2)
x = multiply(matrix1, matrix2)
print("Result:", x)