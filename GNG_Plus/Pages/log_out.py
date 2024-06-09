#کلاس لاگ اوت
from Locators import *
from selenium.webdriver.common.by import By
class Logout():

    def __init__(self,driver):
        self.driver = driver

    def logout(self):
        #کلیک روی آیکون امکانات کاربر
        self.driver.find_element(By.XPATH,user_icone_xpath).click()
        #کلیک روی آیکون خرج
        self.driver.find_element(By.XPATH,logout_icon_xpath).click()




        