#تست کیس لاگین ناموفق
from Pages.Login import Login_Page
from selenium import webdriver
from time import sleep
from Locators import *
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

#create an object form login class
login_object = Login_Page(driver = driver)

driver.get("http://172.31.0.156:5529/")
driver.implicitly_wait(5)

#call login function
login_object.login('qcuser','Qc@1234567')
sleep(2)

#check error box
driver.find_element(By.CSS_SELECTOR,dialog_box_css_selector)
