from selenium import webdriver
from Pages.Login import  Login_Page
from Pages.Details import Detials
from selenium.webdriver.common.by import By
from Locators import *
from time import sleep

driver = webdriver.Chrome()


driver.maximize_window()
driver.implicitly_wait(5)

login_object=Login_Page(driver = driver)
detail = Detials(driver = driver)

driver.get("http://172.31.0.156:5529/")
driver.maximize_window()
driver.implicitly_wait(5)

login_object.login("qcuser","Qc@123456")
driver.implicitly_wait(5)


#کلیک روی سیستم اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_title_link).click()

#کلیک روی تنظیمات
driver.find_element(By.CSS_SELECTOR,setting_link).click()

#کلیک روی انواع اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_types).click()

driver.implicitly_wait(5)

detail.edit_fields()

sleep(5)