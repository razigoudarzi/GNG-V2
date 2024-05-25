from selenium import webdriver

from Pages.LoginClass import Login
from Pages.party_class import Patry
from Locators import *
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class Party_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_delete_party(self):
        self.driver.get("http://172.31.0.156:4326/#/master/general/party")

        # create objects from Login adn Party Calss
        login_object = Login(driver=self.driver)
        party_object = Patry(driver=self.driver)

        # login
        login_object.login_function('TotalSalesAdmin', '123456')
        self.driver.implicitly_wait(5)

        # click on partyLink
        self.driver.find_element(By.LINK_TEXT, party_link_LinkText).click()
        self.driver.implicitly_wait(2)

        # store the text of paging
        my_text1 = self.driver.find_element(By.XPATH, paging_xpath).text
        row_number1 = int(party_object.output_row_number(my_text1, 10, 15))

        # insert a party
        party_object.insert_party('8714007126', 'علی', 'گودرزی', '14030208')
        sleep(5)
        self.driver.implicitly_wait(2)

        # store the text of paging after inserting party
        my_text2 = self.driver.find_element(By.XPATH, paging_xpath).text

        # convert my_text1 to intiger and split a part or its charector
        row_number2 = int(party_object.output_row_number(my_text2, 10, 15))

        assert row_number2 == row_number1 + 1
        print('Party inserted')

        sleep(5)
        # deleting inserted party
        if row_number2 == row_number1 + 1:

            party_object.delete_party()
            sleep(5)
            print('party deleted')
        else:
            print(row_number2)

        my_text3 = self.driver.find_element(By.XPATH, paging_xpath).text
        row_number3 = int(party_object.output_row_number(my_text3, 10, 15))
        print(row_number3)
        assert row_number1 == row_number3
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
