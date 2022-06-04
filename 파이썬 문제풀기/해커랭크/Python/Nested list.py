data = []  # 데이터
sco = [] # 점수만
result = [] # 결과

for _ in range(int(input())):
    name = input()
    score = float(input())
    
    data.append([name, score])
    sco.append(score)
    
data.sort()    
sco = sorted(list(set(sco)))
print(sco)
second_score = sco[1]

for name, score in data :
  if score == second_score :
    print(name)