zales_kay_jared_selectors = {
    "product_boxes": ["div", {"class": "product-item-inner"}],
    "product_on_sale": ["div", {"class": "other-prices"}],
    "product_href": ["a", {"class": "thumb main-thumb"}],
}

zales_items = {
    "name": "zales",
    "url": "https://www.zales.com/earrings/c/0104000000?facetCode=gender_string&q=%3A_relevance_Ascending%3Agender_string%3ALADIES&text=&storePickup=&sameDayDelivery=false&gbapiv2=false&loadMore={page_number}",
    "selectors": zales_kay_jared_selectors,
}

kay_items = {
    "name": "kay",
    "url": "https://www.kay.com/guest-appreciation-sale/c/9000000931?facetCode=gender_string&q=%3A_relevance_Ascending%3AjewelrySearchType_string%3AEarrings%3Agender_string%3AWOMEN&text=&storePickup=&sameDayDelivery=false&gbapiv2=false&loadMore={page_number}",
    "selectors": zales_kay_jared_selectors,
}

jared_items = {
    "name": "jared",
    "url": "https://www.jared.com/jewelry/earrings/c/7000000106?facetCode=gender_string&q=%3A_relevance_Ascending%3Agender_string%3AWOMEN&text=&storePickup=&sameDayDelivery=false&gbapiv2=false&loadMore={page_number}",
    "selectors": zales_kay_jared_selectors,
}

ross_simons_items = {
    "name": "ross_simons",
    "url": "https://www.ross-simons.com/jewelry/earrings/?start={page_number}&sz=120",
    "selectors": {
        "product_boxes": ["div", {"class": "grid-tile"}],
        "product_on_sale": ["div", {"class": "price price-tier3"}],
        "product_href": ["a", {"class": "thumb-link rollover"}],
    },
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

reeds_items = {
    "name": "reeds",
    "url": "https://www.reeds.com/jewelry/earrings/all-earrings.html?genders=Ladies&rfk=1",
    "selectors": {
        "product_boxes": ["div", {"class": "rfk_prodwrap"}],
        "product_on_sale": ["span", {"class": "original-price"}],
        "product_href": ["a", {"class": "rfk_container"}],
    },
}
