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
#     "other": [],
#     "type": [],
#     "colour": [],
#     "material": [],
#     "sku": [],
# }

# types = ["earrings"]

# top 100 in rings, earrings, necklaces, bracelets, watches
# give filter to material such as gold, silver, diamond, etc.
# give price filter
# Find the biggest discount from orginal price compared to sale price

# Track product price over time and give top 5 item in price drop.
# Create a newsletter so that customers get updated discount. Such as sending top 3 discount of day


def get_product_info(driver, link_list, retailer_selectors, results_per_page, retailer):
    soup = BeautifulSoup(driver.page_source, "lxml")
    product_boxes = soup.find_all(*retailer_selectors["product_boxes"])

    for link in product_boxes:
        is_on_sale = link.find(*retailer_selectors["product_on_sale"])
        if is_on_sale:
            if retailer == "reeds":
                product_anchor = link.find_all(
                    "a", href=lambda href: href and "html" in href
                )
                href_link = product_anchor[0].get("href") if product_anchor else None
            else:
                product_anchor = link.find(*retailer_selectors["product_href"])
                href_link = product_anchor.get("href") if product_anchor else None

            link_list.append(href_link)
            print(href_link)

    print(len(product_boxes))
    if len(product_boxes) < results_per_page:
        "No more products"
        return True

    return False


def jomashop_lazy_loading(driver):
    for jomashop_y_axis in range(1000, 9000, 1000):
        driver.execute_script("window.scrollTo(0, " + str(jomashop_y_axis) + ")")
        time.sleep(0.5)


def retailer_earring_data_scraper(
    retailer_items, results_per_page, start_page_number, page_increment
):
    link_list = []

    while True:
        url = retailer_items["url"].format(page_number=start_page_number)
        driver.get(url)
        time.sleep(2)

        if retailer_items["name"] == "jomashop":
            jomashop_lazy_loading(driver)

        out_of_products = get_product_info(
            driver,
            link_list,
            retailer_items["selectors"],
            results_per_page,
            retailer_items["name"],
        )

        if out_of_products:
            break
        start_page_number += page_increment

    print(len(link_list))
    return link_list


def superjeweler_close_popup(driver):
    try:
        driver.switch_to.frame(
            driver.find_element(By.XPATH, "//iframe[@id='attentive_creative']")
        )

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
    try:
        driver.execute_script(f"setPage({page_number})")
        time.sleep(2)
        return False
    except WebDriverException:
        print(f"Failed to load page {page_number}")
        return True


def get_reeds_next_page(driver, page_number):
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


def scrape_superjeweler_reeds(retailer_items, results_per_page, page_number):
    link_list = []
    driver.get(retailer_items["url"])

    if retailer_items["name"] == "superjeweler":
        superjeweler_close_popup(driver)
        superjeweler_change_items_per_page(driver, 240)
    elif retailer_items["name"] == "reeds":
        reeds_change_items_per_page(driver, "48")

    while True:
        time.sleep(2)
        out_of_products = get_product_info(
            driver,
            link_list,
            retailer_items["selectors"],
            results_per_page,
            retailer_items["name"],
        )
        page_number += 1
        if out_of_products:
            break

        if retailer_items["name"] == "superjeweler":
            no_next_page = get_superjeweler_next_page(driver, page_number)
            if no_next_page:
                break
        elif retailer_items["name"] == "reeds":
            no_next_page = get_reeds_next_page(driver, page_number)
            if no_next_page:
                break

    print(len(link_list))


if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    driver = uc.Chrome(use_subprocess=True, options=options)

    banana = retailer_earring_data_scraper(zales_items, 30, 0, 1)
    # kiwi = scrape_superjeweler_reeds(superjeweler_items, 235, 1)
    # grape = scrape_superjeweler_reeds(reeds_items, 48, 1)
    # pear = retailer_earring_data_scraper(jomashop_items, 50, 1, 1)
    # apple = retailer_earring_data_scraper(ross_simons_items, 110, 0, 120)
    # pineapple = retailer_earring_data_scraper(jared_items, 30, 0, 1)
    # blueberry = retailer_earring_data_scraper(kay_items, 30, 0, 1)
    # apple = earring_scraper_v1(ross_simons_url, 110, 120, ross_simons_selectors)
    # banana = earring_scraper_v1(zale_urls, 30, 1, zales_selectors)

    driver.quit()
