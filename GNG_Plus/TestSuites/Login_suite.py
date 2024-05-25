import  unittest
from selenium import webdriver
from Pages.Login import Login_Page
from time import  sleep
from Locators import *
from selenium.webdriver.common.by import By

#ایجاد کلاس برای اجرا کردن تست ها با فریم ورک unittest
class Login_Test_Suite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

#تست کیس مربوط به لاگین موفق
    def test1_successfull_login(self):
        self.driver.implicitly_wait(5)
        url = "http://172.31.0.156:5529/#/launcher/home"
        login_object = Login_Page(driver=self.driver)
        self.driver.get("http://172.31.0.156:5529/")
        login_object.login('qcuser','Qc@123456')
        sleep(3)
        assert self.driver.current_url == url
        #self.driver.quit()
        #self.driver.close()

# تست کیس مربوط به لاگین ناموفق
    def test3_unsucces_login(self):
        self.driver.switch_to.new_window('tab')
        login_object = Login_Page(driver = self.driver)
        self.driver.get("http://172.31.0.156:5529/")
        self.driver.implicitly_wait(5)
        login_object.login('qcuser','Qc@123457')
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, dialog_box_css_selector)
        #self.driver.quit()
        #self.driver.close()

#تست کیس مربوط به فیلدهای اجباری
    def test2_required_fields(self):
        self.driver.switch_to.new_window('tab')

        login_object = Login_Page(driver = self.driver)
        self.driver.get("http://172.31.0.156:5529/")
        self.driver.implicitly_wait(8)

        login_object.login('qcuser','Qc@123456')
        sleep(3)
        # کلیک روی لینک اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR, request_title_link).click()
        # کلیک روی لینک تنظیمات
        self.driver.find_element(By.CSS_SELECTOR, setting_link).click()

        # کلیک روی انواع اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR, request_types).click()

        # کلیک روی دکمه ی +
        self.driver.find_element(By.XPATH, plus_button).click()
        sleep(2)

        # بررسی none بودن اتریبیوت فیلد عنوان اعلام نیاز
        print(self.driver.find_element(By.CSS_SELECTOR, request_title).get_attribute('aria-invalid'))
        assert (self.driver.find_element(By.CSS_SELECTOR, request_title)).get_attribute('aria-invalid') == None

        # بررسی none بودن اتریبیوت فیلد عنوان طرف حساب
        print(self.driver.find_element(By.CSS_SELECTOR, party_title).get_attribute('aria-invalid'))
        assert (self.driver.find_element(By.CSS_SELECTOR, party_title)).get_attribute('aria-invalid') == None

        #  کلیک روی دکمه ی ثبت
        self.driver.find_element(By.CSS_SELECTOR, "div[aria-label='ثبت']").click()
        sleep(5)

        # بررسی true  شدن اتریبیوت فیلد عنوان اعلام نیاز
        print(self.driver.find_element(By.CSS_SELECTOR, request_title).get_attribute('aria-invalid'))
        assert (self.driver.find_element(By.CSS_SELECTOR, request_title)).get_attribute('aria-invalid') == 'true'

        # بررسی true شدن اتریبیوت فیلد عنوان طرف حساب
        print(self.driver.find_element(By.CSS_SELECTOR, party_title).get_attribute('aria-invalid'))
        assert (self.driver.find_element(By.CSS_SELECTOR, party_title)).get_attribute('aria-invalid') == 'true'
        #self.driver.quit()
        #self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

