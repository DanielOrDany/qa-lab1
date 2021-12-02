from config import config

def openHomePage(self):
    driver = self.driver
    driver.get(config.HOME_PAGE)
    self.driver = driver
    return self