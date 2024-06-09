#کلاس سرچ یک نوع اعلام نیاز در فرم انواع اعلام نیاز
from  Locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
class Search():
    def __init__(self,driver):
        self.driver = driver

#تابع سرچ : یک عنوان را سرچ می کند و بعد عنوان رکورد را با مقدار سرچ شده تطبیق می دهد .
    def search(self,text):
        self.driver.implicitly_wait(5)
        #سرچ text مورد نظر در فست فیلتر
        self.driver.find_element(By.CSS_SELECTOR,search_input_css_selector).send_keys(text)
        #استفاده از کلاس Enter جهت نمایش خروجی
        self.driver.find_element(By.CSS_SELECTOR,search_input_css_selector).send_keys(Keys.ENTER)

        sleep(2)
    # اسرشن رکورد خروجی با تکست سرچ شده
        assert(self.driver.find_element(By.CSS_SELECTOR,".dx-datagrid-search-text").text)==text



