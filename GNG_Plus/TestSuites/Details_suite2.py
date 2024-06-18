import  unittest
from selenium import webdriver
from Pages.Login import Login_Page
from Pages.Details import Detials
from selenium.webdriver.common.by import By
from Locators import *
from time import sleep


class Details(unittest.TestCase):
    @classmethod
   # def setUpClass(cls):
    def setUp(self):
        self.driver = webdriver.Chrome(())
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # ساخت یک object از کلاس Login_page

        login_object = Login_Page(driver=self.driver)
        self.driver.get("http://172.31.0.156:5529/")
        login_object.login("Qcuser", "Qc@123456")



    def test_Detail_Tc(self):
        # ساخت یک object از کلاس Login_page
        #login_object = Login_Page(driver=self.driver)

        # ساخت یک object از کلاس Details
        details = Detials(driver=self.driver)

        # لود آدرس سیستم اعلام نیاز
        #self.driver.get("http://172.31.0.156:5529/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # صدا کردن متد login از کلاس Login_page
        #login_object.login("Qcuser", "Qc@123456")
        # sleep(8)

        self.driver.implicitly_wait(5)

        # کلیک روی سیستم اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR, request_title_link).click()

        # کلیک روی تنظیمات
        self.driver.find_element(By.CSS_SELECTOR, setting_link).click()

        # کلیک روی انواع اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR, request_types).click()

        # sleep(3)
        self.driver.implicitly_wait(5)

        # صدا کردن متد show_detail از کلاس Detail
        details.show_detail()

        sleep(3)






    def test_Edit_Tc(self):

        #self.driver.switch_to.new_window('tab')
        #self.driver.maximize_window()
        #self.driver.implicitly_wait(5)

        #login_object = Login_Page(driver=self.driver)
        detail = Detials(driver=self.driver)

        #self.driver.get("http://172.31.0.156:5529/")
       # self.driver.maximize_window()
        #self.driver.implicitly_wait(5)

        #login_object.login("qcuser", "Qc@123456")
        #self.driver.implicitly_wait(5)

        # کلیک روی سیستم اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR, request_title_link).click()

        # کلیک روی تنظیمات
        self.driver.find_element(By.CSS_SELECTOR, setting_link).click()

        # کلیک روی انواع اعلام نیاز
        self.driver.find_element(By.CSS_SELECTOR, request_types).click()

        self.driver.implicitly_wait(5)

        detail.edit_fields()

        sleep(5)

    @classmethod
    #def tearDownClass(cls):
    def tearDown(self):
       self.driver.close()
       self.driver.quit()





