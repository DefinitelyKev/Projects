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


def initialize_driver():
    """
    Initializes and returns a Chrome webdriver with specific options for web scraping.
    """
    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )

    return uc.Chrome(use_subprocess=True, options=options)


def scrape_retailer_data(driver):
    """
    Scrapes earring product data from various retailers and accumulates it in a dictionary.
    """
    product_info = {}

    # Scraping data from static retailers
    static_retailers = [
        (zales_items, 30, 0, 1),
        (jared_items, 30, 0, 1),
        (kay_items, 30, 0, 1),
        (jomashop_items, 50, 1, 1),
        (ross_simons_items, 110, 0, 120),
    ]
    for retailer, results_per_page, starting_page, page_increment in static_retailers:
        product_info = product_info | static_retailer_earring_scraper(
            driver, retailer, results_per_page, starting_page, page_increment
        )

    # Scraping data from dynamic retailers
    dynamic_retailers = [(superjeweler_items, 235), (reeds_items, 24)]
    for retailer, results_per_page in dynamic_retailers:
        product_info = product_info | dynamic_retailer_earring_scrape(
            driver, retailer, results_per_page
        )

    return product_info


def close_driver(driver):
    """
    Closes the Chrome driver and handles any exceptions during closure.
    """
    try:
        driver.close()
        driver.quit()
    except Exception as e:
        print(f"Error closing the driver: {e}")


if __name__ == "__main__":
    driver = initialize_driver()
    product_info = scrape_retailer_data(driver)
    close_driver(driver)
