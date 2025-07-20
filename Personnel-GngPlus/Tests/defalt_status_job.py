import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import *
from Pages.login_class import login_page

    #def test_status_toggle_default(self,driver):
    #self.driver = driver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("http://172.31.0.156:1921/")
login_object = login_page(driver)
login_object.login('adminhr','123!@#QWEasdzxc')

time.sleep(3)
#driver.get("http://172.31.0.156:1921/#/hr/job/jobHeaderV2")
# مسیر‌یابی به فرم افزودن شغل
driver.find_element(By.CSS_SELECTOR, personnel_link_css_selector).click()
driver.find_element(By.CSS_SELECTOR, jobs_info_css_selector).click()
driver.find_element(By.CSS_SELECTOR, job_css_selctor).click()

# کلیک روی دکمه افزودن
wait.until(EC.element_to_be_clickable((By.XPATH, plus_button))).click()

# صبر برای نمایش پاپ‌آپ
toggle_element = wait.until(
     EC.visibility_of_element_located((By.XPATH, "//dx-switch[@role = 'button']"))
    )

# بررسی مقدار پیش‌فرض تاگل
toggle_status = toggle_element.get_attribute("aria-pressed")
assert toggle_status == "true", f"Toggle is not active by default. Current value: {toggle_status}"

print("✅ Toggle is active by default.")


