from seleniumpagefactory.Pagefactory import PageFactory


class PimPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'pim': ('XPATH', "//li[@class='oxd-main-menu-item-wrapper'][2]"),
        'name': ('XPATH', "//input[@placeholder='Type for hints...']"),
        'search': ('XPATH', "//button[@type='submit']")
    }

    def click_pim(self):
        self.pim.click()

    def select_empname(self):
        self.name.send_keys('Admin')

    def click_search(self):
        self.search.click()
