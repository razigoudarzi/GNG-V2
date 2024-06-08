#تست کیس بررسی خالی شدن فیلدها از دیتا با بازنشانی در فرم اعلام نیاز

from selenium import webdriver
from Pages.Login import Login_Page
from time import sleep
from Pages.filter import Filters


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://172.31.0.156:5529/")
#ساخت شی از کلاس login و فراخوانی متد آن
login_object = Login_Page(driver = driver)
login_object.login('qcuser','Qc@123456')

#ساخت شی از کلاس filters و فراخوانی متد آن
filter_object = Filters(driver = driver)
filter_object.remove_filter()
sleep(4)

