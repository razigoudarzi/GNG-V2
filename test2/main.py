from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
base_url = "https://play1.automationcamp.ir/"

driver.get(f"{base_url}/forms.html")
time.sleep(5)

driver.find_element(By.ID,'check_python').click()

time.sleep(5)
check1 = driver.find_element(By.ID,'check_validate').text

time.sleep(2)
assert check1 == 'PYTHON'

text2 = 'I am learning automtion'
time.sleep(3)
driver.find_element(By.ID,'notes').send_keys(text2)

time.sleep(3)
check2 = driver.find_element(By.ID,'area_notes_validate').text

assert check2 == text2