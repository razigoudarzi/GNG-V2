from selenium import webdriver
import time
from Pages.Adding_Job import Adding_job
from Pages.login_class import login_page


driver = webdriver.Chrome()
driver.maximize_window()




driver.get("http://172.31.0.156:1921/")
time.sleep(1)
login_object = login_page(driver = driver)
login_object.login('adminhr','123!@#QWEasdzxc')

add_job= Adding_job(driver = driver)
add_job.add_job('140429','Test28')

time.sleep(5)
add_job.delete_job_by_code('140429')

time.sleep(2)
