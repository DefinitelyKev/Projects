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

product_info = {
    "title": {
        "price": [],
        "sale_price": [],
        "product_url": [],
        "image_url": [],
        "stone_type": [],
        "metal_type": [],
    }
}

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
        (zales_items, 30, 0, 1, "zales_products.csv"),
        (jared_items, 30, 0, 1, "jared_products.csv"),
        (kay_items, 30, 0, 1, "kay_products.csv"),
        (jomashop_items, 50, 1, 1, "jomashop_products.csv"),
        (ross_simons_items, 110, 0, 120, "ross_simons_products.csv"),
    ]

    for (
        retailer,
        results_per_page,
        starting_page,
        page_increment,
        filename,
    ) in static_retailers:
        product_info = static_retailer_earring_scraper(
            driver, retailer, results_per_page, starting_page, page_increment
        )
        product_info = clean_product_titles(product_info)
        product_info = sort_products_by_sale_discount(product_info)
        save_product_info_to_csv(product_info, filename)

    # Scraping data from dynamic retailers
    # dynamic_retailers = [
    #     (superjeweler_items, 235, "superjeweler_products.csv"),
    #     (reeds_items, 24, "reeds_products.csv"),
    # ]
    # for retailer, results_per_page, filename in dynamic_retailers:
    #     product_info = dynamic_retailer_earring_scrape(
    #         driver, retailer, results_per_page
    #     )
    #     product_info = clean_product_titles(product_info)
    #     product_info = sort_products_by_sale_discount(product_info)
    #     save_product_info_to_csv(product_info, filename)

    # return product_info


def clean_product_titles(product_info):
    """
    Cleans product titles by removing newlines and any text following newlines.
    """
    cleaned_product_info = {}
    for title, details in product_info.items():
        clean_title = title.split("\n")[0]
        cleaned_product_info[clean_title] = details
    return cleaned_product_info


def sort_products_by_sale_discount(product_info):
    """
    Sorts the products by sale discount in descending order.
    """
    products_list = [(title, details) for title, details in product_info.items()]

    products_list.sort(key=lambda x: x[1].get("sale_discount", 0), reverse=True)

    sorted_product_info = {title: details for title, details in products_list}
    return sorted_product_info


def save_product_info_to_csv(product_info, filename):
    """
    Saves product information from a nested dictionary to a CSV file.
    """
    headers = [
        "Title",
        "Price",
        "Original Price",
        "Sale Discount",
        "Product URL",
        "Image URL",
        "Stone Type",
        "Metal Type",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for title, details in product_info.items():
            price = details.get("price", "")
            original_price = details.get("original_price", "")
            sale_discount = details.get("sale_discount", "")
            product_url = details.get("product_url", "")
            image_url = details.get("image_url", "")
            stone_type = ", ".join(details.get("stone", []))
            metal_type = ", ".join(details.get("metal", []))

            writer.writerow(
                [
                    title,
                    price,
                    original_price,
                    sale_discount,
                    product_url,
                    image_url,
                    stone_type,
                    metal_type,
                ]
            )


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
    save_product_info_to_csv(product_info, "products.csv")
    close_driver(driver)
