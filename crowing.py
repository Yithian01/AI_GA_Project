from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# iframe의 src URL
iframe_src_url = 'https://choocheon.com/recommend/pc-%ED%8C%8C%EC%9B%8C%EC%84%9C%ED%94%8C%EB%9D%BC%EC%9D%B4-%EC%B6%94%EC%B2%9C-%EC%9D%B8%EA%B8%B0-%ED%8C%90%EB%A7%A4-%EC%88%9C%EC%9C%84/'

# Selenium을 사용해 웹 드라이버 초기화
driver = webdriver.Chrome()

# iframe의 src URL로 직접 접근
driver.get(iframe_src_url)

# 페이지가 완전히 로드될 때까지 기다린 후 HTML 가져오기
html = driver.page_source

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 정보를 저장할 리스트 생성
data = []

# 원하는 데이터 추출 (예시: 모든 'h1' 태그)
for span in soup.select('tbody tr td'):
    data.append([span.text])

# 브라우저 닫기
driver.close()

# CSV 파일로 저장
with open('SSD_LIST.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Header'])  # 선택적으로 컬럼 헤더를 작성할 수 있습니다.
    writer.writerows(data)  # 추출한 데이터를 쓰기
