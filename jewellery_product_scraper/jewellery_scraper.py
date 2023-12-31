from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time
import csv
import os
import pandas as pd
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
#     "title": {
#         "price": [],
#         "sale_price": [],
#         "product_url": [],
#         "image_url": [],
#         "stone_type": [],
#         "metal_type": [],
#     },
#     more products etc
# }

# types = ["earrings"]

# top 100 in rings, earrings, necklaces, bracelets, watches
# give filter to material such as gold, silver, diamond, etc.
# give price filter
# Find the biggest discount from orginal price compared to sale price

# Track product price over time and give top 5 item in price drop.
# Create a newsletter so that customers get updated discount. Such as sending top 3 discount of day


class EarringScraper:
    def __init__(self):
        self.is_final = False
        self.retailer_items = [
            zales_items,
            kay_items,
            jared_items,
            jomashop_items,
            ross_simons_items,
            superjeweler_items,
            reeds_items,
        ]

    @staticmethod
    def initialize_driver():
        """
        Initializes and returns a Chrome webdriver with specific options for web scraping.
        """
        options = uc.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 1}
        )
        return uc.Chrome(use_subprocess=True, options=options)

    @staticmethod
    def close_driver(driver):
        """
        Closes the Chrome driver and handles any exceptions during closure.
        """
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(f"Error closing the driver: {e}")

    def get_static_retailers(self, driver):
        static_retailers = [
            ([driver, zales_items, 30, 0, 1], "zales_products.csv"),
            ([driver, jared_items, 30, 0, 1], "jared_products.csv"),
            ([driver, kay_items, 30, 0, 1], "kay_products.csv"),
            ([driver, jomashop_items, 50, 1, 1], "jomashop_products.csv"),
            ([driver, ross_simons_items, 110, 0, 120], "ross_simons_products.csv"),
        ]
        return static_retailers

    def get_dynamic_retailers(self, driver):
        dynamic_retailers = [
            ([driver, superjeweler_items, 235], "superjeweler_products.csv"),
            ([driver, reeds_items, 24], "reeds_products.csv"),
        ]
        return dynamic_retailers

    def get_retailer_items(self):
        return self.retailer_items

    def get_finalized_product_data(self, filename):
        combined_data = self.combine_csv_files("product_data")
        combined_data = self.add_material_type(combined_data)
        finalized_product_data = self.clean_and_sort_product_info(combined_data)
        self.other(finalized_product_data, filename)

    def scrape_retailer_data(self, driver):
        """
        Scrapes earring product data from various retailers and accumulates it in a dictionary.
        """
        product_info = {}
        static_retailers = self.get_static_retailers(driver)
        dynamic_retailers = self.get_dynamic_retailers(driver)

        for retailer_info, filename in static_retailers:
            product_info = static_retailer_earring_scraper(*retailer_info)
            product_info = self.clean_and_sort_product_info(product_info)
            self.save_product_info_to_csv(product_info, filename)

        for retailer_info, filename in dynamic_retailers:
            product_info = dynamic_retailer_earring_scrape(*retailer_info)
            product_info = self.clean_and_sort_product_info(product_info)
            self.save_product_info_to_csv(product_info, filename)

    def clean_and_sort_product_info(self, product_info):
        """
        Cleans product titles by removing newlines and any text following newlines and sorts title by sale discount in descending order.
        """
        sorted_info = dict(
            sorted(
                product_info.items(),
                key=lambda x: x[1].get("sale_discount", 0),
                reverse=True,
            )
        )
        return {title.split("\n")[0]: details for title, details in sorted_info.items()}

    def save_product_info_to_csv(self, product_info, filename):
        """
        Saves product information from a nested dictionary to a CSV file in the 'product_data' folder.
        """
        folder_name = "product_data"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_path = os.path.join(folder_name, filename)

        headers = [
            "title",
            "price",
            "original_price",
            "sale_discount",
            "product_url",
            "image_url",
        ]

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for title, details in product_info.items():
                row = {**details, "title": title}
                writer.writerow(row)

    def other(self, product_data, filename):
        headers = [
            "title",
            "price",
            "original_price",
            "sale_discount",
            "product_url",
            "image_url",
            "stone_type",
            "metal_type",
        ]

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            for key, value in product_data.items():
                # Preparing row for CSV
                row = {**value}
                writer.writerow(row)

    def combine_csv_files(self, directory, max_entries_per_file=100):
        """
        Combines data from CSV files in a directory into a single dictionary.
        """
        combined_data = {}

        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                entry_count = 0

                for row in reader:
                    if entry_count < max_entries_per_file:
                        combined_data[f"{filename}_entry{entry_count}"] = row
                        entry_count += 1
                    else:
                        break

        return combined_data

    def find_material_in_title(self, title, materials):
        """
        Searches for materials in the product title and returns the found material.
        """
        for material in materials:
            if material in title.lower():
                return material.capitalize()
        return None

    def add_material_type(self, product_info):
        """
        Adds material types to the product information based on the product title.
        """
        retailer_items = self.get_retailer_items()

        for product_number, details in product_info.items():
            title = details["title"]
            retailer = next(
                (item for item in retailer_items if item["name"] in product_number),
                None,
            )
            if not retailer:
                continue

            stone_type = self.find_material_in_title(title, retailer["stone_type"])
            metal_type = self.find_material_in_title(title, retailer["metal_type"])

            if stone_type:
                details.setdefault("stone_type", []).append(stone_type)
            else:
                details.setdefault("stone_type", []).append("No Stone")

            if metal_type:
                details.setdefault("metal_type", []).append(metal_type)

        self.is_final = True
        return product_info


def main():
    scraper = EarringScraper()
    driver = scraper.initialize_driver()
    try:
        # scraper.scrape_retailer_data(driver)
        scraper.get_finalized_product_data("finalized_product_info.csv")

    finally:
        scraper.close_driver(driver)


if __name__ == "__main__":
    main()
