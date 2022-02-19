def swap4(
        _arr: list[list[int]],
        i: int,
        j: int,
        rows: int,
        cols: int) -> None:
    backup                   = _arr[i][j] 
    _arr[i][j]               = _arr[rows-j-1][i]        #top
    _arr[rows-j-1][i]        = _arr[rows-i-1][rows-j-1] #left
    _arr[rows-i-1][rows-j-1] = _arr[j][rows-i-1]        #bott
    _arr[j][rows-i-1]        = backup                   # right

def rotateMatrix(_arr: list[list[int]]) -> None:
    _row = int(len(_arr[0]) / 2)
    _col = int(len(_arr[0]) / 2)
    for i in range(0,_row):
        for j in range(0,_col):
            swap4(_arr,i,j,len(_arr),len(_arr[0]))

rows, cols = (4, 4)
matrix=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(i*4+j+1)
    matrix.append(col)
print("original: ", matrix)
rotateMatrix(matrix)
print("rotated: ", matrix)