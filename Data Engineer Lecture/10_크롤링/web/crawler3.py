import requests
import bs4

url = 'https://movie.naver.com/movie/point/af/list.naver'
response = requests.get( url )
# print( reponse.text )
# 이렇게 원하는 정보가 있는 페이지 전체를 가져온다..

html = response.text


# 가져온 페이지 내 원하는 것을 뽑아내기위해 BeautifulSoup을 사용

review = bs4.BeautifulSoup(html)
search = {
    'class':'title'
}

td_elements = review.find_all('td', attrs=search)

# 하위요소 뽑기

# tmp = list(td_elements[2].children)   # 이렇게하면 리스트형태로 묶어 프린트됨

# tmp = list(td_elements[2].children)

# print(td_elements[2].text.split('\n'))  # 문자만 분리해서 뽑아냄

# print(td_elements[2].text.split('\n')[5])   # 5번째 요소 프린트

for element in td_elements :
    title = element.find('a').text
    score = element.find('em').text
    # print(element.text.split('\n')[5] )   # 전체 element 중 5번째 요소에 해당하는 것을 프린트
    
    r = element.text.split('\n')[5]
    
    print(f'영화제목 : {title}')
    print(f'평점 : {score}')
    print(f'리뷰 : {r}')
    
    
# < 페이지 전체 즉 모든 리뷰를 가져오려면 어떻게 해야 할까 >>
no = ??
url = f'https://movie.naver.com/movie/point/af/list.naver?&page={no}'

response == requests.get( url )
response.text