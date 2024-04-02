from Matrix import Matrix


matrix = Matrix([
    [1,2,2],
    [4,5,5],
    [2,0.5,-3]
])

print(matrix.reduce().getArray())