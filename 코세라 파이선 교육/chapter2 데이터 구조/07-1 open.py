# 파일 이름을 입력하라는 메시지를 표시한 다음 해당 파일을 열고 파일을 읽고 
# 파일 내용을 대문자로 인쇄하는 프로그램을 작성하십시오. 
# word.txt 파일을 사용하여 아래 출력을 생성합니다.


fname = input("Enter file name: ")
fh = open(fname)

for line in fh :
	line = line.rstrip()
	line = line.upper()

	print(line)

