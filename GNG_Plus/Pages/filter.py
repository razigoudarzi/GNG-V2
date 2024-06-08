#کلاس Filters برای تست خالی شدن دیتای فیلدها با بازنشانی تنظیمات - فرم اعلام نیاز

from Locators import *
from selenium.webdriver.common.by import By
from time import sleep
class Filters:
    def __init__(self,driver):
        self.driver = driver

    def remove_filter(self):
        self.driver.implicitly_wait(5)
        #کلیک روی اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR,request_title_link).click()
        #کلیک روی اقدامات
        self.driver.find_element(By.XPATH,actions_xpath).click()
        #کلیک روی اعلام نیاز
        self.driver.find_element(By.XPATH,request_xpath2).click()
        #کلیک روی نوع اعلام نیاز
        self.driver.find_element(By.XPATH,request_type_drop_down_xpath).click()
        # انتخاب اولین نوع اعلام نیاز
        self.driver.find_element(By.XPATH,"(//div[@aria-label='انتخاب ردیف'])[1]").click()
        sleep(3)
        #اسرشن یک اتریبیوت بعد  از انتخاب نوع اعلام نیاز
        assert (self.driver.find_element(By.XPATH,
                                         "(//input[@aria-autocomplete = 'list' and @type = 'text'])[2]").get_attribute(
            'aria-invalid')) == None

        #کلیک روی بازنشانی فیلتر
        self.driver.find_element(By.XPATH,refresh_field_xpath).click()
        sleep(3)
        #اسرشن یک اتریبیوت بعد از بازنشانی فیلتر
        assert(self.driver.find_element(By.XPATH,"(//input[@aria-autocomplete = 'list' and @type = 'text'])[2]").get_attribute('aria-invalid'))== 'true'



