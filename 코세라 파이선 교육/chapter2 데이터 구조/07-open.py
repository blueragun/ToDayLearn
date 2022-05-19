# 파일 열기/읽기

# 해당 파일에서 cheese 단어를 출력한다.
xfile = open('mbox.txt')
for cheese in xfile :
  print(cheese)
  
# 해당파일의 라인 개수를 출력한다. 
fhand = open('mbox.txt')
count = 0
for line in fhand :
  count += 1
print("Line Count :", count)  

# 해당파일 길이가 몇인지 출력한디.
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

# 아래의 경우 From으로 시작하는 문장오른쪽 자동으로 newline이 입력되어
# 다음 line에서 print의 newline이 작동한다.
fhand = open('mbox-short.txt')
for line in fhand :
  if line.startswith('From:') :
    print(line)

# 아래의 경우 From 문당 오른쪽의 공백이 제거되면서 print의 newline이 작동해 
# 문장간 공백이 없어진다.
fhand = open('mbox-short.txt')
for line in fhand :
  line = line.rstrip()
  if line.startswith('From:') :
    print(line)
    
# 위 코드와 똑같다    
fhand = open('mbox-short.txt')
for line in fhand :
  line = line.rstrip()
  if not line.startswith('From:') :
    continue
  print(line)    
  
fname = input("Enter the file name: ")
try :
  fhand = open(fnamd)
except :
  print('File cannot be opened:', fname)
  quit()

count = 0
for line in fhand :
  if line.startswith('Subject: ') :
    count += 1
    
print('There were', count, 'Subject lines in', fname)      
      