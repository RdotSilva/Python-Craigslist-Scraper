from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraigslistScraper(object):
  def __init__(self, location, postal, max_price, radius):
    self.location = location
    self.postal = postal
    self.max_price = max_price
    self.radius = radius

    self.url = f"https://{location}.craigslist.org/search/sss?&sort=date&search_distance={radius}&postal={postal}&max_price={max_price}"


location = "providence"
postal = "02904"
max_price = "200"
radius = "50"

scraper = CraigslistScraper(location, postal, max_price, radius)

