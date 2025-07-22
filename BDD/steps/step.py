import time

from behave  import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://172.31.0.156:4326")
    context.driver.maximize_window()

@when ('I enter the username "{username}"')
def step_impl(context,username):
   sleep(2)
   user = context.driver.find_element(By.XPATH,"//input[@data-placeholder='نام کاربری']")
   user.send_keys(username)

@when('I enter the password "{passwrod}"')
def step_impl(context,passwrod):
    sleep(2)
    pasw = context.driver.find_element(By.XPATH,"//input[@data-placeholder='رمز عبور']")
    pasw.send_keys(passwrod)

@when('I click the login button')
def stet_impl(context):
    sleep(2)
    context.driver.find_element(By.XPATH,"//button[@type = 'submit']").click()

@then('I should be redirected to the dashboard page')
def step_impl(context):
    sleep(2)
    assert context.driver.current_url=="http://172.31.0.156:4326/#/launcher/home"



