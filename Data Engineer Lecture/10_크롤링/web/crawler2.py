import requests
from fake_useragent import UserAgent

agent = UserAgent()
header = {'User-Agent' : agent.chrome}

url = 'https://imgnews.pstatic.net/image/020/2022/01/03/0003403400_001_20220103100801057.jpg?type=w647'

response = requests.get(url, headers=header)

with open('./data/download3.jpg', 'wb') as file :
    file.write(response.content )