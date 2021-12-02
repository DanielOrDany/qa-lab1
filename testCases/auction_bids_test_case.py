import random
from time import sleep
from verifications.verify_last_bidder import vefiryLastBidder
from actions.open_home_page import openHomePage
from actions.open_login_page import openLoginPage
from actions.login import signIn
from actions.open_any_auction import openAnyAuction
from actions.place_bid import placeBid
from actions.logout import signOut
from config import config

class AuctionBidsTestCase:
  def __init__(self, driver):
    self.driver = driver

  def run(self, numberOfRepetitions):
    for x in range(numberOfRepetitions):
      sleep(1)
      self = openLoginPage(self)
      sleep(1)
      users = config.users
      userIndex = random.randint(0, 4)
      self = signIn(self, users[userIndex])
      sleep(3)
      self = openAnyAuction(self)
      sleep(2)
      self = placeBid(self)
      sleep(2)
      vefiryLastBidder(self, users[userIndex]['name'])
      sleep(2)
      self = signOut(self)
