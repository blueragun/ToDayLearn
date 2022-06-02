n = 5

count = 0

for i in range(n+1) : # 시간
  for j in range(60) : # 분
    for k in range(60) : # 초
      if '5' in str(i) + str(j) + str(k) :
        count += 1
        
print(count)        