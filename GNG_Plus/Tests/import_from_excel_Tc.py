from Pages.Login import Login_Page
from Pages.profuct_request import Insert_request
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.maximize_window()

login_object = Login_Page(driver = driver)
product_object = Insert_request(driver = driver)
driver.get("http://172.31.0.156:5529/")
login_object.login('qcuser','Qc@123456')
sleep(3)

product_object.importing()
product_object.insert_request()
sleep(1)
driver.find_element(By.XPATH,"(//tbody)[7]//tr[1]").click()
#driver.find_element(By.XPATH,"//div[@aria-label='درج گروهی از اکسل']").click()
driver.find_element(By.XPATH,"//div[@aria-label='درج گروهی از اکسل']").send_keys("C:/Users/goudarzi.razieh/Documents/25.xlsx")
#driver.find_element(By.XPATH,"//dx-button[@aria-label = 'انتقال']").click()
sleep(3)
#
# df = pd.read_excel("C:/Users/goudarzi.razieh/Documents/25.xlsx")
# sleep(5)
# print(df)
sleep(5)

