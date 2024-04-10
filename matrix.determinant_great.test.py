from Matrix import Matrix

matrix1 = Matrix([
    [1,-2,5],
    [2,3,-2],
    [3,1,2]
])

matrix2 = Matrix([
    [1,  -2,   0,   5],
    [2,   3,   1,  -2],
    [0,   2,  -1,   3],
    [3,   1,   0,   2]
])
print(str(matrix1.getDeterminant()))
print(str(matrix2.getDeterminant()))