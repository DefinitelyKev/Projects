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

# FEMALE ONLY

product_info = {
    "title": [],
    "price": [],
    "sale_price": [],
    "product_url": [],
    "image_url": [],
    "other": [],
    "type": [],
    "colour": [],
    "material": [],
    "sku": [],
}

types = ["earrings"]

# top 100 in rings, earrings, necklaces, bracelets, watches
# give filter to material such as gold, silver, diamond, etc.
# give price filter
# Find the biggest discount from orginal price compared to sale price

# Track product price over time and give top 5 item in price drop.
# Create a newsletter so that customers get updated discount. Such as sending top 3 discount of day


def get_product_info(driver, link_list, retailer_selectors, results_per_page):
    soup = BeautifulSoup(driver.page_source, "lxml")
    product_boxes = soup.find_all(*retailer_selectors["product_boxes"])

    for link in product_boxes:
        is_on_sale = link.find(*retailer_selectors["product_on_sale"])
        if is_on_sale:
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
            driver, link_list, retailer_items["selectors"], results_per_page
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


def superjeweler_change_items_per_page(driver, items_count):
    try:
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ss-items"))
        )
        Select(select_element).select_by_value(str(items_count))
    except NoSuchElementException:
        print("Dropdown for changing items per page not found.")
    except TimeoutException:
        print("Timed out waiting for the dropdown.")


def scrape_superjeweler(retailer_items, results_per_page, start_page_number):
    results_per_page = 220
    page_number = 1

    link_list = []
    url = "https://www.superjeweler.com/earrings"
    driver.get(url)

    superjeweler_close_popup(driver)
    superjeweler_change_items_per_page(driver, 240)

    while True:
        time.sleep(2)
        out_of_products = get_product_info(
            driver, link_list, retailer_items["selectors"], results_per_page
        )

        start_page_number += 1
        if out_of_products:
            break

        try:
            driver.execute_script(f"setPage({page_number})")
            time.sleep(2)
        except WebDriverException:
            print(f"Failed to load page {page_number}")
            break

    print(len(link_list))
    return link_list


def scrape_reeds():
    results_per_page = 48
    page_number = 1

    link_list = []
    url = (
        "https://www.reeds.com/jewelry/earrings/all-earrings.html?genders=Ladies&rfk=1"
    )
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rfk_nview")))

    dropdown = driver.find_element(By.CLASS_NAME, "rfk_nview")
    dropdown.click()

    time.sleep(3)

    option_96 = driver.find_element(By.XPATH, "//li[contains(text(), '48')]")
    option_96.click()

    time.sleep(3)

    while True:
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "lxml")

        product_boxes = soup.find_all("div", attrs={"class": "rfk_prodwrap"})

        for link in product_boxes:
            is_on_sale = link.find("span", attrs={"class": "original-price"})
            if is_on_sale:
                product_anchor = link.find_all(
                    "a", href=lambda href: href and "html" in href
                )
                href_link = product_anchor[0].get("href") if product_anchor else None
                link_list.append(href_link)
                print(href_link)

        if len(product_boxes) < results_per_page:
            print("No more products")
            break

        print(len(product_boxes))

        page_number += 1

        try:
            all_next_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "rfk_next"))
            )

            last_next_button = all_next_buttons[-1]
            last_next_button.click()
            time.sleep(2)
        except WebDriverException:
            print(f"Failed to load page {page_number}")
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
    ross_simons_url = (
        "https://www.ross-simons.com/jewelry/earrings/?start={page_number}&sz=120"
    )
    zales_url = "https://www.zales.com/earrings/c/0104000000?facetCode=gender_string&q=%3A_relevance_Ascending%3Agender_string%3ALADIES&text=&storePickup=&sameDayDelivery=false&gbapiv2=false&loadMore={page_number}"

    jomashop_url = "https://www.jomashop.com/jewelry.html?gender=Ladies&subtype=Earrings&p={page_number}"

    ross_simons_selectors = {
        "product_boxes": ["div", {"class": "grid-tile"}],
        "product_on_sale": ["div", {"class": "price price-tier3"}],
        "product_href": ["a", {"class": "thumb-link rollover"}],
    }

    zales_kay_jared_selectors = {
        "product_boxes": ["div", {"class": "product-item-inner"}],
        "product_on_sale": ["div", {"class": "other-prices"}],
        "product_href": ["a", {"class": "thumb main-thumb"}],
    }

    reeds_selectors = {
        "product_boxes": ["li", {"class": "rfk_product"}],
        "product_on_sale": ["span", {"class": "other-prices"}],
        "product_href": ["a", {"class": "rfk_container"}],
    }

    jomashop_items = {
        "name": "jomashop",
        "url": "https://www.jomashop.com/jewelry.html?gender=Ladies&subtype=Earrings&p={page_number}",
        "selectors": {
            "product_boxes": ["div", {"class": "productItemBlock"}],
            "product_on_sale": ["div", {"class": "was-price-wrapper"}],
            "product_href": ["a", {"class": "productName-link"}],
        },
    }

    superjeweler_items = {
        "name": "superjeweler",
        "url": "https://www.superjeweler.com/earrings",
        "selectors": {
            "product_boxes": ["div", {"class": "sj-grid-element"}],
            "product_on_sale": ["p", {"class": "regular-price-value"}],
            "product_href": ["a", {"class": "short_desc_container"}],
        },
    }

    scrape_reeds()
    # pear = scrape_reeds()
    # apple = earring_scraper_v1(ross_simons_url, 110, 120, ross_simons_selectors)
    # banana = earring_scraper_v1(zale_urls, 30, 1, zales_selectors)

    driver.quit()
