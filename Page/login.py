from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'username': ('XPATH', "//input[@name='username']"),
        'password': ('XPATH', "//input[@name='password']"),
        'login_btn': ('XPATH', "//button[@type='submit']")
    }

    def select_username(self):
        self.username.send_keys('Admin')

    def select_password(self):
        self.password.send_keys("admin123")

    def click_login(self):
        self.login_btn.click()
