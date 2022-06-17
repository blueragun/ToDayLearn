# textwrap 모듈을 이용한 text 자르기
# textwrap.fill(test, width) 함수 이용



import textwrap

def wrap(string, max_width) :
  return textwrap.fill(string, width = max_width)
  
  
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)