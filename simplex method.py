M = [
    [1, 1, 2, 8],
    [-1, -2, 3, 1],
    [3, -7, 4, 10]
    ]


def show_matrix(M):
    print("\n")
    for i in M:
        for j in i:
            print(j, end="\t\t")
        print("\n")


show_matrix(M)
num_of_rows = len(M)
num_of_cols = len(M[0])

pivot_row = 0
pivot_col = 0


while pivot_row >= 0 and pivot_col >= 0:
    pivot_row = int(input('Enter row number: '))
    pivot_col = int(input('Enter column number: '))
    pivot_row -= 1
    pivot_col -= 1  #numbering starts from 0
    pivot_value = M[pivot_row][pivot_col]

    #when you want to divide a whole row you change columns
    for c in range(num_of_cols):
        M[pivot_row][c] = M[pivot_row][c] / pivot_value

    for r in range(num_of_rows):
        if r == pivot_row:
            continue
        make_zero = M[r][pivot_col]
        for c in range(num_of_cols):
            M[r][c] = M[r][c] - (make_zero * M[pivot_row][c])

    show_matrix(M)