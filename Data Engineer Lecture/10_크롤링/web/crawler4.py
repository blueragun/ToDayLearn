from selenium import webdriver   # 셀레늄은 뷰티풀의 파싱기능을 가지고 있어 bs4를 임포트 할 필요 없음
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# webdriver
# 크롬을 기준으로 현재 사용하고 있는 버전에 맞춰 webdriver 다운
service = Service(executable_path="D:\\강의\\Visual code\\WORKSPACE\\web\\chromedriver.exe")
browser = webdriver.Chrome(service=service)

url = 'https://itempage3.auction.co.kr/DetailView.aspx?itemno=C220859288'
