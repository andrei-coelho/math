from typing import Tuple,List,TypeVar

MatrixType = TypeVar("MatrixType", bound="Matrix")

class Matrix:


    _total_columns:int = 0
    _total_rows:int = 0
    _matrix:Tuple[Tuple[int|float],...]|List[List[int|float]]


    def __init__(self, matrix:Tuple[Tuple[int|float],...]|List[List[int|float]]):
        
        self._total_rows = len(matrix)
        self._total_columns = len(matrix[0])

        for row in matrix:
            if len(row) != self._total_columns:
                raise Exception('the matrix does not have the same number of columns')
            
        self._matrix = matrix
            

    def getArray(self):
        return list(self._matrix)
    

    def getInfo(self):
        return (self._total_rows, self._total_columns)
    
    def transpose(self) -> MatrixType:
        
        c = 0
        newmatrix = []
        while c < self._total_columns: 
            newline = []
            for linha in self._matrix:
                newline.append(linha[c])
            c += 1
            newmatrix.append(newline)

        return Matrix(newmatrix)
    
    
    def mult(self, matrix:MatrixType) -> MatrixType:
        
        info = matrix.getInfo()

        if info[0] != self._total_columns:
            raise Exception("the other matrix does not have the same number of columns")

        m3 = matrix.transpose().getArray()
        res = []

        for linha in self._matrix:
            res_linha = []
            for l in m3:
                total = 0
                for i in range(self._total_columns):
                    total += linha[i] * l[i]
                res_linha.append(total)

            res.append(res_linha)

        return Matrix(res)
