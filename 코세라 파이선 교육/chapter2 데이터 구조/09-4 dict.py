name = input("Enter file:")
if len(name) < 1:
		name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle :
		line = line.rstrip()   # 해당 파일 라인의 오른쪽 공백 제거
		if line == " " :
				continue
		if line.startswith("From ") : # 라인에서 From으로 시작하는 단어일 경우
			words = line.split() # 라인을 분해
			words = words[1] # 단어 2번째를 저장
			counts[words] = counts.get(words, 0) + 1 # 딕셔너리 키-값 형태로 저장한다.
		else : continue
				
bigcount = None
bigword = None

for word, count in counts.items() :
		if bigcount is None or count > bigcount : # bigcount가 None이거나 count가 bigcount보다 크면
				bigcount = count  # bigcount는 count 값이 저장된다. 즉 가장 큰값이 저장됨
				bigword = word

print(bigword, bigcount)