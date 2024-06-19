import  unittest
from selenium import webdriver
from Pages.Login import Login_Page
from Pages.Details import Detials
from selenium.webdriver.common.by import By
from Locators import *
from time import sleep


class Details(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        # ساخت یک object از کلاس Login_page
        login_object = Login_Page(driver=cls.driver)
        cls.driver.get("http://172.31.0.156:5529/")
        # صدا کردن متد login از کلاس Login_page
        login_object.login("Qcuser", "Qc@123456")

        # کلیک روی سیستم اعلام نیاز
        cls.driver.find_element(By.CSS_SELECTOR, request_title_link).click()

        # کلیک روی تنظیمات
        cls.driver.find_element(By.CSS_SELECTOR, setting_link).click()

        # کلیک روی انواع اعلام نیاز
        cls.driver.find_element(By.CSS_SELECTOR, request_types).click()


    def test_Detail_Tc(self):

        details = Detials(driver=self.driver)

        self.driver.implicitly_wait(5)

        # صدا کردن متد show_detail از کلاس Detail
        details.show_detail()

        sleep(3)

    def test_Edit_Tc(self):


         detail = Detials(driver=self.driver)

         self.driver.implicitly_wait(5)

         detail.edit_fields()

         sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()





