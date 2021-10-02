import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.youtube.com/channel/UCtwxuughKbSAV0e4bnz4ORg/videos',headers=headers)
# #
# soup = BeautifulSoup(data.text, 'html.parser')
#
#
# # 코딩 시작

driver = webdriver.Chrome()
url = 'https://www.youtube.com/channel/UCtwxuughKbSAV0e4bnz4ORg/videos'
driver.get(url)
page=driver.page_source


movies=driver.find_elements_by_id("details") # 영화 내용 및 조회수


# for movie in movies:
#     print(movie.text)


# for i in range(len(movies)): # 타이틀 리스트 만듬 계속 조회수랑 업데이트 딸려옴 ㅠㅠ -> 알고보니 같은 인덱스에 전부 포함. 각각 크롤링 해야할 듯...타이틀, 조회수, 업데이트 날짜...
#     title = []
#     title.append(movies[i].text)
#     print(i,title)

# play_time=driver.find_elements_by_id("thumbnail") # 재생 시간 근데 리스트 값에 공란 존재함 어떻게 공란은 제거하는지
# for time in play_time:
#     if time is not None:
#         print(time.text)

#
# for i in range(len(play_time)): #재생 시간 리스트 만듬 [''] 제거 예정. 반복문 돌려야 하나?
#     video_time=[]
#
#     video_time.append(play_time[i].text)
#
#     print(i, video_time)




# for i in range(len(play_time)): #재생 시간 리스트 만듬 [''] 제거 예정. 반복문 돌려야 하나? remove 함수 사용???
#     video_time=[]
#
#     video_time.append(play_time[i].text)
#
# while '['']' in video_time:
#     video_time.remove('['']')



# hong_contents=driver.find_elements_by_id("contents") # 영화 제목 조회수 및 재생 시간...근데 전부 하나에
# for content in hong_contents:
#     print(content.text)

# img_path="//*[@id="thumbnail"]/yt-img-shadow"
# //*[@id="dismissible"]/ytd-thumbnail
# //*[@id="thumbnail"]




#이미지 썸네일
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]
#
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/ytd-thumbnail
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/ytd-thumbnail/a
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/ytd-thumbnail/a/yt-img-shadow
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/ytd-thumbnail/a/yt-img-shadow/img
#
# #재생시간
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span
#
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[4]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span
#
# #조회수 리스트
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[4]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]
# /html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]
#
#
# #링크
/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+ str(idx) + ']/div[1]/div[1]/div[1]/h3/a










