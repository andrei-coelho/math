from typing import Tuple,List,TypeVar

MatrixType = TypeVar("MatrixType", bound="Matrix")

class Matrix:


    _total_columns:int = 0
    _total_rows:int = 0
    _matrix:Tuple[Tuple[int|float],...]|List[List[int|float]]

    _identity:list = []


    def __init__(self, matrix:Tuple[Tuple[int|float],...]|List[List[int|float]]):
        
        self._total_rows = len(matrix)
        self._total_columns = len(matrix[0])

        for row in matrix:
            if len(row) != self._total_columns:
                raise Exception('the matrix does not have the same number of columns')
            
        self._matrix = matrix
            

    def iquals(self, matrix:MatrixType) -> bool:

        infom = matrix.getInfo()
        if infom[0] != self._total_rows or infom[1] != self._total_columns:
            return False 
        
        lista = matrix.getArray()
        
        r = 0
        while r < self._total_rows:
            for c in range(self._total_columns):
                if lista[r][c] != self._matrix[r][c]: return False    
            r += 1

        return True
    

    def getArray(self):
        return list(self._matrix)
    

    def getIdentity(self) -> list:
        
        if len(self._identity) != 0:
            return self._identity

        total_col = self._total_rows
        res = []
        
        for i in range(total_col):
            linha = []
            for x in range(total_col):
                val = 1 if i == x  else 0
                linha.append(val)
            res.append(linha)
        
        self._identity = res
        return self._identity


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
    

    def getLastIndexRowNotNull(matrix_base):

        last_index = len(matrix_base)
        status = False

        while not status:
            last_index -= 1
            if last_index == 0: break
            for m in matrix_base[last_index]:
                if m != 0:
                    status = True 
                    break

        return last_index
    

    def getPivotXY(matrix_base,x=0,l=0):
        cont = True
        z = l
        max_rows = len(matrix_base)
        while cont:

            if x >= len(matrix_base[0]): break

            while z < max_rows:

                if matrix_base[z][x] != 0:
                    cont = False
                    break
                z = z + 1 if z + 1 < max_rows else 0

            if cont: x += 1

        return [x,z]


    def determinant2x2(matrix):
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) 
    
    def determinant3x3(matrix):
        diag1 = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] * matrix[2][1])
        diag2 = (matrix[2][0] * matrix[1][1] * matrix[0][2]) + (matrix[2][1] * matrix[1][2] * matrix[0][0]) + (matrix[1][0] * matrix[0][1] * matrix[2][2])
        return diag1 - diag2

    def getDeterminant(self) -> float:
        pass


    def inverse(self) -> MatrixType:

        matrix_final = self.getIdentity()
        matrix_base  = self._matrix

        x,line_pivot = Matrix.getPivotXY(matrix_base)

        line_pivot = 0

        # faz a pemutação
        matrix_perm = []
        matrix_perm.append(matrix_base[line_pivot])

        i = -1
        for m in matrix_base:
            i += 1
            if i == line_pivot: continue
            matrix_perm.append(m)
               
        # gauss
        while line_pivot < self._total_rows:

            x,y = Matrix.getPivotXY(matrix_perm,x,line_pivot)

            linha = matrix_perm[y]
            pivot = linha[x]
            num_mult = 1 / pivot if pivot != 0 else 0
    
            xl = 0
            xf = 0 
            
            # multiplica linha pelo pivo
            for n in linha:
                matrix_perm[line_pivot][xl] = n * num_mult
                xl += 1
            for e in matrix_final[line_pivot]:
                matrix_final[line_pivot][xf] = e * num_mult
                xf += 1
            # zera a coluna atual
            li = line_pivot + 1
            while li < self._total_rows:
                
                num_mult_iqual_0 = matrix_perm[li][x]
                linha_pivot_arr = matrix_perm[line_pivot]

                xo = 0
                xz = 0
                for v in linha_pivot_arr:
                    matrix_perm[li][xo] = matrix_perm[li][xo] - v * num_mult_iqual_0
                    xo += 1
                for f in matrix_final[line_pivot]:
                    matrix_final[li][xz] = matrix_final[li][xz] - f * num_mult_iqual_0
                    xz += 1
                li += 1
            x += 1
            line_pivot += 1            

        index_to_mult = Matrix.getLastIndexRowNotNull(matrix_perm)
        lc = self._total_columns - 1

        # jordan
        while True:

            if lc == 0 or index_to_mult == 0: break

            for xo in range(len(matrix_perm)):
                
                if xo == index_to_mult: break
                
                mult = matrix_perm[xo][lc]
                matrix_perm[xo][lc] = matrix_perm[xo][lc] - matrix_perm[index_to_mult][lc] * mult

                ind = 0
                for vmf in matrix_final[xo]:
                    matrix_final[xo][ind] = vmf - matrix_final[index_to_mult][ind] * mult
                    ind += 1

            lc -= 1
            index_to_mult -= 1
        
        return Matrix(matrix_final)
