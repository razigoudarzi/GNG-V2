from selenium.webdriver.common.by import By
from Locators import *
from selenium.webdriver.common.keys import Keys
from time import sleep
class Insert_request:
    def __init__(self,driver):
        self.driver = driver


    def insert_request(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, plus_button).click()
        self.driver.find_element(By.XPATH, product_group_xpath).click()
        self.driver.find_element(By.XPATH,select_request_xpath2).click()
        self.driver.find_element(By.XPATH,unit_xpath).click()
        self.driver.find_element(By.XPATH,select_request_xpath3).click()
        sleep(2)

        self.driver.find_element(By.XPATH,save_button_xpath).click()




    def importing(self):
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.CSS_SELECTOR,request_title_link).click()
        self.driver.find_element(By.XPATH,actions_xpath).click()
        self.driver.find_element(By.XPATH,request_xpath2).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,request_type_drop_down_xpath).click()
        #sleep(3)

        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH,select_request_xpath).click()
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH,search_button_xpath).click()





















