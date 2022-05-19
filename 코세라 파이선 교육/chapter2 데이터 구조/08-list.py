# list를 print 하면 list 형태로 출력
print([1, 2, 3])
# => [1, 2, 3]

# append, count, extend, index, insert, pop, remove, reverse, sort 등 메소드가 있음

a = list()
a.append(1)
a.append(2)
print(a)
# => [1, 2]

total = 0
count = 0

#-----------------------------------------------------------
while True :
  inp = input('Enter a number: ')
  if inp == 'done' : 
    break
  value = float(inp)
  total += value
  count += 1

average = total / count
print('Average:', average)  

# 아래 코드는 위와 동일함 다만 수백만 숫자에 있어 용량은 위가 작아
# 계산이 용이한 점은 있다

numlist = list()
while True :
  inp = input('Enter a number: ')
  if inp == 'done' : 
    break
  value = float(inp)
  numlist.append(value)
  
average = sum(numlist) / len(numlist)  
print('Average:', average) 

# ----------------------------------------------------------
# split 메서드
abc = 'with three words'
s = a.split()
print(s)

# => ['with', 'three', 'words]

abc = 'with;three;words'
s = a.split(';')
print(s)

# => ['with', 'three', 'words]