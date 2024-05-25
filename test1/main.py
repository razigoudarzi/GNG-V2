from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# chrome_options=Options()
# chrome_options.add_experimental_option("detach",True)
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(10)
search = driver.find_element(By.NAME,'q')
search_button = driver.find_element(By.NAME,'btnK')
time.sleep(2)
search.send_keys("python")
time.sleep(3)

search_button.send_keys(Keys.ENTER)

time.sleep(10)



