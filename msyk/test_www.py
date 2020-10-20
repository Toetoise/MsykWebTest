from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType
from test_loginclass import Login
import time
# import unittest
import win32gui
import win32con
import random
import pytest


class Test_VisitMsykByEdge:
    def setUp(self):
        # driver_url = r"H:\Python38\msedgedriver.exe"
        self.driver = webdriver.Edge(executable_path=r"H:\Python38\msedgedriver.exe")
        self.driver.implicitly_wait(10)
        url = "https://httpswww.msyk.cn/"
        self.driver.get(url)
        self.driver.maximize_window()
        res = self.isElementPresent("xpath", '/html/body/div[2]/div/a[2]')
        if res is True:
            print("首页打开成功！")
        else:
            print("首页打开失败！")
        Login(self.driver).login("lusu", "12345678")

    # def test_Login(self):
    #     login(self.driver).login("lusu", "12345678")
    #     # 用户协议弹框
    #     # while True:
    #     #     try:
    #     #         Agreement = driver.find_element_by_xpath('//*[@id="layui-layer2"]')
    #     #         if Agreement.is_displayed():
    #     #             print("有弹框")
    #     #             driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()
    #     #             # time.sleep(1)
    #     #             continue
    #     #         else:
    #     #             print("没有弹框")
    #     #     except:
    #     #         break
    #     # loginSuccess = self.isElementPresent("id", "personalCenter")
    #     # if loginSuccess is True:
    #     #     print("登录成功！")
    #     # else:
    #     #     print("登录失败！")
    #     # time.sleep(2)

    def isElementPresent(self, by, value):
        from selenium.common.exceptions import NoSuchElementException
        try:
            element = self.driver.find_element(by=by, value=value)
        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True

    def test_Homework(self):
        self.driver.find_element_by_id("classAndGradeHomework").click()
        self.driver.find_element_by_xpath('//*[@id="classHomework"]').click()
        self.driver.find_element_by_id("addHomeworkButton").click()
        # 选择学科
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[1]').click()
        # 输入作业名称
        self.driver.find_element_by_id("homeworkName").send_keys("TEST_1")
        startTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        endTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() + 7200))
        print(startTime, endTime)
        # 设置起止时间
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[5]/div[1]/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[5]/div[2]/div/input').send_keys(Keys.CONTROL, "a")
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[5]/div[2]/div/input').send_keys(Keys.DELETE)
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[5]/div[2]/div/input').send_keys(endTime)
        # 选择作业范围
        self.driver.find_element_by_xpath('//*[@id="class-squad"]/div/div[1]/span').click()
        self.driver.find_element_by_id("submitCourseware").click()
        # 添加微课
        self.driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div/div[2]/div/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="569"]/a/span[1]').click()
        self.driver.find_element_by_class_name("btn").click()
        # 添加习题
        self.driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div/div[3]/div[1]/button[3]').click()
        exercise_table = self.driver.find_element_by_xpath('//*[@id="containerDiv"]/div[1]/div[2]/table')
        rows = len(exercise_table.find_elements_by_tag_name('tr'))
        print(rows)

    def test_Kecheng(self):
        self.driver.find_element_by_class_name('courseCenter').click()
        self.driver.find_element_by_css_selector('#newCourseBtn').click()

    def test_Beike(self):
        def upload_file(filePath):
            dialog = win32gui.FindWindow("#32770", "打开")
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            combox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
            edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
            button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

        self.driver.find_element_by_id("courseware").click()
        self.driver.find_element_by_id("addNewCourseware").click()
        myCoursewaresubject_num = len(
            self.driver.find_elements_by_xpath('//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span'))
        myCoursewaresubject = random.randint(1, myCoursewaresubject_num)
        self.driver.find_element_by_xpath(
            '//*[@id="main-container"]/div/div/div/div[2]/div/div[1]/div/div/span[{}]'.format(
                myCoursewaresubject)).click()
        myCoursewareclass_num = len(self.driver.find_elements_by_xpath('//*[@id="classDiv"]/span'))
        myCoursewareclass = random.randint(1, myCoursewareclass_num)
        if myCoursewareclass_num > 1:
            self.driver.find_element_by_xpath('//*[@id="classDiv"]/span[{}]'.format(myCoursewareclass)).click()
        self.driver.find_element_by_id("coursewarName").send_keys("高中英语备课包")
        self.driver.find_element_by_class_name('upload-img-btn').click()
        filepath = r"D:\BAK_JF\WP\素材\picture\jpg\01.jpg"
        upload_file(filepath)
        self.driver.find_element_by_id("submitCourseware").click()
        self.driver.find_element_by_class_name("js-addNavItem").click()
        self.driver.find_element_by_xpath('//*[@id="navCourse"]/li[last()-1]').click()
        self.driver.find_element_by_xpath('//*[@id="filter-type"]/ul/li[1]/a').click()
        check = self.driver.find_element_by_xpath('//*[@id="containerDiv"]/div[1]/div/ul/li[1]/a/div/img')
        ActionChains(self.driver).move_to_element(check).perform()
        self.driver.find_element_by_xpath('//*[@id="containerDiv"]/div[1]/div/ul/li[1]/a/span/i').click()
        self.driver.find_element_by_class_name("topbar-buttons").click()

    def test_Sucaiku(self):
        # login(self.driver).login("lusu", "12345678")
        self.driver.find_element_by_id("material").click()
        while True:
            try:
                Bullet = driver.find_element_by_xpath('//*[@id="layui-layer1"]')
                if Bullet.is_displayed():
                    print("有弹框")
                    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
                    continue
                else:
                    print("没有弹框")
            except:
                break
        self.driver.find_element_by_xpath('//*[@id="h3-title-1"]/div[1]').click()
        # self.driver.find_element_by_xpath('//*[@id="myMaterialsubjectul"]/li[4]').click()
        # self.driver.find_element_by_xpath('//*[@id="gradeList"]/li[3]').click()
        myMaterialsubject_num = len(self.driver.find_elements_by_css_selector("#myMaterialsubjectul li"))
        myMaterialsubject = random.randint(1, myMaterialsubject_num)
        # 用{}占位在css中，format格式化随机数代入
        self.driver.find_element_by_css_selector(
            '#myMaterialsubjectul > li:nth-child({})'.format(myMaterialsubject)).click()
        myMaterialgrade_num = len(self.driver.find_elements_by_css_selector("#gradeList li"))
        myMaterialgrade = random.randint(1, myMaterialgrade_num)
        self.driver.find_element_by_css_selector('#gradeList > li:nth-child({})'.format(myMaterialgrade)).click()
        time.sleep(2)

        def upload_file(filePath):
            dialog = win32gui.FindWindow("#32770", "打开")
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            combox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
            edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
            button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

        filepaths = [r'D:\BAK_JF\WP\素材\picture\jpg\01.jpg', r'D:\BAK_JF\WP\素材\音频\different\林俊杰 - 将故事写成我们.mp3',
                     r'D:\BAK_JF\WP\素材\视频\NASA打造太空GPS导航_标清.mp4', r'D:\BAK_JF\WP\素材\PDF\真\P0209C-数学理(1).pdf',
                     r'D:\BAK_JF\WP\素材\ppt\模板19.pptx', r'D:\BAK_JF\WP\素材\ppt\模板27.pptx',
                     r'D:\BAK_JF\WP\素材\ppt\各种字体.pptx', r'D:\BAK_JF\WP\素材\ppt\优质.pptx',
                     r'D:\BAK_JF\WP\素材\题目\综合5-单、多、填、解.docx', r'D:\BAK_JF\WP\素材\文档\2017年高中物理：电学实验.docx']
        for filepath in filepaths[0:4:1]:
            self.driver.find_element_by_xpath('//*[@id="file-upload"]').click()
            time.sleep(1)
            print(filepath)
            upload_file(filepath)
            time.sleep(1)
        print("上传了图片、音频、视频、PDF")
        for filepath in filepaths[4:6:1]:
            self.driver.find_element_by_css_selector('#all-ppt-upload > a').click()
            self.driver.find_element_by_xpath('//*[@id="ppt-upload-local"]').click()
            time.sleep(1)
            print(filepath)
            upload_file(filepath)
            time.sleep(1)
        print("快速上传了ppt")
        for filepath in filepaths[6:8:1]:
            self.driver.find_element_by_css_selector('#all-ppt-upload > a').click()
            self.driver.find_element_by_xpath('//*[@id="ppt-hight-upload"]').click()
            time.sleep(1)
            print(filepath)
            upload_file(filepath)
            time.sleep(1)
        print("优质上传了ppt")
        self.driver.find_element_by_css_selector('#all-ques-upload > a').click()
        self.driver.find_element_by_xpath('//*[@id="question-upload"]').click()
        time.sleep(1)
        print(filepaths[8])
        upload_file(filepaths[8])
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="word-upload"]').click()
        time.sleep(1)
        print(filepaths[9])
        upload_file(filepaths[9])
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="newFolder"]').click()
        self.driver.find_element_by_xpath('//*[@id="newFolderTr"]/td[2]/span/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="newFolder"]').click()
        self.driver.find_element_by_xpath('//*[@id="newFolderName"]').send_keys("TEST1")
        self.driver.find_element_by_xpath('//*[@id="newFolderTr"]/td[2]/span/a[2]').click()
        self.driver.find_element_by_css_selector('#sidebar > div > ul > li:nth-child(3) > a').click()
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

    def tearDown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
