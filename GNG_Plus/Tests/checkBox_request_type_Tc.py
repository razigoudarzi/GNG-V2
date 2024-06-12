#تست کیس بررسی فعال بودن چک باکس های طرف حساب اول و دوم در فرم انواع اعلام نیاز
from selenium import webdriver
from Pages.checkBox_request_type import CheckBox
from time import sleep
from Pages.Login import Login_Page
from selenium.webdriver.common.by import By
from Locators import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.31.0.156:5529/")
sleep(3)
#ساخت یک object از کلاس Login_Page
login_objct = Login_Page(driver = driver)
#ساخت یک object از کلاس CheckBox
check_box_object=CheckBox(driver = driver)
#لاگین در سیستم اعلام نیاز
login_objct.login('qcuser','Qc@123456')
sleep(1)
#کلیک روی لینک اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_title_link).click()
#کلیک روی تنظیمات
driver.find_element(By.CSS_SELECTOR,setting_link).click()
#کلیک روی انواع اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_types).click()

#فراخوانی متد insert_request جهت اضافه کردن نوع اعلام نیاز جدید
check_box_object.insert_request('GoudarziTest','واحد','مشتری')
#فراخوانی متد check_box
check_box_object.check_box()
#فراخوانی متد delete_request
check_box_object.delete_request()