N = int(input())
    
result = []

for i in range(N) :
  data = input().split()
  for j in range(1, len(data)) :
    data[j] = int(data[j]) # string을 int로 변환
  
  if data[0] == 'insert' : 
      result.insert(data[1], data[2])
  elif data[0] == 'remove' :
      result.remove(data[1])
  elif  data[0] == 'append' :
      result.append(data[1])
  elif data[0] == 'print':
      print(result)
  elif data[0] == 'sort' :
      result.sort()
  elif data[0] == 'pop':
      result.pop()
  elif data[0] == 'reverse':
      result.reverse()
