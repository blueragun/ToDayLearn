name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle : 
    if line.startswith("From ") :
        words = line.split()  # 라인 분해
        words = words[5].split(':') # 분해된 라인의 6번째를 ':'로 재분해
        counts[words[0]] = counts.get(words[0], 0) + 1 # 분해된 string의 1번째 단어 카운트
            
lst = list()
for key, val in counts.items() :  # count.items를 key, val로 반복
    newtup = (key, val)
    lst.append(newtup)
    
lst = sorted(lst)  # 순서대로 정렬

for key, val in lst :
	print(key, val)