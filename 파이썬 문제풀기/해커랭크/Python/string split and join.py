# 입력되는 string을 '-'을 join해 출력

def split_and_join(line):
  data = line.split(' ')
  data = '-'.join(data)
  return data
  
  
line = 'this is a string'

result = split_and_join(line)

print(result)