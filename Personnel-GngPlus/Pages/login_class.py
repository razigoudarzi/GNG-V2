from Locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login_page:
    def __init__(self,driver):
        self.driver = driver


    def login(self,username,password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR,username_box_css_selector).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,password_box_css_selector).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,login_button_css_slector).click()

        personnel_link_css_selector = (By.CSS_SELECTOR, "li[aria-label='پرسنلی']")
        element = WebDriverWait(self.driver,15).until(
            EC.visibility_of_element_located(personnel_link_css_selector)
        )



