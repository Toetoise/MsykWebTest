import time
from homework.Ordinary_homework import Ordinary
from homework.Reading_homework import Reading
from homework.Exam_homework import Exam
from homework.Sheet_homework import Sheet


class TeaHomework:
    def __init__(self, driver):
        self.driver = driver

    def homework(self):
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
