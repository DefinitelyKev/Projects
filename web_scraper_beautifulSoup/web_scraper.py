from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import Session
import requests
import undetected_chromedriver as uc
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re
import os
from itertools import zip_longest
from web_scraper_selectors import retailer_info


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


def write_to_csv(product_dict, folder_name="product_data"):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for category, products in product_dict.items():
        if not products:
            continue  # Skip empty categories

        # Determine the fieldnames from the first product dictionary
        fieldnames = products[0].keys()

        file_path = os.path.join(folder_name, f"{category}.csv")
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)

        print(f"Data for {category} written to {file_path}")


def get_centercom_availbility(product, product_available):
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


def get_pccasegear_avaibility(product_avaliable):
    if product_avaliable == "Check back later!":
        return "Out of Stock"
    elif product_avaliable != "In stock":
        return "Preorder"
    else:
        return "In Stock"


def get_mwave_avaibility(product_avaliable):
    if product_avaliable == "Add to Cart":
        return "In Stock"
    return product_avaliable


def get_scorptec_avaibility(product_avaliable):
    if product_avaliable == ("sold out" or "end of life"):
        return "Out of Stock"
    elif "eta" in product_avaliable:
        return "Pre-order"
    else:
        return "In Stock"


def get_availability(product, product_info, retailer):
    if retailer == "centercom":
        return get_centercom_availbility(product, product_info["availability"])
    elif retailer == "pccasegear":
        return get_pccasegear_avaibility(product_info["availability"])
    elif retailer == "mwave":
        return get_mwave_avaibility(product_info["availability"])
    elif retailer == "scorptec":
        return get_scorptec_avaibility(product_info["availability"])


def get_product_brand(product, product_info, retailer):
    if retailer == "centercom":
        brand_div = product.find("div", attrs={"class": "manufacturer-picture"})
        brand_img = brand_div.find("img")
        brand_name = brand_img.get("alt") if brand_img else None
        return brand_name

    product_brand = product_info["title"].split(" ", 1)[0]
    if product_brand == "Lian":
        product_brand = "Lian Li"
    elif product_brand == "be":
        product_brand = "Be Quiet!"
    elif product_brand == "Cooler":
        product_brand = "Cooler Master"
    elif product_brand == "Fractal":
        product_brand = "Fractal Design"
    return product_brand


def scrape_retailer_products(
    div_find, retailer, categories, selectors, url, items_per_page
):
    for item_category, category_selector in categories.items():
        for sub_catergory in category_selector:
            page_number = 1
            while page_number:
                driver.get(
                    url.format(sub_catergory=sub_catergory, page_number=page_number)
                )
                time.sleep(1)

                soup = BeautifulSoup(driver.page_source, "html.parser")
                element, class_name = div_find
                products = soup.find_all(element, class_=class_name)

                get_product_info_list(
                    products, product_dict, retailer, selectors, item_category
                )

                if len(products) < items_per_page:
                    break

                page_number += 1


def get_product_info_list(products, product_dict, retailer, selectors, item_category):
    for product in products:
        product_info = get_product_info(product, selectors)

        if retailer in ["centercom", "pccasegear", "mwave", "scorptec"]:
            product_info["brand"] = get_product_brand(product, product_info, retailer)
            product_info["availability"] = get_availability(
                product, product_info, retailer
            )

        print(product_info)
        product_dict[item_category].append(product_info)


if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.headless = False

    driver = uc.Chrome(use_subprocess=True, options=options)

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
        "speakers": [],
        "webcams": [],
    }

    # Open the page with Selenium
    try:
        for retailer, info in retailer_info.items():
            scrape_retailer_products(
                info["div_find"],
                retailer,
                info["categories"],
                info["selectors"],
                info["url"],
                info["items_per_page"],
            )
        # scrape_retailer_products(
        #     retailer_info["pccasegear"]["div_find"],
        #     "pccasegear",
        #     retailer_info["pccasegear"]["categories"],
        #     retailer_info["pccasegear"]["selectors"],
        #     retailer_info["pccasegear"]["url"],
        #     retailer_info["pccasegear"]["items_per_page"],
        # )
        write_to_csv(product_dict, "my_product_data")
    finally:
        driver.close()
