# 파일 이름을 입력하라는 메시지를 표시한 다음 해당 파일을 열고 파일을 읽고 
# 다음 형식의 행을 찾는 프로그램을 작성하십시오.
# X-DSPAM-신뢰도: 0.8475
# 이 라인을 세고 각 라인에서 부동 소수점 값을 추출하고 해당 값의 평균을 계산하고 
# 아래와 같이 출력을 생성합니다. 솔루션에서 sum() 함수 또는 sum이라는 변수를 사용하지 마십시오.
fname = input("Enter file name: ")
fh = open(fname)

count = 0
scount = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue 
    else :    
        count += 1 
        spam = line[20:]
        scount = scount + float(spam)

spamavg = scount/count

print("Average spam confidence:", spamavg)