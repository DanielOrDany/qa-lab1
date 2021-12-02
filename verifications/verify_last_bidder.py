def vefiryLastBidder(self, bidderName):
    driver = self.driver

    lastBidder = driver.find_element_by_xpath("//*/span[contains(text(),'" + bidderName + "')]")

    if not lastBidder:
        print("Last bidder is not counted!")
    else:
        print("Last bidder is counted:", bidderName)

    self.driver = driver
    return self