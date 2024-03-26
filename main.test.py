from VectorSpace import VectorSpace

vs  = VectorSpace(((1.1,0,1),(2,3,1)))

vecSum = vs.sum()

print(vecSum.getArray())

print(vs.sub().getArray())

print(vs.mult())

print(vecSum.getMod())