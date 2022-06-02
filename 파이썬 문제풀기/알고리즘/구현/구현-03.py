n = input()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1 # 열로 주어진 알파벳을 숫자로 바꾼다,  a == 1

move_type = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


result = 0

for plan in move_type :
  print(plan[1])
  row_n = row + plan[0]
  column_n = column + plan[1]
  
  if row_n >= 1 and column_n <= 8 and row_n <= 8 and column_n >=0 :
    result += 1
    
print(result)