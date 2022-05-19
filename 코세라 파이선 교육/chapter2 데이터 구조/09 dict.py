# 딕셔너리는 순서가 없다. unpredictable
# 키-값으로 이루어져 있음 
# { '키' : 값 } = { 'A' = 1 }

jjj = { 'chuck' : 1, 'fred' : 2, 'jan' : 3}
print(list(jjj))
# ['chuck', 'fred', 'jan']
print(jjj.keys())
# ['chuck', 'fred', 'jan']
print(jjj.values())
# [1, 2, 3]
print(jjj.items())
# [('chuck', 1), ('fred', 2), ('jan', 3)]

for aaa, bbb in jjj.items() :
  print(aaa, bbb)
  
# aaa = key값, bbb = value값 출력


counts = dict()
for line in handle :
  words = line.split()
  for word in words :
    counts[word] = counts.get(word, 0) + 1
    
bigcount = None
bigword = None
for word, count in counts.items() :
  if bigcount is None or count > bigcount :
    bigword = word
    bigcount = count
    
print(bigword, bigcount)
        