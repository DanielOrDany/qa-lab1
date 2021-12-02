from testCases.auction_bids_test_case import AuctionBidsTestCase
from webDrivers.chrome import webdriver

auctionBidsTest = AuctionBidsTestCase(webdriver.Chrome())
auctionBidsTest.run(3)