from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import chromedriver_binary

#Open your browser (Chrome 94.0.4606.41)
driver = webdriver.Chrome()

#Open the Google search TOP screen.
driver.get("https://www.google.com")

#Type "quickquery" as the search term and press Enter.
search = driver.find_element_by_name('q')
search.send_keys("quickquery")
search.send_keys(Keys.ENTER)

element = driver.find_element_by_partial_link_text("QuickQuery")
element.click()

sleep(5)

driver.close()