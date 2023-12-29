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
from static_website_scraper_functions import (
    website_lazy_loading,
    get_product_info,
    construct_url,
)


# Helper functions
def wait_for_element(driver, locator, timeout=10, element_to_be_clickable=False):
    """
    Waits for a web element to be present or clickable, depending on the 'element_to_be_clickable' flag.
    """
    wait = WebDriverWait(driver, timeout)
    if element_to_be_clickable:
        return wait.until(EC.element_to_be_clickable(locator))
    return wait.until(EC.presence_of_element_located(locator))


def click_element(driver, locator, sleep_time=2):
    """
    Waits for an element to be clickable and then clicks it. Includes a sleep delay after the click.
    """
    element = wait_for_element(driver, locator, element_to_be_clickable=True)
    time.sleep(sleep_time)
    element.click()


# Popup handling
def superjeweler_close_popup(driver):
    """
    Waits for an element to be clickable and then clicks it. Includes a sleep delay after the click.
    """
    try:
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.ID, "attentive_creative"))
        click_element(driver, (By.ID, "closeIconContainer"))
        driver.switch_to.default_content()

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Exception in closing popup: {e}")


def get_reeds_close_pop_up(driver):
    """
    Closes the cookie acceptance pop-up on the Reeds website, if it appears.
    """
    try:
        click_element(driver, (By.CLASS_NAME, "btn-cookie-accept"))

    except TimeoutException as e:
        print(f"Exception in closing pop-up: {e}")


# Changing items per page
def change_items_per_page(driver, item_count, retailer):
    """
    Changes the number of items displayed per page on a retailer's website.
    """
    try:
        if retailer == "superjeweler":
            select_element = wait_for_element(driver, (By.ID, "ss-items"))
            Select(select_element).select_by_value(str(item_count))

        elif retailer == "reeds":
            click_element(driver, (By.CLASS_NAME, "rfk_nview"))
            dropdown_selector = f"//li[contains(text(), '{item_count}')]"
            click_element(driver, (By.XPATH, dropdown_selector))

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Exception in changing items per page: {e}")


# Page navigation
def get_next_page(driver, retailer, page_number):
    """
    Navigates to the next page of a retailer's website.
    """
    try:
        if retailer == "superjeweler":
            driver.execute_script(f"setPage({page_number})")
        elif retailer == "reeds":
            time.sleep(2)
            wait = WebDriverWait(driver, 10)
            next_buttons = wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "rfk_next"))
            )

            next_buttons[-1].click()
        time.sleep(2)
        return False
    except WebDriverException as e:
        print(f"Exception in navigating to next page: {e}")
        return True


# Material filter selection
def click_material_filter(type_key, driver, material_id, retailer_name):
    """
    Selects a specific material filter on the retailer's website.
    """
    if retailer_name == "superjeweler":
        time.sleep(2)
        if type_key == "stone":
            material_id = f"gemstone_{material_id}"
        else:
            material_id = f"metal_type_{material_id}"
        click_element(driver, (By.ID, material_id))


# Main dynamic scraping function
def dynamic_retailer_earring_scrape(driver, retailer_items, results_per_page):
    """
    Scrapes earring product data dynamically from a retailer's website based on the specified material types.
    """

    def scrape_dynamic_material(type_key, driver, product_info, material):
        """
        Helper function to scrape product data for a specific material type.
        """
        page_number = 1
        is_initial_url = True
        while True:
            if retailer_name == "reeds" and is_initial_url:
                url = construct_url(retailer_items, type_key, material, page_number)
                driver.get(url)

            time.sleep(2)
            if retailer_name != "reeds":
                website_lazy_loading(driver)

            out_of_products = get_product_info(
                driver,
                product_info,
                retailer_items,
                results_per_page,
                [type_key, material],
            )

            page_number += 1
            is_initial_url = False

            if out_of_products:
                if retailer_name == "superjeweler":
                    get_next_page(driver, retailer_name, 1)
                break

            if get_next_page(driver, retailer_name, page_number):
                break

    product_info = {}
    retailer_name = retailer_items["name"]
    driver.get(retailer_items["url"])

    if retailer_name == "superjeweler":
        superjeweler_close_popup(driver)
        change_items_per_page(driver, 240, "superjeweler")
    elif retailer_name == "reeds":
        get_reeds_close_pop_up(driver)

    materials_list = [
        ["stone", retailer_items["stone_type"]],
        ["metal", retailer_items["metal_type"]],
    ]

    for type_key, materials in materials_list:
        for type_counter, material in enumerate(materials):
            if retailer_name == "superjeweler":
                click_material_filter(type_key, driver, type_counter, retailer_name)
            scrape_dynamic_material(type_key, driver, product_info, material)
            if retailer_name == "superjeweler":
                click_material_filter(type_key, driver, type_counter, retailer_name)

    return product_info
