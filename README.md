# Python Craigslist Scraper

Python Scraper for Craigslist. Allows you to scrape craigslist search and produce the title, price, date, and url link of each post. This is a basic implementation and only shows a fraction of what can be done.

## Requirements

- Selenium
- Beautiful Soup 4

```
pip install selenium
pip install bs4
```

## Set your search variables

You must set up custom variables for this scraper to work. Replace each item inside quotes with your desired search criteria.

```
query = "QUERY"
location = "LOCATION"
postal = "ZIPCODE"
max_price = "PRICE"
radius = "MILES"
```

## Running the script

Run the python script in terminal:

```
python craigslist_scraper.py
```

## Screenshots

![Post Data](https://i.imgur.com/mwQZLhf.png "Post Data")
![Post URL List](https://i.imgur.com/hN0l1wU.png "Post URL List")

## Built With

- Python
- Selenium
- Beautiful Soup 4

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
