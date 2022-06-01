# ATM 돈 인출 시간
# 입력
# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

n = 5 # int(input())

t = [3, 1, 4, 3, 2] 
# t = list(map(int, input().split()))

t.sort()

k = 0

result = 0 # 결과 값

for i in t :
  k += i
  result += k
  
print(result)