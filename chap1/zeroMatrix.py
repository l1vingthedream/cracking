def zero_matrix(arr: list[list[int]], rows: int, cols: int) -> None:
    nullCols: list[int] = []
    nullRows: list[int] = []
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                nullRows.append(i)
                nullCols.append(j)

    for x in range(0, rows):
        for y in range(0, cols):
            if x in nullRows or y in nullCols:
                arr[x][y] = 0


rows, cols = (5, 5)
matrix = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(i*4+j+1)
    matrix.append(col)
matrix[2][3] = 0
print("original: ", matrix)
zero_matrix(matrix, rows, cols)
print("zeroed out: ", matrix)
