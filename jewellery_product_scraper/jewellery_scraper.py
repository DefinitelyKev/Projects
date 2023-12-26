from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import Session
import requests
import undetected_chromedriver as uc
import time
import csv
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re
from re import sub
from decimal import Decimal
import os

from retailer_selectors import (
    zales_items,
    reeds_items,
    superjeweler_items,
    jared_items,
    kay_items,
    ross_simons_items,
    jomashop_items,
)

# FEMALE ONLY

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


def get_product_url(retailer_name, box, retailer_selectors):
    """
    Extracts the product URL from a BeautifulSoup 'box' element based on the retailer's specifics.
    """
    if retailer_name == "reeds":
        product_anchor = box.find_all("a", href=lambda href: href and "html" in href)
        product_url = product_anchor[0].get("href") if product_anchor else None
    else:
        product_anchor = box.find(*retailer_selectors["product_href"])
        product_url = product_anchor.get("href") if product_anchor else None
    return product_url


def get_price(text):
    """
    Extracts the price from a text string.
    """
    price = re.search(r"\d+(\,\d{1,3})*(.\d+)?", text).group() if text else None
    num_price = float(sub(r"[^\d.]", "", price)) if price else None
    return [price, num_price]


def add_material_type(title, product_info_dict, material):
    """
    Adds material type to the product information dictionary.
    """
    if title not in product_info_dict:
        return False

    material_type, material_value = material
    if material[0] in product_info_dict[title]:
        product_info_dict[title][material_type].append(material_value)
    else:
        product_info_dict[title].update({material_type: [material_value]})
    print(product_info_dict[title])
    return True


def extract_product_details(box, retailer_name, retailer_selectors, material):
    """
    Extracts product details from a BeautifulSoup 'box' element.
    """
    price_element = box.find(*retailer_selectors["price"])
    price, num_price = get_price(price_element.text.strip()) if price_element else None

    original_price_element = box.find(*retailer_selectors["original_price"])
    original_price, num_original_price = (
        get_price(original_price_element.text.strip())
        if original_price_element
        else None
    )

    sale_discount = round(
        ((num_original_price - num_price) / (num_original_price)) * 100, 1
    )

    image_src = box.find(*retailer_selectors["image_src"])
    image_url = image_src.get("src") if image_src else None
    product_url = get_product_url(retailer_name, box, retailer_selectors)

    return {
        "price": price,
        "original_price": original_price,
        "sale_discount": sale_discount,
        "image_url": image_url,
        "product_url": product_url,
        material[0]: [material[1]],
    }


def get_product_info(
    driver, product_info_dict, retailer_items, results_per_page, material
):
    """
    Scrapes product information from a web page.
    """
    retailer_selectors = retailer_items["selectors"]
    retailer_name = retailer_items["name"]
    soup = BeautifulSoup(driver.page_source, "lxml")
    product_boxes = soup.find_all(*retailer_selectors["product_boxes"])

    for box in product_boxes:
        try:
            on_sale = box.find(*retailer_selectors["product_on_sale"])
            if not on_sale:
                continue

            title = box.find(*retailer_selectors["title"]).text.strip()

            if add_material_type(title, product_info_dict, material):
                continue

            product_info_dict[title] = extract_product_details(
                box, retailer_name, retailer_selectors, material
            )
            print(product_info_dict[title])

        except Exception as error:
            print(f"Error processing box: {error}")

    print(len(product_boxes))
    if len(product_boxes) < results_per_page:
        return True
    return False


def construct_url(retailer_items, type_key, material, page_number):
    """
    Constructs the URL based on retailer name, material type, and page number.
    """
    base_url = retailer_items.get("url", "")
    if retailer_items["name"] == "ross_simons":
        if type_key == "stone" and material not in [
            "Diamond",
            "Pearls",
            "Other+Stones",
        ]:
            return retailer_items["url_gemstone"].format(
                material=material, page_number=page_number
            )
        elif type_key == "stone" and material == "Cubic+Zirconia":
            return retailer_items["url_faux"].format(page_number=page_number)

    return base_url.format(type=type_key, material=material, page_number=page_number)


def website_lazy_loading(driver):
    """
    Scrolls through website to load all products with lazy loading.
    """
    website_height = driver.execute_script("return document.body.scrollHeight")
    scroll_count = round(website_height, -3)

    for website_y_axis in range(1000, scroll_count, 1000):
        driver.execute_script(f"window.scrollTo(0, {website_y_axis})")
        time.sleep(0.3)


def retailer_earring_data_scraper(
    retailer_items, results_per_page, starting_page, page_increment
):
    """
    Scrapes earring product data from a retailer's website.
    """

    def scrape_material(type_key, driver, product_info_dict):
        """
        Scrapes material data from the retailer's website.
        """
        page_number = starting_page
        while page_number < 2:
            url = construct_url(retailer_items, type_key, material, page_number)
            driver.get(url)
            time.sleep(2)

            website_lazy_loading(driver)

            out_of_products = get_product_info(
                driver,
                product_info_dict,
                retailer_items,
                results_per_page,
                [type_key, material],
            )

            if out_of_products:
                break
            page_number += page_increment

    product_info_dict = {}
    for material in retailer_items["stone_type"]:
        scrape_material("stone", driver, product_info_dict)

    for material in retailer_items["metal_type"]:
        scrape_material("metal", driver, product_info_dict)

    return product_info_dict


def superjeweler_close_popup(driver):
    """
    Closes the popup on the SuperJeweler website.
    """
    try:
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.ID, "attentive_creative"))

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "closeIconContainer"))
        )
        driver.find_element(By.ID, "closeIconContainer").click()
        driver.switch_to.default_content()
    except NoSuchElementException:
        print("Popup close button or iframe not found.")
    except TimeoutException:
        print("Timed out waiting for popup to be clickable.")


def superjeweler_change_items_per_page(driver, item_count):
    """
    Changes the number of items per page on the SuperJeweler website.
    """
    try:
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ss-items"))
        )
        Select(select_element).select_by_value(str(item_count))
    except NoSuchElementException:
        print("Dropdown for changing items per page not found.")
    except TimeoutException:
        print("Timed out waiting for the dropdown.")


def reeds_change_items_per_page(driver, item_count):
    """
    Changes the number of items per page on the Reeds website.
    """
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rfk_nview")))

    dropdown = driver.find_element(By.CLASS_NAME, "rfk_nview")
    dropdown.click()

    time.sleep(2)
    option_96 = driver.find_element(
        By.XPATH, "//li[contains(text(), '{item_count}')]".format(item_count=item_count)
    )
    option_96.click()


def get_superjeweler_next_page(driver, page_number):
    """
    Navigates to the next page on the SuperJeweler website.
    """
    try:
        driver.execute_script(f"setPage({page_number})")
        time.sleep(2)
        return False
    except WebDriverException:
        print(f"Failed to load page {page_number}")
        return True


def get_reeds_next_page(driver, page_number):
    """
    Navigates to the next page on the Reeds website.
    """
    try:
        all_next_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "rfk_next"))
        )

        last_next_button = all_next_buttons[-1]
        last_next_button.click()
        time.sleep(2)
        return False
    except WebDriverException:
        print(f"Failed to load page {page_number}")
        return True


def click_material_filter(type_key, driver, material_id):
    """
    Clicks on a material filter on the website.
    """
    if type_key == "stone":
        material_id = f"gemstone_{material_id}"
    else:
        material_id = f"metal_type_{material_id}"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, material_id)))
    driver.find_element(By.ID, material_id).click()


def scrape_superjeweler_reeds(retailer_items, results_per_page):
    """
    Scrapes earring product data from a retailer's website.
    """

    def navigate_next_page(driver, retailer_items, page_number):
        """
        Navigates to the next page of products on the retailer's website.
        """
        if retailer_items["name"] == "superjeweler":
            return not get_superjeweler_next_page(driver, page_number)
        elif retailer_items["name"] == "reeds":
            return not get_reeds_next_page(driver, page_number)

    def scrape_responsive_material(type_key, driver, product_info_dict, material):
        """
        Scrapes material data from the retailer's website.
        """
        page_number = 1
        while True:
            time.sleep(2)
            website_lazy_loading(driver)

            out_of_products = get_product_info(
                driver,
                product_info_dict,
                retailer_items,
                results_per_page,
                [type_key, material],
            )

            if out_of_products:
                if retailer_items["name"] == "superjeweler":
                    get_superjeweler_next_page(driver, 1)
                break

            if not navigate_next_page(driver, retailer_items, page_number):
                break
            page_number += 1

    product_info_dict = {}
    driver.get(retailer_items["url"])

    if retailer_items["name"] == "superjeweler":
        superjeweler_close_popup(driver)
        superjeweler_change_items_per_page(driver, 240)
    elif retailer_items["name"] == "reeds":
        reeds_change_items_per_page(driver, "48")

    type_counter = 0
    for material in retailer_items["stone_type"]:
        time.sleep(3)
        click_material_filter("stone", driver, type_counter)
        scrape_responsive_material("stone", driver, product_info_dict, material)
        click_material_filter("stone", driver, type_counter)
        type_counter += 1

    type_counter = 0
    for material in retailer_items["metal_type"]:
        time.sleep(3)
        click_material_filter("metal", driver, type_counter)
        scrape_responsive_material("metal", driver, product_info_dict, material)
        click_material_filter("metal", driver, type_counter)
        type_counter += 1


if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    driver = uc.Chrome(use_subprocess=True, options=options)

    zales_earrings = {}

    # banana = retailer_earring_data_scraper(zales_items, 30, 0, 1)
    # pear = retailer_earring_data_scraper(jomashop_items, 50, 1, 1)
    # apple = retailer_earring_data_scraper(ross_simons_items, 110, 0, 120)
    kiwi = scrape_superjeweler_reeds(superjeweler_items, 235)
    # grape = scrape_superjeweler_reeds(reeds_items, 48, 1)

    try:
        driver.close()
        driver.quit()
    except:
        pass


# pear = retailer_earring_data_scraper(jomashop_items, 50, 1, 1)

# pineapple = retailer_earring_data_scraper(jared_items, 30, 0, 1)
# blueberry = retailer_earring_data_scraper(kay_items, 30, 0, 1)
