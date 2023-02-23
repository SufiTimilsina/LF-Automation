from seleniumpagefactory.Pagefactory import PageFactory


class AddEmp(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'pim': ('XPATH', "//li[@class='oxd-main-menu-item-wrapper'][2]"),
        'add': ('XPATH', "//button[text()=' Add ']"),
        'fname': ('XPATH', "//input[@placeholder='First Name']"),
        'lname': ('XPATH', "//input[@placeholder='Last Name']"),
        'save': ('XPATH', "// button[@type = 'submit']")
    }

    def click_pim(self):
        self.pim.click()

    def click_button(self):
        self.add.click()

    def firstname(self):
        self.fname.send_keys("Ramma")

    def lastname(self):
        self.lname.send_keys("Thapa")

    def save_button(self):
        self.save.click()



