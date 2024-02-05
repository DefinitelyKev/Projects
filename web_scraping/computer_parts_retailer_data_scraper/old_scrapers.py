# def umart_scaper(retailer_find):
#     results_per_page = 120
#     for item_category, category_selector in umart_categories.items():
#         page_number = 1
#         while True:
#             umart_url = f"https://www.umart.com.au/pc-parts/{category_selector}?page={page_number}&mystock=1-7-6&sort=salenum&order=ASC&pagesize=3"

#             driver.get(umart_url)
#             time.sleep(2)

#             soup = BeautifulSoup(driver.page_source, "html.parser")

#             element, class_name = retailer_find["umart"]
#             products = soup.find_all(element, class_=class_name)

#             for product in products:
#                 product_dict[item_category].append(
#                     get_product_info(product, umart_selctors)
#                 )

#             if len(products) < results_per_page:
#                 break

#             page_number += 1

# def centercom_scraper(retailer_find):
#     results_per_page = 30
#     for item_category, category_selector in centercom_categories.items():
#         page_number = 1
#         while True:
#             centercom_url = f"https://www.centrecom.com.au/{category_selector}?orderby=20&viewmode=list&pagenumber={page_number}"

#             driver.get(centercom_url)
#             time.sleep(2)

#             soup = BeautifulSoup(driver.page_source, "html.parser")

#             element, class_name = retailer_find["centercom"]
#             products = soup.find_all(element, class_=class_name)

#             for product in products:
#                 product_info = get_product_info(product, centercom_selectors)

#                 product_info["brand"] = get_centercom_brand(product)
#                 product_info["availability"] = get_centercom_availbility(
#                     product, product_info["availability"]
#                 )

#                 print(product_info)
#                 product_dict[item_category].append(product_info)

#             if len(products) < results_per_page:
#                 break

#             page_number += 1

# def pccasegear_scraper(retailer_find):
#     results_per_page = 100000
#     for item_category, category_selector in pccasegear_categories.items():
#         page_number = 1
#         for sub_catergory in category_selector:
#             while True:
#                 pccasegear_url = (
#                     f"https://www.pccasegear.com/category/{sub_catergory}/{page_number}"
#                 )

#                 driver.get(pccasegear_url)
#                 time.sleep(2)

#                 soup = BeautifulSoup(driver.page_source, "html.parser")

#                 element, class_name = retailer_find["pccasegear"]
#                 products = soup.find_all(element, class_=class_name)

#                 for product in products:
#                     product_info = get_product_info(product, pccasegear_selectors)

#                     product_info["brand"] = get_product_brand(product_info)

#                     if product_info["availability"] == "Check back later!":
#                         product_info["availability"] = "Out of Stock"
#                     elif product_info["availability"] != "In stock":
#                         product_info["availability"] = "Preorder"
#                     else:
#                         product_info["availability"] = "In Stock"

#                     print(product_info)
#                     product_dict[item_category].append(product_info)

#                 if len(products) < results_per_page:
#                     break

#                 page_number += 1

# def mwave_scraper(retailer_find):
#     results_per_page = 40
#     for item_category, category_selector in mwave_categories.items():
#         page_number = 1
#         for sub_catergory in category_selector:
#             while True:
#                 mwave_url = f"https://www.mwave.com.au/{sub_catergory}/page-{page_number}?view=40&display=list"
#                 driver.get(mwave_url)
#                 time.sleep(2)

#                 soup = BeautifulSoup(driver.page_source, "html.parser")

#                 element, class_name = retailer_find["mwave"]
#                 products = soup.find_all(element, class_=class_name)

#                 for product in products:
#                     product_info = get_product_info(product, mwave_selectors)

#                     product_info["brand"] = get_product_brand(product_info)

#                     if product_info["availability"] == "Add to Cart":
#                         product_info["availability"] = "In Stock"

#                     print(product_info)
#                     product_dict[item_category].append(product_info)

#                 if len(products) < results_per_page:
#                     break

#                 page_number += 1

# def scorptec_scraper(retailer_find):
#     results_per_page = 30
#     for item_category, category_selector in scorptec_categories.items():
#         page_number = 1
#         for sub_catergory in category_selector:
#             while True:
#                 scorptec_url = f"https://www.scorptec.com.au/product/{sub_catergory}?page={page_number}"
#                 driver.get(scorptec_url)
#                 time.sleep(2)

#                 soup = BeautifulSoup(driver.page_source, "html.parser")

#                 element, class_name = retailer_find["scorptec"]
#                 products = soup.find_all(element, class_=class_name)

#                 for product in products:
#                     product_info = get_product_info(product, scorptec_selectors)

#                     product_info["brand"] = get_product_brand(product_info)

#                     if product_info["availability"] == "sold out" or "end of life":
#                         product_info["availability"] = "Out of Stock"
#                     elif "eta" in product_info["availability"]:
#                         product_info["availability"] = "Pre-order"
#                     else:
#                         product_info["availability"] = "In Stock"

#                     print(product_info)
#                     product_dict[item_category].append(product_info)

#                 if len(products) < results_per_page:
#                     break

#                 page_number += 1

# def umart_centercom_scraper(
#     retailer_find,
#     retailer,
#     retail_categories,
#     retail_selectors,
#     retail_url,
#     results_per_page,
# ):
#     for item_category, category_selector in retail_categories.items():
#         page_number = 1
#         while True:
#             driver.get(
#                 retail_url.format(
#                     category_selector=category_selector, page_number=page_number
#                 )
#             )
#             time.sleep(2)

#             soup = BeautifulSoup(driver.page_source, "html.parser")

#             element, class_name = retailer_find[retailer]
#             products = soup.find_all(element, class_=class_name)

#             for product in products:
#                 product_info = get_product_info(product, retail_selectors)

#                 if retailer == "centercom":
#                     product_info["brand"] = get_centercom_brand(product)
#                     product_info["availability"] = get_centercom_availbility(
#                         product, product_info["availability"]
#                     )

#                 print(product_info)
#                 product_dict[item_category].append(product_info)

#             if len(products) < results_per_page:
#                 break

#             page_number += 1

# umart_url = "https://www.umart.com.au/pc-parts/{sub_catergory}?page={page_number}&mystock=1-7-6&sort=salenum&order=ASC&pagesize=3"
# umart_results_per_page = 120

# centercom_url = "https://www.centrecom.com.au/{sub_catergory}?orderby=20&viewmode=list&pagenumber={page_number}"
# centercom_results_per_page = 30

# pccasegear_url = "https://www.pccasegear.com/category/{sub_catergory}/{page_number}"
# pccasegear_results_per_page = 999

# mwave_url = "https://www.mwave.com.au/{sub_catergory}/page-{page_number}?view=40&display=list"
# mwave_results_per_page = 40

# scorptec_url = (
#     "https://www.scorptec.com.au/product/{sub_catergory}?page={page_number}"
# )
# scoptec_results_per_page = 30
