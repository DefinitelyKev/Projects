from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from static_website_scraper_functions import website_lazy_loading, get_product_info


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


def dynamic_retailer_earring_scrape(driver, retailer_items, results_per_page):
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

    def scrape_dynamic_material(type_key, driver, product_info_dict, material):
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

    materials_list = [
        ["stone", retailer_items["stone_type"]],
        ["metal", retailer_items["metal_type"]],
    ]

    for type_key, materials in materials_list:
        type_counter = 0
        for material in materials:
            time.sleep(3)
            click_material_filter(type_key, driver, type_counter)
            scrape_dynamic_material(type_key, driver, product_info_dict, material)
            click_material_filter(type_key, driver, type_counter)
            type_counter += 1

    return product_info_dict
