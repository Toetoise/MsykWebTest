from selenium import webdriver
from selenium.webdriver import ActionChains
from autotest_msyk.Account_login import Login
from autotest_msyk.Upload_file import Upload
from autotest_msyk import Config_file
from homework.Tea_Homework import TeaHomework
from courseware.Courseware import Courseware
from material.Material import Material
import time
import unittest
import re
import warnings
# import pytest


class TestVisitMsykByEdge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        # driver_url = r"H:\Python38\msedgedriver.exe"
        # cls.driver = webdriver.Edge(executable_path=driver_url)
        cls.driver = webdriver.Chrome()
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

    def test_Homework(self):
        TeaHomework(self.driver).homework()

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
        filepath = Config_file.UN_filepaths[0]
        time.sleep(1)
        Upload(self.driver).upload_file(filepath)
        self.driver.find_element_by_id("textarea").send_keys("这是自动化测试_课程包的课程简介")
        self.driver.find_element_by_id("area").send_keys("这是自动化测试_课程包的课程详情")
        self.driver.find_element_by_id("saveCourseButton").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#moduleList > li:nth-child(2)').click()
        time.sleep(1)
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
        filepath = Config_file.UN_filepaths[6]
        time.sleep(1)
        Upload(self.driver).upload_file(filepath)
        self.driver.find_element_by_id("uploadFileList").click()
        success = self.driver.find_element_by_xpath('//*[text()="上传成功"]')
        while success.is_displayed():
            self.driver.find_element_by_class_name("layui-layer-ico").click()
            print("上传成功")
            break
        self.driver.find_element_by_id("js-go-exercise").click()
        time.sleep(1)
        self.driver.find_element_by_id("use-system-tree").click()
        check = self.driver.find_element_by_xpath('//*[text()="第一章 走近细胞"]')
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
        filepaths = Config_file.UN_filepaths
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
        Courseware(self.driver).courseware()

    def test_Sucaiku(self):
        Material(self.driver).material()

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
        # driver_url = r"H:\Python38\msedgedriver.exe"
        # cls.driver = webdriver.Edge(executable_path=driver_url)
        cls.driver = webdriver.Chrome()
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()