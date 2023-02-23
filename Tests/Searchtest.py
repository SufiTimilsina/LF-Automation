from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from Page.login import LoginPage
from Page.search import SearchPage

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

    search = SearchPage(driver)
    search.click_search()
    time.sleep(5)


test_two()
