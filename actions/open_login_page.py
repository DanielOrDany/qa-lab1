from config import config

def openLoginPage(self):
    driver = self.driver
    driver.get(config.pages['LOGIN_PAGE'])
    self.driver = driver
    return self