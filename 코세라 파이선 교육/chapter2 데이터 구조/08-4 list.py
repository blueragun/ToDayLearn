fname = input("Enter file name: ")
fh = open(fname)
count = 0
lst = list()

for line in fh : 
    line = line.rstrip()
    if line == " " :
        continue
    if line.startswith('From ') : # 해당 파일에서 From 문구를 찾으면 아래 코드 실행    
      a = line.split()  # 해당 라인 분해
      a = a[1]  # A리스트의 2번째를 출력한다.
      print(a)
      count += 1
    else :
        continue

print("There were", count, "lines in the file with From as the first word")