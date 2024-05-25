from Pages.LoginClass import Login
from selenium import  webdriver
from Locators import  parent_element_xpath,logout_button_xpath
from selenium.webdriver.common.by import By
from time import  sleep


url = "http://172.31.0.156:4455/#/public/login"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

logout_object = Login(driver = driver)

logout_object.login_function('TotalSalesAdmin','123456')
#sleep(5)

driver.find_element(By.XPATH,parent_element_xpath).click()
driver.find_element(By.XPATH,logout_button_xpath).click()
sleep(2)
assert  driver.current_url == url

