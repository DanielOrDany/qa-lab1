from selenium.webdriver.common.keys import Keys

def signIn(self, user):
    driver = self.driver

    # put user creds
    inputUsername = driver.find_element_by_xpath("//input[contains(@id,'loginInputEmail')]")
    inputUsername.send_keys(user['name'])
    inputPassword = driver.find_element_by_xpath("//input[contains(@id,'loginInputPassword')]")
    inputPassword.send_keys(user['password'])

    # click on login btn
    signInBtn = driver.find_element_by_tag_name('button')
    signInBtn.click()

    self.driver = driver
    return self