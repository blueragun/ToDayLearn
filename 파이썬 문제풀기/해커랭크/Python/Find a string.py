# 문자열이 주어지고 문자열에 포함된 단어가 주어질때
# 문자열에서 해당 단어와 동일한 단어가 몇개인지 출력 

def count_substring(string, sub_string):
    s_len = len(string)
    sub_len = len(sub_string)
    result = 0
    for i in range(0, s_len) :
        if string[i:sub_len+i] == sub_string :
            result += 1
    return result
  
string = "ABCDCDC"
string = string.strip()
print(string)
sub_string = "CDC"
sub_string = sub_string.strip()

count = count_substring(string, sub_string)
print(count)