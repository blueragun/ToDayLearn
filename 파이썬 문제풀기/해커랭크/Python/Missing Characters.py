# 주어지는 값(숫자+알파벳 조합)을 0~9, a~z 중 제거한뒤 숫자, 알파벳 순으로 정렬하여
# 결과값을 도출해라
# 입력 : c87dkjgksj13
# 출력 : 024569abefhilmnopqrtuvwxyz

import os

aski = ['0','1','2','3','4','5','6','7','8','9','a','b','c',
        'd','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']

# 숫자와 소문자 알파벳 전체를 리스트화 한다.


def missingCharacters(s):
    # Write your code here
    data = []
    for i in s :  # 입력된 단어를 data에 추가한다.
        data.append(i)
    
    data = list(set(data)) # data를 중복값 제거하며 list화 시킨다.
    
    for j in data :  # data에 있는 알파벳, 숫자를 아스키에서 제거한다.
        aski.remove(j)
    
    c = ''
    for k in aski : # 아스키에 존재하는 값을 c에 추가한다.
        c += k
        
    c = sorted(c)  # 오름차순으로 정렬한다.
    
    c = ''.join(c) # 공백없이 붙인다 / 리스트는 strip()을 사용할 수 없다
    
    return(c)
        

s = input()

result = missingCharacters(s)

print(result)