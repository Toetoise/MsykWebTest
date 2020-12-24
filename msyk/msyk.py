from selenium import webdriver
from selenium.webdriver import ActionChains
from test_loginclass import Login
from Ordinary_homework import Ordinary
from Reading_homework import Reading
from Exam_homework import Exam
from Sheet_homework import Sheet
from Upload_file import Upload
import Config_file
import time
import unittest
import random
import re
import warnings
# import pytest


class TestVisitMsykByEdge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        driver_url = r"H:\Python38\msedgedriver.exe"
        cls.driver = webdriver.Edge(executable_path=driver_url)
        # cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        url = Config_file.Extranet_url
        cls.driver.get(url)
        cls.driver.maximize_window()
        judge_home = cls.driver.find_element_by_xpath('//a[text()="登录"]')
        if judge_home.is_displayed():
            print("首页打开成功！")
        else:
            print("首页打开失败！")
        # Login(cls.driver).login("lusu", "12345678")
        Login(cls.driver).login("nls_1", "Msyk_741")
        time.sleep(1)
        cls.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()

    def test_Homework(self):
        self.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()
        self.driver.find_element_by_id("classAndGradeHomework").click()
        self.driver.find_element_by_xpath('//*[@id="classHomework"]').click()
        self.driver.find_element_by_partial_link_text("班级作业").click()
        time.sleep(1)
        Ordinary(self.driver).ordinary()
        Reading(self.driver).reading()
        Exam(self.driver).exam()
        Sheet(self.driver).sheet()
        self.driver.find_element_by_link_text("待批阅").click()

    def test_Kecheng(self):
        self.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()
        self.driver.find_element_by_id("courseCenter").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[text()="+新建课程"]').click()
        self.driver.find_element_by_id("selectGrade").click()
        self.driver.find_element_by_css_selector('[value="31"]').click()
        self.driver.find_element_by_css_selector('[value="3020"]').click()
        self.driver.find_element_by_css_selector('[value="7027"]').click()
        self.driver.find_element_by_xpath('//*[text()="高一生物必修一"]').click()
        self.driver.find_element_by_class_name("chosen-choices").click()
        self.driver.find_element_by_css_selector('#form_field_select_4_chosen > div > ul > li:nth-child(1)').click()
        self.driver.find_element_by_id("queryDefaultImages").click()
        self.driver.find_element_by_css_selector('[alt="高中生物"]').click()
        self.driver.find_element_by_id("confirmDefaultImage").click()
        self.driver.find_element_by_id("uploadImg").click()
        filepath = Config_file.Local_filepaths[0]
        time.sleep(1)
        Upload(self.driver).upload_file(filepath)
        self.driver.find_element_by_id("textarea").send_keys("这是自动化测试_课程包的课程简介")
        self.driver.find_element_by_id("area").send_keys("这是自动化测试_课程包的课程详情")
        self.driver.find_element_by_id("saveCourseButton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#moduleList > li:nth-child(2)').click()
        self.driver.find_element_by_id("use-system-tree").click()
        check = self.driver.find_element_by_xpath('//*[text()="第一章 走近细胞"]')
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/div[1]/div/a[1]/i').click()
        self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/ul/li[3]/span/div/input').send_keys("自动化")
        check = self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/ul/li[3]/span/div/input')
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/ul/li[3]/div/a[1]/i').click()
        check = self.driver.find_element_by_xpath('//*[text()="第一章 走近细胞"]')
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/div[1]/div/a[1]/i').click()
        self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/ul/li[4]/span/div/div/select').click()
        self.driver.find_element_by_css_selector('[value="2"]').click()
        check = self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/ul/li[4]')
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_xpath('//*[@id="books"]/li[1]/ul/li[4]/div/a[1]/i').click()
        self.driver.find_element_by_id("uploadResourceBtn").click()
        filepath = Config_file.Local_filepaths[2]
        time.sleep(1)
        Upload(self.driver).upload_file(filepath)
        self.driver.find_element_by_id("uploadFileList").click()
        success = self.driver.find_element_by_xpath('//*[text()="上传成功"]')
        while success.is_displayed():
            self.driver.find_element_by_class_name("layui-layer-ico").click()
            print("上传成功")
            break
        self.driver.find_element_by_id("js-go-exercise").click()
        self.driver.find_element_by_id("use-system-tree").click()
        check = self.driver.find_element_by_css_selector('//*[text()="第一章 走近细胞"]')
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_xpath('//*[@id="exercise-tree"]/li[1]/div[1]/div/a[1]/i').click()
        self.driver.find_element_by_css_selector('[class="tree-label block"]').send_keys("自动化")
        self.driver.find_element_by_id("select-source").click()
        self.driver.find_element_by_xpath('//*[@id="jy-choiceContent"]/div[1]/a/i').click()
        self.driver.find_element_by_class_name("layui-layer-btn0").click()
        self.driver.find_element_by_css_selector(
            '#exercise-table-div > table > tbody > tr > td:nth-child(1) > label > span').click()
        self.driver.find_element_by_xpath('//*[@id="exercise-table-div"]/table/thead/tr/th[2]/a').click()
        self.driver.find_element_by_xpath('//*[text()=" 只显示知识点"]').click()
        self.driver.find_element_by_css_selector('[id="knowledge-dialog-label"] > span:nth-child(1)').click()
        self.driver.find_element_by_xpath('//*[text()="去关联知识点"]').click()
        self.driver.find_element_by_css_selector(
            '#exercise-table-div > table > tbody > tr > td:nth-child(1) > label > span').click()
        self.driver.find_element_by_xpath('//*[text()="去关联知识点"]').click()
        self.driver.find_element_by_css_selector('[class="no-video-tip"] > a').click()
        time.sleep(1)
        Upload(self.driver).upload_file(filepath)
        success = self.driver.find_element_by_css_selector('[class="tl-related-video"] > a')
        while success.is_displayed():
            self.driver.find_element_by_id("back-exercise-list").click()
            break
        self.driver.find_element_by_css_selector('#moduleList > li:nth-child(5)').click()
        self.driver.find_element_by_id("use-system-tree").click()
        filepaths = Config_file.Local_filepaths
        for filepath in filepaths[0:5:1]:
            self.driver.find_element_by_id("uploadResourceBtn").click()
            time.sleep(1)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
        print("上传了图片、音频、视频、PDF、文档")
        for filepath in filepaths[5:6:1]:
            self.driver.find_element_by_id("pptUpload").click()
            time.sleep(1)
            Upload(self.driver).upload_file(filepath)
            time.sleep(1)
        print("上传了PPT")
        success = self.driver.find_element_by_xpath('//*[text()="当前共有6个相关资料"]')
        while success.is_displayed():
            print("全部上传成功")
            break

    def test_Beike(self):
        self.driver.find_element_by_id("courseware").click()
        self.driver.find_element_by_id("addNewCourseware").click()
        myCoursewaresubject_num = len(self.driver.find_elements_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span'))
        # myCoursewaresubject = random.randint(1, myCoursewaresubject_num)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[{}]'.format(myCoursewaresubject)).click()
        self.driver.find_element_by_xpath('//span[text()="历史"]').click()
        myCoursewareclass_num = len(self.driver.find_elements_by_xpath('//*[@id="classDiv"]/span'))
        myCoursewareclass = random.randint(1, myCoursewareclass_num)
        if myCoursewareclass_num > 1:
            self.driver.find_element_by_xpath('//*[@id="classDiv"]/span[{}]'.format(myCoursewareclass)).click()
        self.driver.find_element_by_id("coursewarName").send_keys("高中历史备课包")
        self.driver.find_element_by_class_name('upload-img-btn').click()
        filepath = Config_file.Local_filepaths[0]
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

    def test_Sucaiku(self):
        self.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()
        self.driver.find_element_by_id("material").click()
        Bullet = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]')
        if Bullet.is_displayed():
            print("有弹框")
            self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
        else:
            print("没有弹框")
        self.driver.find_element_by_xpath('//*[@id="h3-title-1"]/div[1]').click()
        # self.driver.find_element_by_xpath('//*[@id="myMaterialsubjectul"]/li[4]').click()
        # self.driver.find_element_by_xpath('//*[@id="gradeList"]/li[3]').click()
        myMaterialsubject_num = len(self.driver.find_elements_by_css_selector("#myMaterialsubjectul li"))
        myMaterialsubject = random.randint(1, myMaterialsubject_num)
        # 用{}占位在css中，format格式化随机数代入
        Materialsubject = self.driver.find_element_by_css_selector('#myMaterialsubjectul > li:nth-child({})'.format(myMaterialsubject))
        self.driver.execute_script("arguments[0].scrollIntoView();", Materialsubject)
        Materialsubject.click()
        myMaterialgrade_num = len(self.driver.find_elements_by_css_selector("#gradeList li"))
        myMaterialgrade = random.randint(1, myMaterialgrade_num)
        Materialgrade = self.driver.find_element_by_css_selector('#gradeList > li:nth-child({})'.format(myMaterialgrade))
        self.driver.execute_script("arguments[0].scrollIntoView();", Materialgrade)
        Materialgrade.click()
        time.sleep(2)
        filepaths = Config_file.Local_sck_filepaths
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

    def test_Fenzu(self):
        self.driver.find_element_by_xpath('//a[text()="智慧课堂"]').click()
        self.driver.find_element_by_id("class-squad-manage").click()
        allStudent = self.driver.find_element_by_id("allStudent").text
        students_num = re.sub(r'）.*', "", re.sub(r'.*（', "", allStudent))
        learnGrouplist_num = len(self.driver.find_elements_by_xpath("//*[@id='schemeUl']/li"))
        while learnGrouplist_num < 3:
            self.driver.find_element_by_xpath("//*[@id='squad-list-div']/div[1]/div/div[1]/button/i").click()
            learnGrouplist_num += 1
        # 添加分组
        Groups_num = len(self.driver.find_elements_by_xpath("//*[@id='schemeUl']/li[1]/ul/li"))
        while Groups_num < int(students_num) :
            self.driver.find_element_by_css_selector("#schemeUl > li:nth-child(1) > div:nth-child(1) > span:nth-child(4)").click()
            time.sleep(1)
            add_button = self.driver.find_element_by_xpath("//*[@id='schemeUl']/li[1]/ul[{}]/li/span[1]".format(Groups_num + 1))
            add_button.send_keys("{}".format(Groups_num+1))
            self.driver.find_element_by_xpath("//*[@id='schemeUl']/li[1]/ul[{}]/li/span[3]".format(Groups_num + 1)).click()
            Groups_num += 1
            time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()