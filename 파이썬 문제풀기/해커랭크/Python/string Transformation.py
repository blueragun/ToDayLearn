import os

# 영문 대소문자를 공백으로 구분한 문자열로 구성된 문장이 있습니다. 
# 주어진 알고리즘에 따라 각 문자열을 변환하고 새 문장을 반환합니다. 
# 각 문자열은 다음과 같이 수정해야 합니다.  
# 문자열의 첫 번째 문자는 변경되지 않은 상태로 유지 됩니다. 
# 각 후속 문자에 대해 x라고 말하면 그 앞에 오는 문자를 고려합니다(예: y). 
# 영어 알파벳에서 y가 x보다 앞에 있으면 x를 대문자 o 로 변환합니다. 
# 영어 알파벳에서 x가 y보다 앞에 있으면 x를 소문자로 변환합니다. 
# x와 y가 같으면 문자가 변경되지 않습니다.

# 입력 : “cOOL dog”

# c가 o보다 알파벳이 빠르기에 첫번째 o는 대문자, 두번째 o의 앞 문자도 o 이기 때문에
# 변경되지 않는다. 마지막 L의 앞문자는 O로 알파벳 순서가 뒤이기 때문에 소문자

def transformSentence(sentence):
    # Write your code here
    
    l = sentence.split() # 입력받는 문장을 분리한다.
    
    data = []
    senten = ""
    
    for i in l :
        senten += i[0]
        
        for j in range(0, len(i)-1) :
            if (i[j].lower()) < (i[j+1].lower()) :
                senten += (i[j+1].upper())
                
            elif (i[j].lower()) > (i[j+1].lower()) :
                senten += (i[j+1].lower()) 
                
            else :
                senten += i[j+1]
        
        data.append(senten) # data에 변형된 값을 추가한다.
        senten = ""
        
    result = ""
        
    for i in data :
        result += " " + i # 공백을 추가한 채로 알파벳을 추가한다.
    return(result.strip())   # 결과값의 공백을 제거한다.
        


sentence = input()

result = transformSentence(sentence)

print(result)