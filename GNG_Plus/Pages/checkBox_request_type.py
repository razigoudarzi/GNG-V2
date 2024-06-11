from Locators import *
from selenium.webdriver.common.by import By
from time import sleep

class CheckBox():
    def __init__(self,driver):
        self.driver = driver

    def insert_request(self,title,partyname1,partyname2):
        self.driver.find_element(By.XPATH,insert_button_xpath).click()
        self.driver.find_element(By.CSS_SELECTOR,request_title).send_keys(title)
        self.driver.find_element(By.CSS_SELECTOR,party1_name_css_Selector).send_keys(partyname1)
        self.driver.find_element(By.XPATH,party2_switch_on_xpath).click()
        self.driver.find_element(By.XPATH, party2_name_xpath).send_keys(partyname2)
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,save_button).click()
        sleep(3)




    def check_box(self):
        self.driver.implicitly_wait(5)
        assert (self.driver.find_element(By.XPATH, check_box_party1_selected).get_attribute('aria-checked')) == 'true'
        assert (self.driver.find_element(By.XPATH, check_box_party2_selected).get_attribute('aria-checked')) == 'true'
        assert (self.driver.find_element(By.XPATH, check_box_party3_selected).get_attribute('aria-checked')) == 'false'
        sleep(2)

    def delete_request(self):
        self.driver.implicitly_wait(5)

       # self.driver.find_element(By.XPATH,"(//dx-drop-down-button)[1]").click()
        sleep(2)
        overflow_button_xpath = self.driver.find_element(By.XPATH,
                                                         "//div[@role = 'button'  and @aria-label = 'overflow'][1]")
        self.driver.execute_script("arguments[0].click();", overflow_button_xpath)

        self.driver.find_element(By.XPATH,"(//div[@class = 'dx-item dx-list-item'])[2]").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//div[@aria-label = 'بله']").click()

        sleep(2)






