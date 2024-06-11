#تست کیس لاگین موفق
from Pages.Login import Login_Page
from selenium import webdriver
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window()

url = "http://172.31.0.156:5529/#/launcher/home"

#crate an object form login class
login_object = Login_Page(driver = driver)
driver.implicitly_wait(10)

#navigate to mainpage
driver.get("http://172.31.0.156:5529/")

#calling login function
login_object.login('qcuser','Qc@123456')
sleep(3)

assert  driver.current_url == url
