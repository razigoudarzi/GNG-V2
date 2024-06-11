#تست کیس مربوط به غیرقابل ویرایش بودن فیلدهای فرم در حالت نمایش جزئیات- فرم انواع اعلام نیاز

from selenium import  webdriver
from Pages.Details import Detials
from Pages.Login import  Login_Page
from time import  sleep
from selenium.webdriver.common.by import By
from Locators import *

driver = webdriver.Chrome()
#ساخت یک object از کلاس Login_page
login_object = Login_Page(driver = driver)

#ساخت یک object از کلاس Details
details = Detials(driver = driver)

#لود آدرس سیستم اعلام نیاز
driver.get("http://172.31.0.156:5529/")
#sleep(15)
driver.implicitly_wait(5)
driver.maximize_window()

# صدا کردن متد login از کلاس Login_page
login_object.login("Qcuser","Qc@123456")
#sleep(8)

driver.implicitly_wait(5)

#کلیک روی سیستم اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_title_link).click()

#کلیک روی تنظیمات
driver.find_element(By.CSS_SELECTOR,setting_link).click()

#کلیک روی انواع اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_types).click()

#sleep(3)
driver.implicitly_wait(5)

#صدا کردن متد show_detail از کلاس Detail
details.show_detail()

sleep(3)

