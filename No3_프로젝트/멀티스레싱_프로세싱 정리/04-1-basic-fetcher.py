# https://2.python-requests.org/en/master/user/advanced/#id1
# pip install requests

import requests
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    with requests.Session() as session:
    # with : 세션을 열고 자동으로 닫아주는 역할 / 네이버 실행 후 긁어오고 닫고, 구글 실행 후 긁어오고 닫고
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 12