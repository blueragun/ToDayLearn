import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

k = []

for i in range(n) :
    k.append(list(map(int, input().split())))
    
k = numpy.array(k)  
    
    
print(numpy.mean(k, axis=1))
print(numpy.var(k, axis=0))
print(numpy.std(k))