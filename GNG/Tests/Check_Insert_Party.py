from Pages.party_class import Patry
from selenium import webdriver
from time import sleep
from Pages.LoginClass import Login
from selenium.webdriver.common.by import By
from Locators import *

driver = webdriver.Chrome()
driver.get("http://172.31.0.156:4326/#/master/general/party")
#sleep(2)
driver.implicitly_wait(2)

# create object from Login and party classes

login_object = Login(driver=driver)
party_object = Patry(driver=driver)

login_object.login_function('TotalSalesAdmin', '123456')

driver.maximize_window()
#sleep(10)
driver.implicitly_wait(10)

# click on party link and open party form
driver.find_element(By.LINK_TEXT, party_link_LinkText).click()

# store paging text
my_text1 = driver.find_element(By.XPATH, paging_xpath).text

# convert text to intiger and split a part of its charector
row_number1 = int(party_object.output_row_number(my_text1, 10, 15))
print(row_number1)

# insert a party
party_object.insert_party('8714007126', 'علی', 'گودرزی', '14030208')
sleep(3)


my_text2 = driver.find_element(By.XPATH, paging_xpath).text
row_number2 = int(party_object.output_row_number(my_text2, 10, 15))
print(row_number2)

if  row_number2 == row_number1 + 1:
     print('Pass')
else:
    print('fail')

