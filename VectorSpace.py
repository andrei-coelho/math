from Vector import Vector
from typing import Tuple, List


class VectorSpace:


    _vectors:List[Vector] = []
    _bigger_dimension:int = 0


    def __init__(self, vectors:Tuple[Tuple[int|float],...]):

        for vector in vectors:

            vec = Vector(vector=vector)
            if self._bigger_dimension < vec.getDimension():
                self._bigger_dimension = vec.getDimension()

            self._vectors.append(vec)


    def sum(self) -> Vector:
        
        count = len(self._vectors)

        if count == 0:
            raise Exception('there are no vectors to sum')
        
        finalVector = self._vectors[0].getArray(self._bigger_dimension,0)
        vtotal = len(self._vectors)
        
        x = 1
        while x < vtotal:
            nextVector = self._vectors[x].getArray(self._bigger_dimension,0)
            tempVectorArray = [] 
            i = 0
            while i < self._bigger_dimension:
                v = finalVector[i] + nextVector[i]
                tempVectorArray.append(v)
                i += 1
            finalVector = tempVectorArray
            x += 1

        return Vector(tuple(finalVector))


    def sub(self) -> Vector:

        count = len(self._vectors)

        if count == 0:
            raise Exception('there are no vectors to subtract')
        
        finalVector = self._vectors[0].getArray(self._bigger_dimension,0)
        vtotal = len(self._vectors)
        
        x = 1
        while x < vtotal:
            nextVector = self._vectors[x].getArray(self._bigger_dimension,0)
            tempVectorArray = [] 
            i = 0
            while i < self._bigger_dimension:
                v = finalVector[i] - nextVector[i]
                tempVectorArray.append(v)
                i += 1
            finalVector = tempVectorArray
            x += 1

        return Vector(tuple(finalVector)) 


    def mult(self):

        count = len(self._vectors)

        if count == 0:
            raise Exception('there are no vectors to multiply')
        
        finalVector = self._vectors[0].getArray(self._bigger_dimension,0)
        vtotal = len(self._vectors)
        
        # multiplicar
        x = 1
        while x < vtotal:
            nextVector = self._vectors[x].getArray(self._bigger_dimension,0)
            tempVectorArray = [] 
            i = 0
            while i < self._bigger_dimension:
                v = finalVector[i] * nextVector[i]
                tempVectorArray.append(v)
                i += 1
            finalVector = tempVectorArray
            x += 1

        # somar tudo

        return sum(finalVector)
        