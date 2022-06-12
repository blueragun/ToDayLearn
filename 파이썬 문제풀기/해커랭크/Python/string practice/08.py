def split_and_join(line):
  line = line.split()
  result = '-'.join(line)
  
  return result
  
line = "this is a string"   
result = split_and_join(line)
print(result)