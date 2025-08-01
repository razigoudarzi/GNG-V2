import time

import self

from Locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class Adding_job :

    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def add_job(self,job_number,job_title):

        self.driver.find_element(By.CSS_SELECTOR,personnel_link_css_selector).click()  #کلیک روی لینک پرسنلی
        self.driver.find_element(By.CSS_SELECTOR,jobs_info_css_selector).click()      #کلیک روی اطلاعات پایه مشاغل
        self.driver.find_element(By.CSS_SELECTOR,job_css_selctor).click()           #کلیک روی شغل


        self.driver.find_element(By.XPATH,plus_button).click()

        time.sleep(1)

       #فیلد کد شغل
        self.driver.find_element(By.CSS_SELECTOR,job_code).send_keys(job_number)
       #فیلد عنوان شغل

        self.driver.find_element(By.CSS_SELECTOR,job_name).send_keys(job_title)
        #رسته شغلی
        self.driver.find_element(By.XPATH,job_drop_down).click()
        #time.sleep(1)

        self.driver.find_element(By.XPATH,Job_type).click()
        #time.sleep(1)

        #شغل معادل بیمه
        self.driver.find_element(By.XPATH,job_bime_drop_down).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,job_bime).click()
        time.sleep(1)
        #نوع شغل بیمه
        self.driver.find_element(By.XPATH,job_type1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,job_type1_option1).click()
        time.sleep(1)


         #دکمه ثبت
        self.driver.find_element(By.XPATH,submit).click()

        time.sleep(3)

    def delete_job_by_code(self, code):
        """
        حذف شغل از گرید با استفاده از کد شغل
        """

        # --- مرحله 1: سرچ کردن کد شغل ---
        # صبر تا فیلتر کد شغل لود شود
        filter_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,job_code_filter))
        )

        # پاک کردن فیلد فیلتر قبلی
        filter_input.clear()

        # وارد کردن کد شغل
        filter_input.send_keys(code)

        # زدن کلید Enter برای سرچ
        filter_input.send_keys(Keys.ENTER)

        time.sleep(1)


        actions = ActionChains(self.driver)
        delete_button = self.driver.find_element(By.XPATH,"//tr[td[normalize-space()='140429']]//a[@aria-label='حذف']")

        # --- مرحله 3: تأیید حذف ---
        actions.move_to_element(delete_button).click().perform()

        confirm_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, confirm_button))
        )
        confirm_btn.click()

        # پاک کردن فیلد فیلتر قبلی
        filter_input.clear()
        time.sleep(1)
        # وارد کردن کد شغل
        filter_input.send_keys(code)

        # زدن کلید Enter برای سرچ
        filter_input.send_keys(Keys.ENTER)

        no_data_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "dx-datagrid-nodata"))
        )
        assert no_data_element.is_displayed()





