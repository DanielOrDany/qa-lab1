def signOut(self):
    driver = self.driver

    # click on login btn
    signInBtn = driver.find_element_by_class_name('logout-icon')
    signInBtn.click()

    self.driver = driver
    return self