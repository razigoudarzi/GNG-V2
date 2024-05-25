from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators import *
from time import sleep
from selenium.webdriver.common.action_chains import  ActionChains

#driver = webdriver.Chrome()
class Patry:
    def __init__(self,driver):
        self.driver = driver

    #function for inserting party
    def insert_party(self,national_code,first_name,last_name,user_code):
        self.driver.implicitly_wait(4)

        self.driver.find_element(By.XPATH,plus_button_xpath).click()
        self.driver.find_element(By.XPATH,national_code_xpath).send_keys(national_code)
        self.driver.find_element(By.XPATH,check_button_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH,first_name_xpath).send_keys(first_name)
        self.driver.find_element(By.XPATH,last_name_xpath).send_keys(last_name)
        self.driver.find_element(By.XPATH,user_code_xpath).send_keys(user_code)
        self.driver.find_element(By.XPATH,continue_button_xpath).click()

    #function for converting text to intiger
    def output_row_number(self,mytext,index1,index2):

        return mytext[index1:index2]

    #function for deleting party
    def delete_party(self):
         self.driver.implicitly_wait(15)
        # sleep(5)
         self.driver.find_element(By.XPATH,record_click_xpath).click()

         self.driver.find_element(By.XPATH, delete_button_xpath).click()

         self.driver.find_element(By.XPATH, save_button_xpath).click()



