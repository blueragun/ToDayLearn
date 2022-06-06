# 문자열, 숫자, 단어가 주어질때 문자열에서 주어진 숫자 자리에
# 주어진 단어를 조합하여 출력

def mutate_string(string, position, character):
    string = list(s)
    string[position] = character
    result = ''.join(string)
    return result
  
s = 'abracadabra'
i = 5
c = 'k'
  
s_new = mutate_string(s, int(i), c)
print(s_new)