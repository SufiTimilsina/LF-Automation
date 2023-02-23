#test for adding employee

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

from Page.Addemp import AddEmp
from Page.login import LoginPage

s = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=s)


def test_two():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    login = LoginPage(driver)
    login.select_username()
    login.select_password()
    login.click_login()
    time.sleep(5)

    add = AddEmp(driver)
    add.click_pim()
    add.click_button()
    add.firstname()
    add.lastname()
    time.sleep(5)
    add.save_button()
    time.sleep(10)


test_two()
