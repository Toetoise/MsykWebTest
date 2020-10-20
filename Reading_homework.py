import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Reading:
    def __init__(self, driver):
        self.driver = driver

    def reading(self):
        self.driver.find_element_by_id("addHomeworkButton").click()
        time.sleep(1)
        # 选择学科
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[1]').click()
        # 输入作业名称
        self.driver.find_element_by_id("homeworkName").send_keys("阅读作业_1")
        self.driver.find_element_by_css_selector('[class=" reading-material"]').click()
        starttime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        endtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() + 7200))
        print(starttime, endtime)
        # 设置起止时间
        self.driver.find_element_by_xpath(
            '//*[@class="form-control date-picker exam-datetimepicker exam-start"]').click()
        self.driver.find_element_by_xpath('//*[@id="datetimepicker"]').send_keys(Keys.CONTROL, "a")
        self.driver.find_element_by_xpath('//*[@id="datetimepicker"]').send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath('//*[@id="datetimepicker"]').send_keys(endtime)
        # 选择作业范围
        self.driver.find_element_by_xpath('//*[@id="class-squad"]/div/div[1]/span').click()
        self.driver.find_element_by_id("submitCourseware").click()
        # 添加ppt
        self.driver.find_element_by_css_selector('[class="fa fa-file-powerpoint-o"]').click()
        ppt_num = len(self.driver.find_elements_by_css_selector('[class="fa fa-check"]'))
        select_ppt = random.randint(1, ppt_num)
        choose = self.driver.find_element_by_css_selector(
            '#containerDiv > div.material > div > ul > li:nth-child({}) > a'.format(select_ppt))
        ActionChains(self.driver).move_to_element(choose).perform()
        self.driver.find_element_by_css_selector(
            '#containerDiv > div.material > div > ul > li:nth-child({}) > a > span.card-checkbox > i'.format(select_ppt)).click()
        self.driver.find_element_by_id("saveResource").click()
        # 添加图片
        self.driver.find_element_by_css_selector('[class="fa fa-file-image-o"]').click()
        image_num = len(self.driver.find_elements_by_css_selector('[class="fa fa-check"]'))
        select_image = random.randint(1, image_num)
        choose = self.driver.find_element_by_css_selector(
            '#containerDiv > div.material > div > ul > li:nth-child({}) > a'.format(select_image))
        ActionChains(self.driver).move_to_element(choose).perform()
        self.driver.find_element_by_css_selector(
            '#containerDiv > div.material > div > ul > li:nth-child({}) > a > span.card-checkbox > i'.format(select_image)).click()
        self.driver.find_element_by_id("saveResource").click()
        # 添加音频
        self.driver.find_element_by_css_selector('[class="fa fa-file-audio-o"]').click()
        audio_num = len(self.driver.find_elements_by_css_selector('[class="lbl audio-checkbox-btn"]'))
        select_audio = random.randint(1, audio_num)
        self.driver.find_element_by_css_selector(
            '#audio-material-5-list > tr:nth-child({}) > td > label > span'.format(select_audio)).click()
        self.driver.find_element_by_id("saveResource").click()
        # 添加视频
        self.driver.find_element_by_css_selector('[class="fa fa-file-video-o"]').click()
        video_num = len(self.driver.find_elements_by_css_selector('[class="fa fa-check"]'))
        select_video = random.randint(1, video_num)
        choose = self.driver.find_element_by_css_selector(
            '.material > div > ul > li:nth-child({}) > a'.format(select_video))
        ActionChains(self.driver).move_to_element(choose).perform()
        self.driver.find_element_by_css_selector(
            '.material > div > ul > li:nth-child({}) > a > span > i'.format(select_video)).click()
        self.driver.find_element_by_id("saveResource").click()
        # 添加文档
        self.driver.find_element_by_css_selector('[class="fa fa-file-o"]').click()
        file_num = len(self.driver.find_elements_by_css_selector('[class="lbl card-checkbox-btn"]'))
        select_file = random.randint(1, file_num)
        self.driver.find_element_by_css_selector(
            '#material-5-list > tr:nth-child({}) > td.text-center > label > span'.format(select_file)).click()
        self.driver.find_element_by_id("saveResource").click()
        # 添加pdf
        self.driver.find_element_by_css_selector('[class="fa fa-file-pdf-o"]').click()
        pdf_num = len(self.driver.find_elements_by_css_selector('[class="lbl card-checkbox-btn"]'))
        select_pdf = random.randint(1, pdf_num)
        self.driver.find_element_by_css_selector(
            '#material-5-list > tr:nth-child({}) > td > label > span'.format(select_pdf)).click()
        self.driver.find_element_by_id("saveResource").click()
        # 保存&&发布
        self.driver.find_element_by_xpath('//button[@class="btn  btn-blue"]').click()
        self.driver.find_element_by_xpath('//*[@id="contentDiv"]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div[1]/a[1]').click()