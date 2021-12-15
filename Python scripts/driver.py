from selenium import webdriver


class Driver:

    def __init__(self):
        self.driver = None

    def navigate_to(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        
    def close_driver(self):
        self.driver.quit()
