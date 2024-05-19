
from selenium.webdriver.common.by import By
from Locators import *
from time import sleep


#کلاس Details برای بررسی نمایش جزئیات و ویرایش یک رکورد
class Detials:
    def __init__(self,driver):
        self.driver =  driver


    #تابع show_detail  برای بررسی غیرقابل ویرایش بودن فیلدهای یک رکورد
    def show_detail(self):
        self.driver.implicitly_wait(8)

    #کلیک روی سه نقطه ی کنار رکود و استفاده از دستور جاوااسکریپتی execute_script
        overflow_button_xpath = self.driver.find_element(By.XPATH, "//div[@role = 'button'  and @aria-label = 'overflow'][1]")
        self.driver.execute_script("arguments[0].click();", overflow_button_xpath)

    #کلیک روی آیتم نمایش جزئیات
        self.driver.find_element(By.XPATH,detail_xpath).click()

        sleep(1)
    #بررسی اتریبیوت مربوطه برای فیلدهای فرم در حالت نمایش جزئیات
        assert (self.driver.find_element(By.CSS_SELECTOR,party2_Css_selector).get_attribute('aria-readonly')) =='true'
        assert (self.driver.find_element(By.CSS_SELECTOR,party3_Css_Selector).get_attribute('aria-readonly')) == 'true'

    #بستن فرم نمایش  جزئیات
        self.driver.find_element(By.XPATH,ignore_button_xpath).click()

        sleep(5)
    #تابع edit_fields برای بررسی قابل ویرایش بودن فیدلهای فرم در حالت ویرایش
    def edit_fields(self):
        self.driver.implicitly_wait(8)

        # کلیک روی سه نقطه ی کنار رکود و استفاده از دستور جاوااسکریپتی execute_script
        overflow_button_xpath = self.driver.find_element(By.XPATH,"//div[@role = 'button'  and @aria-label = 'overflow'][1]")
        self.driver.execute_script("arguments[0].click();",overflow_button_xpath)

        # کلیک روی آیتم ویرایش
        self.driver.find_element(By.XPATH,edit_button_xpath).click()

        sleep(1)

        # بررسی اتریبیوت مربوطه برای فیلدهای فرم در حالت ویرایش
        assert (self.driver.find_element(By.CSS_SELECTOR, party2_Css_selector).get_attribute('aria-readonly')) == None
        assert (self.driver.find_element(By.CSS_SELECTOR, party3_Css_Selector).get_attribute('aria-readonly')) == None

        #بستن فرم ویرایش
        self.driver.find_element(By.XPATH, ignore_button_xpath).click()

        sleep(5)







