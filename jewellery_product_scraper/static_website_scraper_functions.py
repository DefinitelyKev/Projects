from bs4 import BeautifulSoup
import time
import re
from re import sub


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


def static_retailer_earring_scraper(
    driver, retailer_items, results_per_page, starting_page, page_increment
):
    """
    Scrapes earring product data from a retailer's website.
    """

    def scrape_material(type_key, driver, product_info_dict):
        """
        Scrapes material data from the retailer's website.
        """
        page_number = starting_page
        while True:
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
