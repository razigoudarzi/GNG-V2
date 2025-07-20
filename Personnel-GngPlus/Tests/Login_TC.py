from selenium import webdriver
from Pages.login_class import login_page
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

#آدرس پرسنلی
url =" http://172.31.0.156:1921/"

#ساخت یک آبجکت از کلاس لاگین
login_object =login_page(driver = driver)
driver.implicitly_wait(10)

#بازکردن url
driver.get(url)

#فراخوانی کلاس
login_object.login('adminhr','123!@#QWEasdzxc')

sleep(3)
