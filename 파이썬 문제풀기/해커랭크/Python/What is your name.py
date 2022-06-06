# 입력되는 s(이름)에 인사와 문장을 붙여 출력

from pkg_resources import resource_stream


def print_full_name(first, last):
    # Write your code here
    data = first_name + ' ' + last_name
    data = 'Hello '+ data + '! ' + 'You just delved into python.'
    return data
    
first_name = "Rose"
last_name = "Taylor"   

result = print_full_name(first_name, last_name)

print(result) 