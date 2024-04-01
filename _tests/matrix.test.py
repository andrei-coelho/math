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


# cria uma matrix
matrix4 = Matrix([
    [2,-3,4],
    [6,2,1],
    [1,1,2]
])

# pega sua matrix identidade
identity4 = matrix4.getIdentity()

# gera um objeto matrix com a matrix identidade
matrix5 = Matrix(identity4)

# multiplica a matrix identidade pela matrix
matrixres = matrix4.mult(matrix5)

# o resultado desta multiplicação é igual a matriz primaria
print(matrixres.iquals(matrix4))


