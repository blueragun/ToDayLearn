# 1 문자를 입력받아 출력하기
a = input("c")
print(a)

# 2 정수를 입력받아 int로 변환한 후 출력
a = int(input())
print(a)


# 3 실수를 입력받아 변환하여 출력하기
a = float(input())
print(a)

# 4 정수 2개를 입력받아 그대로 출력하기
a = int(input())
b = int(input())

print(a)
print(b)

# 5 문자 2개 입력받아 순서 바꿔 출력하기

a = input()
b = input()

print(b)
print(a)

# 6 실수 1개 입력받아 3번 출력하기

a = float(input())
print(a)
print(a)
print(a)

# 7 정수 2개를 입력받아 분리한 후 그대로 출력

a, b = input().split()
print(int(a))
print(int(b))

# 8 문자 2개를 입력받아 분리한 후 순서 바꿔 출력하기

a, b = input().split()
print(b)
print(a)

# 9 문자 1개를 입력받아 공백을 두고 3번 출력하기

a = input()
print(a, a, a)

# 10 시간 입력받아 그대로 출력하기

a, b = input().split(':')
print(a, b, sep=':')

# 11 연.월.일 입력받아 순서 바꿔 출력하기 2020.3.4 -> 4-3-2020

y, m, d = input().split('.')
print(d, m, y, sep='-')

# 12 주민번호 입력받아 형태 바꿔 출력하기 00000-00000 -> 00000000

a, b = input().split('-')
print(a, b, sep='')

# 13 단어 1개 입력받아 나누어 출력하기

a = input()

for i in a :
  print(i)
  
  
# 14 연월일 입력받아 나누어 출력하기

a = input()

print(a[:2], a[2:4], a[4:])

# 15 시분초 입력받아 분만 출력하기

a, b, c = input().split(':')
print(b)
  
# 16 단어 2개 입력받아 이어붙이기

a, b = input().split()
print(a+b)  

# 17 정수 2개 입력받아 합 계산하기

a, b = input().split()

print(int(a)+int(b))

# 18 실수 2개 입력받아 합 계산하기

a = float(input())
b = float(input())
print(a+b)

# 19 10진 정수 입력받아 16진수 출력하기  

a = int(input())
print('%x' %a)

# 20 10진 정수 입력받아 16진수 출력하기2
a = int(input())
print('%X' %a)

# 21 16진수 입력받아 8진수 출력하기
a = input()
a = int(a, 16)
print('%o' %a)

# 22 영문자 1개 입력받아 10진수로 변환하기

a = ord(input())
print(a)

# 23 정수 입력받아 유니코드 문자로 변환하기
a = int(input())
print(chr(a))

    
  