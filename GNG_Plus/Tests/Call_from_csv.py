from  selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os

#در اولین مرحله csv را ایمپورت می کنیم.
import csv



#آدرس فعلی اسکریپت در current_dir ذخیره می شود .
currnet_dir = os.path.dirname(os.path.abspath(__file__))

#آدرس ذخیره شده با نام فایل ترکیب می شود
file_path = os.path.join(currnet_dir,'user.csv')

with open (file_path,'r') as file:

# مسیر دهی فایل csv
# with open('C:/Users/goudarzi.razieh/Desktop/user.csv','r') as file:

    #متغیری که ردیفهای فایل را بخواند
    reader = csv.reader(file)

    #نادیده گرفتن ردیف اول فایل
    next(reader)

    #ایجاد حلقه برای خواندن ردیف های فایل
    for row in reader:
        username = row[0]
        password = row[1]

        driver = webdriver.Chrome()

        driver.get("http://172.31.0.156:5529/")
        sleep(4)

        driver.find_element(By.CSS_SELECTOR, "input[name = 'username']").send_keys(username)
        driver.find_element(By.CSS_SELECTOR, "input[name = 'password']").send_keys(password)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "dx-button[role='button']").click()

        sleep(5)
        driver.quit()




