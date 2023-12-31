from bs4 import BeautifulSoup
import time
import re
from re import sub
from retailer_selectors import base_urls


def get_product_url(retailer_name, box, retailer_selectors):
    """
    Extracts the product URL from a BeautifulSoup 'box' element based on the retailer's specifics.
    """
    if retailer_name == "reeds":
        product_anchor = box.find_all("a", href=lambda href: href and "html" in href)
        return product_anchor[0].get("href") if product_anchor else None

    product_anchor = box.find(*retailer_selectors["product_href"])
    return product_anchor.get("href") if product_anchor else None


def get_price(text):
    """
    Extracts the price from a text string.
    """
    price_match = re.search(r"\d+(\,\d{1,3})*(.\d+)?", text).group()
    return (
        (price_match, float(sub(r"[^\d.]", "", price_match)))
        if price_match
        else (None, None)
    )


def extract_product_details(box, retailer_items):
    """
    Extracts product details from a BeautifulSoup 'box' element.
    """

    def get_element_text(box, selector):
        """
        Get element and check if exists
        """
        element = box.find(*selector)
        return element.text.strip() if element else None

    retailer_name = retailer_items["name"]
    if retailer_name == "ross_simons":
        retailer_name = "ross-simons"

    retailer_selectors = retailer_items["selectors"]

    price_text = get_element_text(box, retailer_selectors["price"])
    original_price_text = get_element_text(box, retailer_selectors["original_price"])

    price, num_price = get_price(price_text)
    original_price, num_original_price = get_price(original_price_text)

    sale_discount = (
        round(((num_original_price - num_price) / (num_original_price)) * 100, 1)
        if num_original_price
        else None
    )

    image_src = box.find(*retailer_selectors["image_src"])
    image_url = image_src.get("src") if image_src else None
    product_url = get_product_url(retailer_name, box, retailer_selectors)

    base_url = base_urls.get(retailer_name, "")

    if retailer_name not in image_url:
        image_url = f"{base_url}{image_url}" if image_url else None
    product_url = f"{base_url}{product_url}" if product_url else None

    return {
        "price": price,
        "original_price": original_price,
        "sale_discount": sale_discount,
        "image_url": image_url,
        "product_url": product_url,
    }


def get_product_info(driver, product_info, retailer_items, results_per_page):
    """
    Scrapes product information from a web page.
    """
    soup = BeautifulSoup(driver.page_source, "lxml")
    retailer_selectors = retailer_items["selectors"]
    product_boxes = soup.find_all(*retailer_selectors["product_boxes"])

    on_sale_count = 0
    for box in product_boxes:
        try:
            on_sale = box.find(*retailer_selectors["product_on_sale"])
            if not on_sale:
                continue

            title = box.find(*retailer_selectors["title"]).text.strip()
            product_info[title] = extract_product_details(box, retailer_items)
            print(product_info[title])
            on_sale_count += 1

        except Exception as error:
            print(f"Error processing box: {error}")

    print("Found product_boxes: ", len(product_boxes))
    print("Number of products on sale: ", on_sale_count)
    return len(product_boxes) < results_per_page


def website_lazy_loading(driver):
    """
    Scrolls through website to load all products with lazy loading.
    """
    website_height = driver.execute_script("return document.body.scrollHeight")
    scroll_count = round(website_height, -3)

    for website_y_axis in range(1000, scroll_count, 1000):
        driver.execute_script(f"window.scrollTo(0, {website_y_axis})")
        time.sleep(0.3)


def static_retailer_earring_scraper(
    driver, retailer_items, results_per_page, starting_page, page_increment
):
    """
    Scrapes earring product data from a retailer's website.
    """

    def scrape_material(driver, product_info):
        """
        Scrapes material data from the retailer's website.
        """
        page_number = starting_page
        while True :
            url = retailer_items["url"].format(page_number=page_number)
            driver.get(url)
            time.sleep(2)

            website_lazy_loading(driver)
            out_of_products = get_product_info(
                driver,
                product_info,
                retailer_items,
                results_per_page,
            )

            if out_of_products:
                break
            page_number += page_increment

    product_info = {}
    scrape_material(driver, product_info)
    return product_info
