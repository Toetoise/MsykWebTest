import random
import time
from autotestMsyk.Upload_file import Upload
from autotestMsyk import Config_file


class Material:
    def __init__(self, driver):
        self.driver = driver

    def material(self):
        self.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()
        self.driver.find_element_by_id("material").click()
        bullet = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]')
        if bullet.is_displayed():
            print("有弹框")
            self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
        else:
            print("没有弹框")
        self.driver.find_element_by_xpath('//*[@id="h3-title-1"]/div[1]').click()
        # self.driver.find_element_by_xpath('//*[@id="mymaterialsubjectul"]/li[4]').click()
        # self.driver.find_element_by_xpath('//*[@id="gradeList"]/li[3]').click()
        mymaterialsubject_num = len(self.driver.find_elements_by_css_selector("#mymaterialsubjectul li"))
        mymaterialsubject = random.randint(1, mymaterialsubject_num)
        # 用{}占位在css中，format格式化随机数代入
        materialsubject = self.driver.find_element_by_css_selector(
            '#mymaterialsubjectul > li:nth-child({})'.format(mymaterialsubject))
        self.driver.execute_script("arguments[0].scrollIntoView();", materialsubject)
        materialsubject.click()
        mymaterialgrade_num = len(self.driver.find_elements_by_css_selector("#gradeList li"))
        mymaterialgrade = random.randint(1, mymaterialgrade_num)
        materialgrade = self.driver.find_element_by_css_selector(
            '#gradeList > li:nth-child({})'.format(mymaterialgrade))
        self.driver.execute_script("arguments[0].scrollIntoView();", materialgrade)
        materialgrade.click()
        time.sleep(2)
        filepaths = Config_file.UN_sck_filepaths
        for filepath in filepaths[0:4:1]:
            self.driver.find_element_by_xpath('//*[@id="file-upload"]').click()
            time.sleep(1)
            print(filepath)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
        print("上传了图片、音频、视频、PDF")
        for filepath in filepaths[4:6:1]:
            self.driver.find_element_by_id("all-ppt-upload").click()
            self.driver.find_element_by_id("ppt-upload-local").click()
            time.sleep(1)
            print(filepath)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
        print("快速上传了ppt")
        for filepath in filepaths[6:8:1]:
            self.driver.find_element_by_id("all-ppt-upload").click()
            self.driver.find_element_by_id("ppt-hight-upload").click()
            time.sleep(1)
            print(filepath)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
        print("优质上传了ppt")
        self.driver.find_element_by_css_selector('#all-ques-upload > a').click()
        self.driver.find_element_by_xpath('//*[@id="question-upload"]').click()
        time.sleep(1)
        print(filepaths[8])
        Upload(self.driver).upload_file(filepaths[8])
        time.sleep(1)
        # 题库
        self.driver.find_element_by_xpath('//*[@id="question-lib"]/span').click()
        time.sleep(1)
        # 系统题库
        self.driver.find_element_by_xpath('//*[@id="toOwnerMagic"]').click()
        # self.driver.find_element_by_xpath('//li[@class="f-fr"]').click()
        # self.driver.find_element_by_xpath('//*[@class="badge"]').click()
        # self.driver.find_element_by_xpath('//*[@class="basket-ft"]/a').click()
        # questions_num = self.driver.find_element_by_xpath('//span[@id="j_que_total_amount"]')
        # self.driver.find_element_by_xpath('//div[@id="j_muti_set_score"]').click()
        # self.driver.find_element_by_xpath('//*[@class="mini-ipt j_max_quenum"]').send_keys(questions_num)
        # self.driver.find_element_by_xpath('//*[@class="every j_every_score"]').send_keys("1")
        # self.driver.find_element_by_id("primary").click()
        # self.driver.find_element_by_xpath('//a[@data-opt="save"]').click()
        # self.driver.find_element_by_id("primary").click()
        # 文档
        self.driver.find_element_by_xpath('//*[@id="word-upload"]').click()
        time.sleep(1)
        print(filepaths[9])
        Upload(self.driver).upload_file(filepaths[9])
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="newFolder"]').click()
        self.driver.find_element_by_xpath('//*[@id="newFolderName"]').send_keys("TEST1")
        self.driver.find_element_by_xpath('//*[@id="newFolderTr"]/td[2]/span/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="newFolder"]').click()
        self.driver.find_element_by_xpath('//*[@id="newFolderTr"]/td[2]/span/a[2]').click()

        time.sleep(2)
        # i = 0
        # while i < len(self.driver.find_elements_by_css_selector('#mainList tr')):
        #     file_status = self.driver.find_elements_by_css_selector('#mainList > tr > td:nth-child(3) > span')
        #     while file_status == "请添加知识点":
        #         print(file_status.text)
        #         file_status.click()
        #         while file_status == "请完善知识点":
        #             print(file_status.text)
        #             file_status.click()
        #             while file_status == "正在切题":
        #                 print(file_status.text)
        #                 print("请等待...")
        #                 self.driver.find_element_by_xpath('//*[@id="myMaterialFresh"]').click()
        #                 for file_status == "正在切题":
        #                     self.driver.find_element_by_xpath('//*[@id="myMaterialFresh"]').click()
        #                     break
        #             while file_status
