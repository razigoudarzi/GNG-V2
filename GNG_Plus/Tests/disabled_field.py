
#تست کیس مربوط به فعال و غیرفعال شدن یک فیلد در شرایط خاص
from selenium import webdriver
from Pages.Login import Login_Page
from Locators import *
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://172.31.0.156:5529/")
driver.maximize_window()

#ساخت یک object از کلاس لاگین
login_object = Login_Page(driver = driver)

#فراخوانی تابع لاگین از کلاس Login
login_object.login('qcuser','Qc@123456')


driver.implicitly_wait(5)
#کلیک روی سیستم اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_title_link).click()
#کلیک روی اقدامات
driver.find_element(By.XPATH,actions_xpath).click()
#کلیک روی فرم اعلام نیاز
driver.find_element(By.XPATH,request_xpath2).click()

sleep(5)

#assertion غیرفعال بودن دکمه ی جستجو
assert(driver.find_element(By.XPATH,search_button).get_attribute('ng-reflect-disabled')) == 'true'

#باز کردن دراپ داون انواع اعلام نیاز
driver.find_element(By.XPATH,request_type_drop_down_xpath).click()

#  انتخاب یک اعلام نیاز
driver.find_element(By.XPATH,check_box_xpath).click()

sleep(5)

#assertion  فعال بودن دکمه ی جستجو
assert(driver.find_element(By.XPATH,search_button).get_attribute('ng-reflect-disabled')) == 'false'

