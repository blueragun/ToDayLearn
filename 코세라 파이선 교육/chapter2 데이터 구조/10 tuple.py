import re


d = { 'a' : 10, 'c' : 20, 'b' : 1, 'd' : 20}
d.items()
print(d.items())
# [('a', 10), ('c', 20), ('b', 1), ('d', 20)]
bsorted = sorted(d.items()) # d.items를 순서대로 정렬
print(bsorted)
# [('a', 10), ('b', 1), ('c', 20), ('d', 20)]


# ------------------------------------------
c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
for k, v in c.items() :
  tmp.append( (v, k))
  
print(tmp)
# [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)  
# [(22, 'c'), (10, 'a'), (1, 'b')]


# ---------------------------------
fhand = open('romeo.txt')
counts = dict()
for line in fhand :
  words = line.split()
  for word in words :
    counts[word] = counts.get(word, 0) + 1
    
lst = list()
for key, val in counts.items() :
  newtup = (val, key)
  lst.append(newtup)
  
lst = sorted(lst, reverse=True)

# sorted( [ (val, key) for key, val in counts.items() ] )
# 위 36 ~ 40 라인을 함축한 것

for val, key in lst[:10] :  
  print(val, key)    