#تست کیس لاگ اوت

from selenium import webdriver
from time import sleep
from Pages.Login import Login_Page
from Pages.log_out import Logout
import successfull_Tc
driver = webdriver.Chrome()
#driver.maximize_window()

url = "http://172.31.0.156:5529/#/public/login?returnUrl=/launcher/home"
#driver.get(url)
sleep(2)
#ساخت یک شی از کلاس Login_Page
#login_object = Login_Page(driver= driver)
#login_object.login('qcuser','Qc@123456')

#ساخت یک شی از کلاس Logout
logout_object = Logout(driver = driver)
logout_object.logout()
sleep(2)
#اسرشن url
assert driver.current_url==url

sleep(3)
