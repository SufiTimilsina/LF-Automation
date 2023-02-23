from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

from Page.PIM import PimPage
from Page.login import LoginPage

s = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=s)


def test_browserstack():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    login = LoginPage(driver)
    login.select_username()
    login.select_password()
    login.click_login()
    time.sleep(5)

    pim = PimPage(driver)
    pim.click_pim()
    pim.select_empname()
    pim.click_search()
    time.sleep(10)


test_browserstack()
