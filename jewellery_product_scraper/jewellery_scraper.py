from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time
import csv
import os
from static_website_scraper_functions import static_retailer_earring_scraper
from dynamic_website_scraper_functions import dynamic_retailer_earring_scrape
from retailer_selectors import (
    zales_items,
    reeds_items,
    superjeweler_items,
    jared_items,
    kay_items,
    ross_simons_items,
    jomashop_items,
)

# product_info = {
#     "title": [],
#     "price": [],
#     "sale_price": [],
#     "product_url": [],
#     "image_url": [],
#     "stone_type": [],
#     "material_type": [],
# }

# types = ["earrings"]

# top 100 in rings, earrings, necklaces, bracelets, watches
# give filter to material such as gold, silver, diamond, etc.
# give price filter
# Find the biggest discount from orginal price compared to sale price

# Track product price over time and give top 5 item in price drop.
# Create a newsletter so that customers get updated discount. Such as sending top 3 discount of day


if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    driver = uc.Chrome(use_subprocess=True, options=options)

    zales_earrings = {}

    # banana = static_retailer_earring_scraper(driver, zales_items, 30, 0, 1)
    # pear = static_retailer_earring_scraper(driver, jomashop_items, 50, 1, 1)
    # apple = static_retailer_earring_scraper(driver, ross_simons_items, 110, 0, 120)
    # kiwi = dynamic_retailer_earring_scrape(driver, superjeweler_items, 235)
    # grape = static_retailer_earring_scraper(driver, reeds_items, 24, 1, 1)
    grape = dynamic_retailer_earring_scrape(driver, reeds_items, 24)

    try:
        driver.close()
        driver.quit()
    except:
        pass


# pineapple = static_retailer_earring_scraper(jared_items, 30, 0, 1)
# blueberry = static_retailer_earring_scraper(kay_items, 30, 0, 1)
