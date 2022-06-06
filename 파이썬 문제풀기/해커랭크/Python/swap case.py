# 입력된 문장을 소문자는 대문자로, 대문자는 소문자로 변경해 출력

def swap_case(s) :
  data = str(s.swapcase())
  return data

s = 'HackerRank.com presents "Pythonist 2".'

result = swap_case(s)

print(result) 