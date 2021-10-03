import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbmovie_review_test


def get_image_title(url):

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # or bigger second

    # 열고자 하는 채널 -> 동영상 목록으로 된 url 페이지
    driver.get(url)

    image_list = list()  # 썸네일을 받을 수 있는 주소 저장용 리스트
    title_list = list() # 제목
    play_time_list=list() # 썸네일 재생시간을 저장하는 리스트 가장 중요!!!
    views_list=list() # 조회수
    video_list = list() # 비디오 url 저장용 라스트



    idx = 1
    while True:
        try:
            img_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(
                idx) + ']/div[1]/ytd-thumbnail/a/yt-img-shadow/img'
            title_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(
                idx) + ']/div[1]/div[1]/div[1]/h3/a'
            play_time_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(
                idx) + ']/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'
            views_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+ str(
                idx) + ']/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]'
            video_link_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer['+ str(
                idx) + ']/div[1]/div[1]/div[1]/h3/a'



            # 이미지가 곧바로 로드 되지 않을 때, 20초간 강제로 기다림
            img = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, img_xpath)))
            if img is None:
                print(idx, 'img is not loaded.')

            # 한 페이지에 약 8개 불러오는 데, 동영상 목록을 추가 불러오기 위해 스크롤 내림
            if idx % 8 == 0:
                driver.execute_script('window.scrollBy(0, 1080);')
                time.sleep(2)
                driver.execute_script('window.scrollBy(0, 1080);')
                time.sleep(2)
                driver.execute_script('window.scrollBy(0, 1080);')
                time.sleep(2)

            # 썸네일 주소를 리스트에 저장
            image = driver.find_element_by_xpath(img_xpath)
            img_url = image.get_attribute('src')
            image_list.append(img_url)

            # 타이틀을 리스트에 저장
            title = driver.find_element_by_xpath(title_xpath)
            title_list.append(title.text)

            #재생시간 리스트에 저당
            play_time = driver.find_element_by_xpath(play_time_xpath)
            play_time_list.append(play_time.text[0:2].strip())

            #조회수 리스트에 저장
            view_time = driver.find_element_by_xpath(views_xpath)
            views_list.append(view_time.text)


            #동영상 링크 리스트에 저장
            video = driver.find_element_by_xpath(video_link_xpath)
            video_url = video.get_attribute('href')
            video_list.append(video_url)

            print(idx, title.text, img_url, play_time.text[0:2].strip(), view_time.text, video_url)


            idx += 1

        except Exception as e:
            print()
            print(e)
            break
    assert len(image_list) == len(title_list)
    driver.close()
    doc = {'image_list': image_list, 'title_list': title_list, 'play_time_list': play_time_list,
           'views_list': views_list, 'viseo_list': video_list}
    db.movies_review2.insert_one(doc)

    return image_list, title_list, play_time_list, views_list, video_list





# 진솔한 리뷰
url1 = 'https://www.youtube.com/channel/UC3DNe5b3NYZ5ojre8YE1_xw/videos'
image1, title1, play_time1, view_time1, video1 = get_image_title(url1)





