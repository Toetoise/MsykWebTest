import random
import time
from selenium.webdriver import ActionChains
from autotestMsyk.Upload_file import Upload
from autotestMsyk import Config_file


class Courseware:
    def __init__(self, driver):
        self.driver = driver

    def courseware(self):
        self.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()
        self.driver.find_element_by_id("courseware").click()
        self.driver.find_element_by_id("addNewCourseware").click()
        # myCoursewaresubject_num = len(self.driver.find_elements_by_xpath(
        #     '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span'))
        # myCoursewaresubject = random.randint(1, myCoursewaresubject_num)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[{}]'.format(myCoursewaresubject)).click()
        self.driver.find_element_by_xpath('//span[text()="历史"]').click()
        mycoursewaresubject_num = len(self.driver.find_elements_by_xpath('//*[@id="classDiv"]/span'))
        mycoursewareclass = random.randint(1, mycoursewaresubject_num)
        if mycoursewaresubject_num > 1:
            self.driver.find_element_by_xpath('//*[@id="classDiv"]/span[{}]'.format(mycoursewareclass)).click()
        self.driver.find_element_by_id("coursewarName").send_keys("高中历史备课包")
        self.driver.find_element_by_class_name('upload-img-btn').click()
        filepath = Config_file.UN_filepaths[0]
        time.sleep(1)
        Upload(self.driver).upload_file(filepath)
        time.sleep(1)
        self.driver.find_element_by_id("submitCourseware").click()
        self.driver.find_element_by_class_name("js-addNavItem").click()
        self.driver.find_element_by_xpath('//*[@id="navCourse"]/li[last()-1]').click()
        time.sleep(1)
        # 添加PPT
        self.driver.find_element_by_xpath('//span[text()="PPT"]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 添加文档
        self.driver.find_element_by_xpath('//span[text()="文档"]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 添加图片
        self.driver.find_element_by_xpath('//span[text()="图片"]').click()
        self.driver.find_element_by_xpath('//a[text()="本地添加"]').click()
        time.sleep(2)
        Upload(self.driver).upload_file(filepath)
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[text()="图片"]').click()
        self.driver.find_element_by_xpath('//a[text()="从素材库添加 "]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 添加音频
        self.driver.find_element_by_xpath('//span[text()="音频"]').click()
        # 功能出现bug
        # self.driver.find_element_by_xpath('//a[text()="本地添加"]').click()
        # mic_filepath = Config_file.Local_filepaths[1]
        # time.sleep(2)
        # Upload(self.driver).upload_file(mic_filepath)
        # time.sleep(1)
        self.driver.find_element_by_xpath('//a[text()="从素材库添加 "]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 添加微课
        self.driver.find_element_by_xpath('//span[text()="微课"]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 添加测验
        self.driver.find_element_by_xpath('//span[text()="测验"]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 添加例题
        self.driver.find_element_by_xpath('//span[text()="例题"]').click()
        check = self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_css_selector("ul.card-list > li:nth-child(1) > a > span.card-checkbox").click()
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        time.sleep(1)
        # 未完善完
        # # 添加答题卡
        # self.driver.find_element_by_xpath('//span[text()="答题卡"]').click()
        # # 单选题
        # self.driver.find_element_by_id("choice-num-set").clear()
        # self.driver.find_element_by_id("choice-num-set").send_keys("5")
        # self.driver.find_element_by_id("quesCount").clear()
        # self.driver.find_element_by_id("quesCount").send_keys("2")
        # self.driver.find_element_by_xpath('//span[text()="添加"]').click()
        # # 多选题
        # self.driver.find_element_by_id("ques-type-select").click()
        # self.driver.find_element_by_xpath('//span[text()="多选题"]').click()
        # self.driver.find_element_by_xpath('//span[text()="添加"]').click()
        # # 判断题
        # self.driver.find_element_by_id("ques-type-select").click()
        # self.driver.find_element_by_xpath('//span[text()="多选题"]').click()
        # self.driver.find_element_by_xpath('//span[text()="添加"]').click()
        # # 主观题
        # self.driver.find_element_by_id("ques-type-select").click()
        # self.driver.find_element_by_xpath('//span[text()="主观题"]').click()
        # self.driver.find_element_by_xpath('//span[text()="添加"]').click()
        # 作业讲解
        self.driver.find_element_by_xpath('//span[text()="作业讲解"]').click()
        self.driver.find_element_by_css_selector("#homeworkList:nth-child(1) > li:nth-child(2)").click()
        self.driver.find_element_by_xpath('//*[@id="ques-num-list"]/div[1]/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[text()="保存"]').click()
        # 未完善完
        # # 反馈
        # Feedback = self.driver.find_element_by_xpath('//div[@class="class-feedback"]/div[2]/table/tbody/tr[4]/td[1]')
        # self.driver.execute_script("arguments[0].scrollIntoView();", Feedback)
        # self.driver.find_element_by_xpath('//div[@class="class-feedback"]/div[2]/table/tbody/tr[2]/td[2]/label[2]/span').click()
        # self.driver.find_element_by_xpath('//*[text()="保存"]').click()
