from config import config

def openAnyAuction(self):
    driver = self.driver
    
    signInBtn = driver.find_element_by_class_name('card')
    signInBtn.click()

    self.driver = driver
    return self