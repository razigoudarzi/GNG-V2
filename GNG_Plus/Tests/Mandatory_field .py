from Pages.Login import Login_Page
from selenium  import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from Locators import *


# تست اجباری بودن دو فیلد عنوان اعلام نیاز و عنوان طرف حساب در فرم انواع اعلام نیاز

driver = webdriver.Chrome()
driver.maximize_window()
#باز کردن پورت سیستم اعلام نیاز
driver.get("http://172.31.0.156:5529/")
sleep(5)

#ساخت آبجکت از کلاس لاگین
login_object = Login_Page(driver = driver)
#لاگین در سیستم اعلام نیاز
login_object.login('qcuser','Qc@123456')


driver.implicitly_wait(5)
#کلیک روی لینک اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_title_link).click()

#کلیک روی لینک تنظیمات
driver.find_element(By.CSS_SELECTOR,setting_link).click()

#کلیک روی انواع اعلام نیاز
driver.find_element(By.CSS_SELECTOR,request_types).click()

#کلیک روی دکمه ی +
driver.find_element(By.XPATH,plus_button).click()
sleep(2)

#بررسی none بودن اتریبیوت فیلد عنوان اعلام نیاز
print(driver.find_element(By.CSS_SELECTOR,request_title).get_attribute('aria-invalid'))
assert (driver.find_element(By.CSS_SELECTOR,request_title)).get_attribute('aria-invalid')==None

#بررسی none بودن اتریبیوت فیلد عنوان طرف حساب
print(driver.find_element(By.CSS_SELECTOR,party_title).get_attribute('aria-invalid'))
assert (driver.find_element(By.CSS_SELECTOR,party_title)).get_attribute('aria-invalid')==None


#  کلیک روی دکمه ی ثبت
driver.find_element(By.CSS_SELECTOR, "div[aria-label='ثبت']").click()
sleep(5)

#بررسی true  شدن اتریبیوت فیلد عنوان اعلام نیاز
print(driver.find_element(By.CSS_SELECTOR,request_title).get_attribute('aria-invalid'))
assert (driver.find_element(By.CSS_SELECTOR,request_title)).get_attribute('aria-invalid')=='true'

#بررسی true شدن اتریبیوت فیلد عنوان طرف حساب
print(driver.find_element(By.CSS_SELECTOR,party_title).get_attribute('aria-invalid'))
assert (driver.find_element(By.CSS_SELECTOR,party_title)).get_attribute('aria-invalid')=='true'






