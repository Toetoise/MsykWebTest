import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Exam:
    def __init__(self, driver):
        self.driver = driver

    def exam(self):
        self.driver.find_element_by_id("addHomeworkButton").click()
        time.sleep(1)
        # 选择学科
        # self.driver.find_element_by_xpath(
        #     '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[1]').click()
        self.driver.find_element_by_xpath('//span[text()="历史"]').click()
        # 输入作业名称
        self.driver.find_element_by_id("homeworkName").send_keys("小测_1")
        self.driver.find_element_by_css_selector('[class=" exam-material"]').click()
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
        # 添加微课
        self.driver.find_element_by_link_text("添加微课").click()
        video_num = len(self.driver.find_elements_by_css_selector('[class="card-item  "]'))
        select_video = random.randint(1, video_num)
        choose = self.driver.find_element_by_css_selector(
            '#containerDiv > div.material > div > ul >li:nth-child({})'.format(select_video))
        ActionChains(self.driver).move_to_element(choose).perform()
        self.driver.find_element_by_css_selector(
            '#containerDiv > div.material > div > ul >li:nth-child({}) > a > span > i'.format(select_video)).click()
        self.driver.find_element_by_css_selector('button[id="saveResource"]').click()
        # 添加习题
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[@onclick="addQuestion()"]').click()
        exercise_table = self.driver.find_element_by_xpath('//*[@id="containerDiv"]/div[1]/div[2]/table')
        rows = len(exercise_table.find_elements_by_tag_name('tr'))
        check = random.randint(1, rows)
        self.driver.find_element_by_css_selector(
            '#material-5-list > tr:nth-child({}) > td.text-ellipsis > a > span'.format(check)).click()
        multiple_choice_num = len(self.driver.find_elements_by_xpath('//div[@class="widget-box"]'))
        # Multiple_choice = random.randint(1, multiple_choice_num)
        i = 1
        while i < multiple_choice_num + 1:
            self.driver.find_element_by_xpath('//*[@id="contentDiv"]/div[{}]/div[1]/div/label/span'.format(i)).click()
            i = i + 1
        self.driver.find_element_by_css_selector('button[id="saveResource"]').click()
        self.driver.find_element_by_link_text("批量设置分值>").click()
        batchpoint_num = len(self.driver.find_elements_by_css_selector('[class="txt"]'))
        i = 2
        while i < batchpoint_num + 2:
            self.driver.find_element_by_css_selector(
                '#tbody > tr:nth-child({}) > td:nth-child(3) > input'.format(i)).clear()
            self.driver.find_element_by_css_selector(
                '#tbody > tr:nth-child({}) > td:nth-child(3) > input'.format(i)).send_keys("5")
            i = i + 1
        self.driver.find_element_by_id('saveScore').click()
        self.driver.find_element_by_css_selector('[id="save"]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="contentDiv"]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div[1]/a[1]').click()
