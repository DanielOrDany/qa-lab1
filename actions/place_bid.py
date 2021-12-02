from config import config

def placeBid(self):
    driver = self.driver
    
    signInBtn = driver.find_element_by_xpath('//button[contains(text(), "Place the bid of")]')
    signInBtn.click()

    self.driver = driver
    return self