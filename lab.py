from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary

class WebSiteTest:
  def __init__(self, website_name):
    self.website_name = website_name
    self.chrome_driver = webdriver.Chrome()

  def findSiteInGoogle(self):
    print("Website: " + self.website_name)

    # Open your browser (Chrome 94.0.4606.41)
    driver = self.chrome_driver

    # Open the Google search TOP screen.
    driver.get("https://www.google.com")

    search = driver.find_element_by_name('q')
    search.send_keys(self.website_name)
    search.send_keys(Keys.ENTER)

    element = driver.find_element_by_partial_link_text(self.website_name)
    element.click()

    sleep(5)
    driver.close()

  def registerNewUser(self):
    print("Website: " + self.website_name)

    # Open your browser (Chrome 94.0.4606.41)
    driver = self.chrome_driver

    # Open the Google search TOP screen.
    driver.get("https://www.google.com")

    search = driver.find_element_by_name('q')
    search.send_keys(self.website_name)
    search.send_keys(Keys.ENTER)

    element = driver.find_element_by_partial_link_text(self.website_name)
    element.click()

    signInBtn = driver.find_element_by_xpath('//a[contains(text(), "Signin")]')
    signInBtn.click()

    createNewAccountBtn = driver.find_element_by_xpath('//a[contains(text(), "Create")]')
    createNewAccountBtn.click()

    sleep(5)
    driver.close()

web_site = WebSiteTest("testapp")

# web_site.findSiteElement();

web_site.registerNewUser()