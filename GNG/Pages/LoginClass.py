from Locators import *
#from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
from selenium.webdriver.common.by import  By
class Login:
    def __init__(self,driver):
        self.driver = driver


    #create a function for login

    def login_function(self,username,password):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,user_text_box_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,pass_text_box_xpath).send_keys(password)
        self.driver.find_element(By.XPATH,login_button_xpath).click()






