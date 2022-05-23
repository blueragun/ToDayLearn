# 24정수 3개 입력받아 짝수만 출력하기---------------------------------

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0 :
  print(a)

if b % 2 == 0 :
  print(a)

if c % 2 == 0 :
  print(a)
  
# 또는 ------------------

m = (a, b, c)

for i in m :
  if i % 2 == 0 :
    print(i)    
  

# 25 정수 3개를 입력받아 짝/홀 출력하기 ------------------------------
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

m = (a, b, c)
for i in m :
  if i % 2 == 0 :
    print("even")
  else :
    print("odd")  
    
# 26 정수 1개 입력받아 분류하기----------------------------------------

a = int(input())

if a > 0 :
  if a % 2 == 0 :
    print("C")
  else :
    print("D")
else :
  if a % 2 == 0 :
    print("A")
  else :
    print("B")     
    
# 27 점수 입력받아 평가 출력하기--------------------------------------

a = int(input())

if a >= 90 :
  print("A")
elif a >= 70 :
  print("B")
elif a >= 40 :
  print("C")
else :
  print("D")      
  
# 28 평가 입력받아 다르게 출력----------------------------------------
a = input()

if a == "A" :
  print("best!!!")
elif a == "B" :
  print("good!!")
elif a == "C" :
  print("run!")
elif a == "D" :
  print("slowly~")
else :
  print("what?")    
  
# 29 월 입력받아 계절 출력하기------------------------------------------

a = int(input())

if a // 3 == 3 :
  print("fall")
elif a // 3 == 1:
  print("spring")
elif a // 3 == 2 :
  print("summer")
else :
  print("winter")  
  
# 30 0이 될때 까지 무한 출력하기----------------------------------------

a = 1  # 초기 조건을 통과하기 위해 임시 지정

while a != 0 :
  a = int(input())
  if a != 0 :
    print(a)
    
# 31 정수 1개 입력받아 카운트 다운 출력하기-----------------------

a = int(input())

while a != 0 :
  print(a)
  a -= 1
  
# 32 정수 1개 입력받아 카운트다운 출력하기 2----------------------
a = int(input())

while a >= 1 :
  a -= 1
  print(a)
  
  
# 33 문자 1개 입력받아 알파벳 출력하기-----------------------------

a = ord(input())
b = ord('a')

while b <= a :
  print(chr(b), end=" ")
  b += 1  
  
# 34 정수 1개 입력받아 그 수까지 출력하기 --------------------------
a = int(input())
t = 0

while t <= a :
  print(t)
  t += 1  

# 35 정수 1개 입력받아 그 수까지 출력하기 2--------------------------
a = int(input())

for i in range(a+1) :
  print(i)
  
# 36 짝수의 합 구하기-----------------------------------------------
a = int(input())
s = 0

for i in range(a+1) :
  if i % 2 == 0 :
    s += i
print(s)    # 합을 구하기에 if문 밖에서 출력한다.

    
# 37 원하는 문자가 입력될때까지 반복 출력하기-------------------

while True :
  a = input()
  print(a)
  if a == 'q' :
    break
  
# 38 언제까지 더해야 할까---------------------------------------

a = int(input())
t = 0  # 이전 합
s = 0  # 최종 합

while s < a :
  t += 1
  s += t

print(t)  

# 39 주사위 2개 던지기 ---------------------------------------
a, b = input().split()
a = int(a)
b = int(b)

for i in range(1, a+1) :
  for j in range(1, b+1) :
    print(i, j)
    
# 40  369게임의 왕이 되자-------------------------------------

a = int(input())

for i in range(1, a+1) :
  if i % 10 == 3 :
    print("X", end = ' ')
  elif i % 10 == 6 : 
    print("X", end = ' ') 
  elif i % 10 == 9 : 
    print("X", end = ' ') 
  elif i % 33 == 0 :
    print("XX", end = ' ')
    
  else :
    print(i, end = ' ')   
    
    
# 41 빛 섞어 색 만들기---------------------------------------

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

for i in range(a) :
  for j in range(b) :
    for k in range(c) :
      print(i, j, k)
            
s = a * b * c            
print(s)    

# 42 거기까지! 이제그만~~~-------------------------------------
a = int(input())
t = 0
s = 0

while True :
  t += 1
  s += t
  if s >= a :
    break
  
print(s)  
        
    
          
      