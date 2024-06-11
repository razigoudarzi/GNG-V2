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
login_objct = Login_Page(driver = driver)
check_box_object=CheckBox(driver = driver)
login_objct.login('qcuser','Qc@123456')
sleep(1)

driver.find_element(By.CSS_SELECTOR,request_title_link).click()
driver.find_element(By.CSS_SELECTOR,setting_link).click()
driver.find_element(By.CSS_SELECTOR,request_types).click()

check_box_object.insert_request('GoudarziTest','واحد','مشتری')
check_box_object.check_box()
check_box_object.delete_request()