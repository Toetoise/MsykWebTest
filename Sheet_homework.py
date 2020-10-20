import time
import random
from Upload_file import Upload
from selenium.webdriver.common.keys import Keys


class Sheet:
    def __init__(self, driver):
        self.driver = driver

    def sheet(self):
        self.driver.find_element_by_id("addHomeworkButton").click()
        time.sleep(1)
        # 选择学科
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[1]').click()
        # 输入作业名称
        self.driver.find_element_by_id("homeworkName").send_keys("答题卡_1")
        self.driver.find_element_by_css_selector('[type="7"]').click()
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

        self.driver.find_element_by_id("homework-description").send_keys("这是自动化测试_答题卡的作业说明")
        self.driver.find_element_by_css_selector('[title="从素材库添加"]').click()
        resourcetypes = ['ppt', 'jpg', 'mp3', 'mp4', 'doc', 'pdf']
        for resourcetype in resourcetypes[0:6:1]:
            self.driver.find_element_by_css_selector('[class="tol-search-input"]').send_keys(resourcetype)
            self.driver.find_element_by_id("searchBtn").click()
            self.driver.find_element_by_css_selector(
                "#materialList > tr:nth-child(1) > td.text-ellipsis > a > label > span").click()
            self.driver.find_element_by_css_selector('[class="tol-search-input"]').send_keys(Keys.CONTROL, "a")
            self.driver.find_element_by_css_selector('[class="tol-search-input"]').send_keys(Keys.DELETE)
            print("选择了", resourcetype)
        self.driver.find_element_by_id("sureBtn").click()
        # 继续添加
        filepaths = [r'D:\BAK_JF\WP\素材\picture\jpg\01.jpg', r'D:\BAK_JF\WP\素材\BUG编写规范.txt',
                     r'D:\BAK_JF\WP\素材\PDF\真\P0209C-数学理(1).pdf']
        for filepath in filepaths[0:4:1]:
            self.driver.find_element_by_id("showButton").click()
            self.driver.find_element_by_partial_link_text("本地添加").click()
            time.sleep(1)
            print(filepath)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
            success = self.driver.find_element_by_xpath('//*[text()="上传成功 "]')
            while success.is_displayed():
                self.driver.find_element_by_id("local-sure").click()
                break
        print("上传了图片、txt、PDF")
        # 添加答题卡
        self.driver.find_element_by_css_selector('[class="btn btn-sm btn-blue btn-tjxt continue-add-1"]').click()
        self.driver.find_element_by_id("question-num1").send_keys("1")
        self.driver.find_element_by_css_selector('[class="btn btn-sm btn-blue"]').click()
        options = ['[for="r0-0"]', '[for="r0-1"]', '[for="r0-2"]', '[for="r0-3"]']
        option = random.choice(options)
        self.driver.find_element_by_css_selector(option).click()
        question = [['[value="2"]', "question-num2"],
                    ['[value="5"]', "question-num2"],
                    ['[value="3"]', "question-num2"]]
        for [questiontype, questionnum] in question[0:3:1]:
            self.driver.find_element_by_css_selector('[class="btn btn-sm btn-blue btn-tjxt continue-add-2"]').click()
            self.driver.find_element_by_xpath('//*[@id="createExerciseDiv"]/div/div/div/div/div[1]/div/div').click()
            self.driver.find_element_by_css_selector(questiontype).click()
            self.driver.find_element_by_id(questionnum).send_keys("1")
            self.driver.find_element_by_css_selector('[class="btn btn-sm btn-blue"]').click()
        multipleoption = random.randint(1, 4)
        self.driver.find_element_by_css_selector(
            '#question-ul > li[data-ques-type="2"] > div.dtk-tm-li-body > label:nth-child({}) > span'.format(multipleoption)).click()
        torf = ['[for="r2-0"]', '[for="r2-1"]']
        judgment = random.choice(torf)
        self.driver.find_element_by_css_selector(judgment).click()
        # 未添加知识点和答案解析
        print("添加了单选题、多选题、判断题、主观题")
        self.driver.find_element_by_xpath('//*[text()="发布"]').click()
