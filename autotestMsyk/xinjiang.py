from selenium import webdriver
import time
import win32gui
import win32con
import pytest
import allure
import  os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver_url = r"H:\Python38\msedgedriver.exe"
driver = webdriver.Edge(executable_path=driver_url)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(r"http://estudyxj.st.tst/")     #打开首页
driver.find_element_by_css_selector("#header-con > div.warp-header > div > ul > li.login > a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]").click()
driver.find_element_by_id("userName").send_keys("13679138183")
driver.find_element_by_id("userSecret").send_keys("123456a")
driver.find_element_by_css_selector(".btn-login-form > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)").click()
time.sleep(2)
abd=driver.find_element_by_css_selector("img.user-m:nth-child(2)")
ActionChains(driver).move_to_element(abd).perform()
driver.find_element_by_css_selector(".m-header_dropdown > li:nth-child(1)").click()
time.sleep(2)
driver.find_element_by_css_selector(".user-tabs-content > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(2)").click()
driver.execute_script("window.scrollBy(0,6000)")
time.sleep(2)
driver.find_element_by_css_selector(".ant-btn-primary").click()
time.sleep(2)

def upload_file(filepath):
    dialog = win32gui.FindWindow("#32770", "打开")
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    combox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

filepaths = [r"C:\Users\Tortoise\Desktop\3\1.pdf",r"C:\Users\Tortoise\Desktop\3\2.pdf",r"C:\Users\Tortoise\Desktop\3\3.pdf",r"C:\Users\Tortoise\Desktop\3\4.pdf"]
i=0
while i < 101:
    for filepath in filepaths[0:4:1]:
        driver.find_element_by_css_selector('.upload').click()
        time.sleep(1)
        print(filepath)
        upload_file(filepath)
        time.sleep(1)
    i = i+1
print("上传了图片、音频、视频、PDF")


