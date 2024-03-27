

class Vector:


    _vector:tuple
    _dimension:int


    def __init__(self, vector:tuple):
        self._dimension = len(vector)
        self._vector = vector 


    def getDimension(self):
        return self._dimension
    

    def getArray(self, dim:int=0, defValue=0) -> list:
        
        lista:list = []
        
        for v in self._vector:
            lista.append(v)

        if dim != 0 and self._dimension < dim:
            more = dim - self._dimension
            while more > 0:
                lista.append(defValue)
                more -= 1

        return lista
    

    def getMod(self):
        
        x = 0
        values:list = []

        # multplica os valores
        while x < self._dimension:
            values.append(self._vector[x] * self._vector[x])
            x += 1

        # soma os valores
        valorSomado = sum(values)

        estimativa_atual = 1.0

        # calcula raiz quadrada
        while True:
            
            valor_final = (estimativa_atual + valorSomado / estimativa_atual) / 2
            
            if abs(estimativa_atual - valor_final) < 0.0001:

                return valor_final
            
            estimativa_atual = valor_final