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
    
    self.driver = webdriver.Firefox()

    # Set delay higher if you get timeout exception below
    self.delay = 3

    # Use load url with webdriver
  def load_craigslist_url(self):
    self.driver.get(self.url)
    try:
      wait = WebDriverWait(self.driver, self.delay)
      # Wait until the form with id of searchform is loaded
      wait.until(EC.presence_of_element_located((By.ID, "searchform")))
      print("Page is ready")
    except TimeoutException:
      print("Loading took too much time")
  
  def extract_post_information(self):
    # Give list of selenium objects with class name of result-row
    all_posts = self.driver.find_elements_by_class_name("result-row")

    dates = []
    titles = []
    prices = []

    for post in all_posts:
      title = post.text.split("$")
      
      if title[0] == '':
        title = title[1]
      else:
        title = title[0]

      title = title.split("\n")
      price = title[0]
      title = title[-1]

      title = title.split(" ")

      month = title[0]
      day = title[1]

      title = ' '.join(title[2:])
      date = month + " " + day
      # print("PRICE: " + price)
      # print("TITLE: " + title)
      # print("DATE: " + date)

      titles.append(title)
      prices.append(price)
      dates.append(date)

    return titles, prices, dates
      

  def extract_post_urls(self):
    url_list = []
    html_page = urllib.request.urlopen(self.url)
    soup = BeautifulSoup(html_page)

    # Find all a tags with class of result-title hdrlnk
    for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
      print(link["href"])
      url_list.append(link["href"])
    return url_list

  # Close driver
  def quit(self):
    self.driver.close()


  
location = "providence"
postal = "02904"
max_price = "200"
radius = "50"

scraper = CraigslistScraper(location, postal, max_price, radius)
scraper.load_craigslist_url()
titles, prices, dates = scraper.extract_post_information()
print(titles)
# scraper.extract_post_urls()
# scraper.quit()