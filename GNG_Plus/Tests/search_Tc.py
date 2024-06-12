#تست کیس سرچ عنوان در فرم انواع اعلام نیاز
from selenium import webdriver
from Pages.search import Search
from Pages.Login import Login_Page
from time import sleep
from selenium.webdriver.common.by import By
from Locators import *


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://172.31.0.156:5529/")
#ساختن یک شی از کلاس Login_Page
login_object = Login_Page(driver = driver)

login_object.login('qcuser','Qc@123456')
sleep(2)
#کلیک روی اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_title_link).click()
#کلیک روی تنظیمات
driver.find_element(By.CSS_SELECTOR,setting_link).click()
#کلیک روی انواع اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_types).click()

#ساخت یک شی از کلاس Search
search_object = Search(driver = driver)
#فراخوانی متد search از کلاس Search
search_object.search('Goudarzi')

sleep(5)