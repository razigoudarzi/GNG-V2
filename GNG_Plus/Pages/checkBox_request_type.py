#کلاس CheckBox - بررسی چک باکس های طرف حساب اول و دوم در فرم انواع اعلام نیاز
from Locators import *
from selenium.webdriver.common.by import By
from time import sleep

class CheckBox():
    def __init__(self,driver):
        self.driver = driver
#تابع ایجاد یک اعلام نیاز جدید
    def insert_request(self,title,partyname1,partyname2):
        #کلیک روی دکمه ی افزودن
        self.driver.find_element(By.XPATH,insert_button_xpath).click()
        #تایپ عنوان در فیلد عنوان اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR,request_title).send_keys(title)
        #تایپ نام طرف حساب اول در  فیلد عنوان طرف حساب 1
        self.driver.find_element(By.CSS_SELECTOR,party1_name_css_Selector).send_keys(partyname1)
        #فعال کردن تاگل طرف حساب 2 استفاده می شود
        self.driver.find_element(By.XPATH,party2_switch_on_xpath).click()
        #تایپ نام طرف حساب دوم در فیلد عنوان طرف حساب دوم
        self.driver.find_element(By.XPATH, party2_name_xpath).send_keys(partyname2)
        sleep(1)
        #کلیک روی دکمه ی ذخیره
        self.driver.find_element(By.CSS_SELECTOR,save_button).click()
        sleep(3)



#تابع check_box برای بررسی چک باکس ها
    def check_box(self):
        self.driver.implicitly_wait(5)
        #اسرشن اتریبیوت aria-checked مربوط به المنت چک باکس طرف حساب اول
        assert (self.driver.find_element(By.XPATH, check_box_party1_selected).get_attribute('aria-checked')) == 'true'
        # اسرشن اتریبیوت aria-checked مربوط به المنت چک باکس طرف حساب دوم
        assert (self.driver.find_element(By.XPATH, check_box_party2_selected).get_attribute('aria-checked')) == 'true'
        # اسرشن اتریبیوت aria-checked مربوط به المنت چک باکس طرف حساب سوم
        assert (self.driver.find_element(By.XPATH, check_box_party3_selected).get_attribute('aria-checked')) == 'false'
        sleep(2)
#حذف رکورد اضافه شده از لیست برای جلوگیری از خطای تکراری بودن عنوان در تست های بعدی
    def delete_request(self):
        self.driver.implicitly_wait(5)

        #پیدا کردن المنت سه نقطه کنار رکورد
        overflow_button_xpath = self.driver.find_element(By.XPATH,
                                                         "//div[@role = 'button'  and @aria-label = 'overflow'][1]")
        #کلیک روی سه نقطه
        self.driver.execute_script("arguments[0].click();", overflow_button_xpath)

        #کلیک روی گزینه ی حذف
        self.driver.find_element(By.XPATH,"(//div[@class = 'dx-item dx-list-item'])[2]").click()
        sleep(2)
        #کلیک روی گزینه ی بله
        self.driver.find_element(By.XPATH,"//div[@aria-label = 'بله']").click()

        sleep(2)






