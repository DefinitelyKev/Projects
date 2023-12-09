from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re
from web_scraper_selectors import (
    umart_selctors,
    umart_categories,
    computer_alliance_selctors,
    center_com_categories,
    center_com_selectors,
    pc_case_gear_categories,
    pc_case_gear_selectors,
    mwave_categories,
    mwave_selectors,
)

product_dict = {
    "cases": [],
    "cooling": [],
    "cpus": [],
    "gpus": [],
    "fans": [],
    "ram": [],
    "mother_boards": [],
    "psus": [],
    "sound_cards": [],
    "ssds": [],
    "hdds": [],
    "headphones": [],
    "keyboards": [],
    "microphones": [],
    "monitors": [],
    "mouses": [],
    "mouse_pad": [],
    "speakers": [],
    "webcams": [],
}


def get_product_info(product, selectors):
    product_details = {}

    for key, (tag, attribute, selector_name) in selectors.items():
        element = product.find(tag, attrs={attribute: selector_name})
        if key == "on_sale":
            if not element:
                product_details["price_off"] = None
                break
            else:
                continue

        if key == "availability":
            if not element:
                product_details[key] = "Out Of Stock"
                continue

        product_details[key] = element.text.strip() if element else None

    return product_details


# def addToCSV(products):
#     with open("products.csv", "w", newline="") as csv_file:
#         writer = csv.DictWriter(
#             csv_file,
#             fieldnames=[
#                 "title",
#                 "price",
#                 "brand",
#                 "availability",
#                 "price_off",
#             ],
#         )
#         writer.writeheader()
#         for product in products:
#             writer.writerow(product)


def addToCSV(products):
    with open("products.csv", "w", newline="") as csv_file:
        # Assuming 'products' is a dictionary where each key has a list of values
        fieldnames = [
            "title",
            "price",
            "brand",
            "availability",
            "price_off",
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Find the length of the longest list in the dictionary
        max_length = max(len(lst) for lst in products.values())

        for i in range(max_length):
            row = {
                key: products[key][i] if i < len(products[key]) else None
                for key in fieldnames
            }
            writer.writerow(row)


def umart_scaper(retailer_find):
    results_per_page = 120
    for item_category, category_selector in umart_categories.items():
        page_number = 1
        while True:
            umart_url = f"https://www.umart.com.au/pc-parts/{category_selector}?page={page_number}&mystock=1-7-6&sort=salenum&order=ASC&pagesize=3"

            driver.get(umart_url)
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            element, class_name = retailer_find["umart"]
            products = soup.find_all(element, class_=class_name)

            for product in products:
                product_dict[item_category].append(
                    get_product_info(product, umart_selctors)
                )

            if len(products) < results_per_page:
                break

            page_number += 1

    print(product_dict)


def center_com_availbility_check(product, product_available):
    if product_available == "Not available to purchase online.":
        product_find_instore = product.find("span", class_="instore").text.strip()
        if product_find_instore == "Not available to purchase at retail stores.":
            product_available = "Out of Stock"
        else:
            product_available = "In Stock Instore"
    elif product_available == "Available to preorder online.":
        product_available = "Pre-order"
    else:
        product_available = "In Stock Online"
    return product_available


def center_com_scraper(retailer_find):
    results_per_page = 30
    for item_category, category_selector in center_com_categories.items():
        page_number = 1
        while True:
            center_com_url = f"https://www.centrecom.com.au/{category_selector}?orderby=20&viewmode=list&pagenumber={page_number}"

            driver.get(center_com_url)
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            element, class_name = retailer_find["center_com"]
            products = soup.find_all(element, class_=class_name)

            for product in products:
                product_info = get_product_info(product, center_com_selectors)

                brand_div = product.find("div", attrs={"class": "manufacturer-picture"})
                brand_img = brand_div.find("img")
                brand_name = brand_img.get("alt") if brand_img else None
                product_info["brand"] = brand_name

                product_info["availability"] = center_com_availbility_check(
                    product, product_info["availability"]
                )

                print(product_info)
                product_dict[item_category].append(product_info)

            if len(products) < results_per_page:
                break

            page_number += 1


def pc_case_gear_scraper(retailer_find):
    results_per_page = 20
    for item_category, category_selector in pc_case_gear_categories.items():
        page_number = 1
        while True:
            pc_case_gear_url = f"https://www.pccasegear.com/search?query={category_selector}&hierarchicalMenu%5Bcategories.lvl0%5D={category_selector}&page={page_number}"

            driver.get(pc_case_gear_url)
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            element, class_name = retailer_find["pc_case_gear"]
            products = soup.find_all(element, class_=class_name)

            for product in products:
                product_info = get_product_info(product, pc_case_gear_selectors)

                if product_info["availability"] == "Check back later!":
                    product_info["availability"] = "Out of Stock"
                elif product_info["availability"] != "In stock":
                    product_info["availability"] = "Preorder"
                else:
                    product_info["availability"] = "In Stock"

                print(product_info)
                product_dict[item_category].append(product_info)

            if len(products) < results_per_page:
                break

            page_number += 1


def mwave_scraper(retailer_find):
    results_per_page = 100
    for item_category, category_selector in mwave_categories.items():
        page_number = 0
        while True:
            mwave_url = f"https://www.mwave.com.au/searchresult?w={category_selector}&cnt=100&srt={page_number}&isort=score&view=grid&af="

            driver.get(mwave_url)
            time.sleep(2)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            element, class_name = retailer_find["mwave"]
            products = soup.find_all(element, class_=class_name)

            for product in products:
                product_info = get_product_info(product, mwave_selectors)

                print(product_info)
                product_dict[item_category].append(product_info)

            if len(products) < results_per_page:
                break

            page_number += 100


if __name__ == "__main__":
    options = Options()
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    retailer_find = {
        "umart": ["div", "row goods-item"],
        "computer_alliance": ["div", "product"],
        "center_com": ["div", "item-box"],
        "pc_case_gear": ["div", "search-container list-container"],
        "mwave": ["li", "listItem"],
    }

    # Open the page with Selenium
    try:
        # umart_scaper(retailer_find)
        # center_com_scraper(retailer_find)
        # pc_case_gear_scraper(retailer_find)
        mwave_scraper(retailer_find)
    finally:
        driver.quit()
