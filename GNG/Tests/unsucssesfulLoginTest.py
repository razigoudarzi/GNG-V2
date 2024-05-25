from Pages.LoginClass import Login

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://172.31.0.156:4455/#/public/login")
driver.maximize_window()
sleep(5)

login_object = Login(driver=driver)

login_object.login_function('TotalSalesAdmin','1234567')

sleep(5)

driver.find_element(By.XPATH,"//h2/*")