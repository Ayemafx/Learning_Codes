def show_matrix():
    print("\n")
    for i in matrix:
        for j in i:
            print(j, end="\t\t")
        print("\n")


matrix = [
    [1, 1, 2, 9],
    [2, 4, -3, 1],
    [3, 6, -5, 0]
    ]

show_matrix()
num_of_row = len(matrix)
num_of_cols = len(matrix[0])
pivot_row = int(input('Enter pivot row: '))
pivot_col = int(input('Enter pivot column: '))
pivot_row -= 1
pivot_col -= 1


def get_one():
    for i in range(num_of_cols):
        if matrix[pivot_row][pivot_col] != 1:
            pivot_value = matrix[pivot_row][pivot_col]

            for j in range(num_of_cols): #divides whole row with pivot value
                matrix[pivot_row][j] = matrix[pivot_row][j]/pivot_value


def get_zero():
    for i in range(num_of_cols):
        if matrix[i][pivot_col] != 0:
            make_zero = matrix[i][pivot_col]

            for j in range(num_of_cols):
                matrix[pivot_row][j] = matrix[pivot_row][j] - (make_zero * matrix[pivot_col][j])


def get_zeroo():
    for r in range(num_of_row):
            if r == pivot_row:
                continue
            make_zero = matrix[r][pivot_col]
            for c in range(num_of_cols):
                matrix[r][c] = matrix[r][c] - (make_zero * matrix[pivot_row][c])


get_one()
get_zeroo()
show_matrix()