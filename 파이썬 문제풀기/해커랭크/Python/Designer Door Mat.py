# n, m = map(int, input().split())
n = 9
m = 27

a = ".|."
b = 'WELCOME'

for i in range(1, n, 2) :
  print((a * i).center(m, '-'))

print(b.center(m, '-'))

for i in range(n-2, -1, -2) :
  print((a * i).center(m, '-'))

