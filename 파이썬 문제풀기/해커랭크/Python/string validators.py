# str.isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어 있으면 참, 아니면 거짓
# str.isalpha() : 문자열이 영어 혹은 한글로 되어 있으면 참, 아니면 거짓
# str.isdigit() : 문자열이 숫자로만 이루어져 있으면 참, 아니면 거짓
# str.islower() : 문자열이 소문자면 참, 아니면 거짓
# str.isupper() : 문자열이 대문자면 참, 아니면 거짓

# 문자열 s가 주어질때
# 하나의 영어, 한글, 숫자가 있으면 참, 아니면 거짓
# 하나의 알파벳이 있으면 참, 아니면 거짓
# 하나의 숫자가 있으면 참, 아니면 거짓
# 하나의 소문자가 있으면 참, 아니면 거짓
# 하나의 대문자가 있으면 참, 아니면 거짓

s = 'qA2'

print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))