import urllib.request  # 매번 소켓 http 사용할 필요없이 라이브러리를 이용해 손쉽게 http 통신구현 가능
from fake_useragent import UserAgent

# agent = UserAgent()
# header = {'User-Agent' : agent.chrome}

url = 'https://imgnews.pstatic.net/image/020/2022/01/03/0003403400_001_20220103100801057.jpg'
## request = urllib.request.Request(url, headers = header )
## response = urllib.request.urlopen( request )
## print( response.read() )

# 위와 같은 형식으로 하거나 또는 아래와 같이
# urllib은 urlretrieve 함수를 이용해서 한번에 파일 저장

# 파일을 저장할 경로
path = './data/download2.jpg'

# opener 객체를 생성해서 헤더를 수정을 먼저해준다
# opener = urllib.request.build_opener()
# opener.addheaders = [('User-Agent', agent.chrome)]
# urllib.request.install_opener(opener)

# 이제는 urlretrieve를 이용해서 다운로드한 파일을 바로 생성할 수 있다.
urllib.request.urlretrieve( url, path )


# data 폴더에 이미지가 잘 저장되어 있다.



# ---------------------------------------------------------------------

# 권한이 안걸린 파일은 위와 같이 3문장으로도 간단히 저장할 수 있다.