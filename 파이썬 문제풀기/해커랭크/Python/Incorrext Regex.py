# 정규표현에 대한 식을 사용할때는 내장 모듈인 re를 import 사용한다.
# 메타문자 < $()*+.?[]\^{}| >를 인식하려면 '\' 백스페이스를 앞에 붙여야
# 인식할 수 있다.

import re

n = int(input())

for i in range(n) :
  try :
    re.compile(input())
    print("True")
  except re.error :
    print("False")  
    
    

# match() : 문자열의 처음부터 시작해서 작성한 패턴이 일치하는지 확인
# search() : match()와 유사하지만 패턴이 처음부터 일치하지 않아도 괜찮음
# findal() : 문자열 안에 패턴에 맞는 케이스를 전부 찾아서 리스트로 반환함
# fullmatch() : 문자열에 시작과 끝이 정확하게 일치해야 반환
# split() : 문자열에서 패턴이 맞으면 이를 기점으로 리스트로 쪼개는 함수
# complie() : 정규식을 여러번 사용하려면 complie()을 사용함