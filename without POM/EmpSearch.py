from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

username = driver.find_element(By.XPATH, "//input[@name='username']")
username.send_keys("Admin")

password_field = driver.find_element(By.XPATH, "//input[@name='password']")
password_field.send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//li[@class='oxd-main-menu-item-wrapper'][2]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


time.sleep(10)
