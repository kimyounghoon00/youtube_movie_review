import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_image_title(url):
    # 웹 드라이버 초기화
    # driver_path = '../driver/chromedriver'
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # or bigger second

    # 열고자 하는 채널 -> 동영상 목록으로 된 url 페이지를 엶
    driver.get(url)

    image_list = list()  # 썸네일을 받을 수 있는 주소 저장용 리스트
    title_list = list()  # 썸네일 제목을 저장하는 리스트

    idx = 1
    while True:
        try:
            img_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(
                idx) + ']/div[1]/ytd-thumbnail/a/yt-img-shadow/img'
            title_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(
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
            print(idx, title.text, img_url)
            title_list.append(title.text)

            idx += 1
        except Exception as e:
            print()
            print(e)
            break
    assert len(image_list) == len(title_list)
    driver.close()
    return image_list, title_list


# 진솔한 리뷰
url1 = 'https://www.youtube.com/channel/UC3DNe5b3NYZ5ojre8YE1_xw/videos'
image1, title1 = get_image_title(url1)
# 홍시네마
url2 = 'https://www.youtube.com/channel/UCtwxuughKbSAV0e4bnz4ORg/videos'
image2, title2 = get_image_title(url2)
# 무비우스
# https://www.youtube.com/channel/UCHPuCs7c4jJmDJHdOn3mIDA
# 어쩌다 영화한편
# https://www.youtube.com/channel/UC4a9C90kI9QzTVx9HRdlsjw
# 조조할인
# https://www.youtube.com/channel/UCfsdRdf5YvHDb3bWxkF_0_g
# 영화소녀
# https://www.youtube.com/channel/UCotjQBM9iMsYS0sY-FB0kNw
# 리뷰 MASTER
# https://www.youtube.com/channel/UCul4FTKARC-EaBq0e8UH7RA
# 뿔라 PULA
# https://www.youtube.com/channel/UCOVjr02SIkhawHoJzT3WuhQ
# 동네비디오방
# https://www.youtube.com/channel/UCXvftM-43hGjGc1TA-8Y_IA
# 시네마로드
# https://www.youtube.com/channel/UCe9xx5O_rt4MxQuv4ciPX5g