from Matrix import Matrix


matrix1 = Matrix([
    [1,0],
    [0,1]
])

matrix2 = Matrix([
    [2,-3,4],
    [6,2,1]
])


matrix3 = matrix1.mult(matrix2)

print(matrix3.getArray())