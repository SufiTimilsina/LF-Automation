from seleniumpagefactory.Pagefactory import PageFactory


class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'search': ('XPATH', "//input[@placeholder='Search']"),
        'sidebar': ('XPATH', "//li[@class='oxd-main-menu-item-wrapper']")
    }

    def click_search(self):
        self.search.click()
        self.search.send_keys('Time')

        try:
            self.sidebar.click()

        except:
            raise ValueError("Element not found!")
