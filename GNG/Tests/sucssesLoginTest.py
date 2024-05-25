from Pages.LoginClass import Login
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://172.31.0.156:4455/#/public/login")
sleep(5)

url = "http://172.31.0.156:4455/#/launcher/home"

# create an object from Login Class
login_object= Login(driver = driver)

login_object.login_function('TotalSalesAdmin','123456')
sleep(5)

assert  driver.current_url == url