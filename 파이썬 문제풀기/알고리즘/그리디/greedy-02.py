# 2. 큰수의 법칙
# 다양한 수로 이루어진 배열이 있을때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙. 단, 배역의 특정한 인덱스에 해당하는 수가
# 연속적으로 K번을 초과하여 더해질 수 없다. 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
# 첫줄에 N(2 <= N <= 1000), M(1 <= M <= 10000). K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 배열의 크기가 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질때 결과를 출력
# 입력예시
# 5 8 3
# 2 4 5 4 6

n, m, k = 5, 8, 3

data = [2, 4, 5, 4, 6]

data.sort()  # data에 들어있는 수를 정렬한다.
first_num = data[n-1]  # 가장 큰수
second_num = data[n-2] # 두번째 큰수

result = 0

while True : # '참'일 동안 진행
  for i in range(k) :
    result += first_num # K의 범위에서 가장 큰 수를 더한다.
    m -= 1  # 횟수를 차감한다.
    if m == 0 : # 횟수가 0이면 종료한다.
      break
  result += second_num
  m -= 1   # 횟수를 차감한다.
  if  m == 0 :  # 횟수가 0이면 종료한다.
    break

print(result)  


# 또 다른 방법

n, m, k = 5, 8, 3

data = [2, 4, 5, 4, 6]

data.sort()  # data에 들어있는 수를 정렬한다.
first_num = data[n-1]  # 가장 큰수
second_num = data[n-2] # 두번째 큰수

result = 0
# 가장 큰 숫자가 사용될 수 있는 수는 정해서 있다, 주어진 횟수에 따르면 큰수는 3번, 두번때 수는 1번 사용하면 4번씩 반복된다는 것을 알 수 있다.
count = int(m / (k+1)) * k 
count += m % (k+1) # count는 8 / 4 * 3  + (8 % 4) = 6번, 가장 큰수는 6번 사용된다

result += count * first_num 
result += (m - count) * second_num # 총 8회 중 2번만 두번째 큰수가 사용된다.

print(result)