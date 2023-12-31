base_urls = {
    "zales": "https://www.zales.com",
    "jared": "https://www.jared.com",
    "kay": "https://www.kay.com",
    "jomashop": "https://www.jomashop.com",
    "ross-simons": "https://www.ross-simons.com",
    "superjeweler": "https://www.superjeweler.com",
    "reeds": "https://www.reeds.com",
}


def initialize_retailer_items(name, url, selectors, stone_types, metal_types):
    """
    Initializes and returns a dictionary containing the retailer's scraping configuration.
    """
    return {
        "name": name,
        "url": url,
        "selectors": selectors,
        "stone_type": stone_types,
        "metal_type": metal_types,
    }


zales_stone_types = [
    "diamond",
    "lab-created diamond",
    "morganite",
    "sapphire",
    "pearl",
    "emerald",
    "ruby",
    "amethyst",
    "topaz",
    "opal",
    "garnet",
    "peridot",
    "citrine",
    "aquamarine",
    "tanzanite",
    "onyx",
    "spinel",
    "quartz",
    "multi",
    "alexandrite",
    "cubic zirconia",
    "birthstone",
]
zales_metal_types = [
    "gold",
    "sterling silver",
    "platinum",
    "stainless steel",
]

zales_kay_jared_selectors = {
    "product_boxes": ["div", {"class": "product-item-inner"}],
    "product_on_sale": ["div", {"class": "other-prices"}],
    "product_href": ["a", {"class": "thumb main-thumb"}],
    "image_src": ["img", {"class": "img-responsive with-border"}],
    "title": ["div", {"class": "name product-tile-description"}],
    "price": ["div", {"class": "price"}],
    "original_price": ["div", {"class": "original-price"}],
}

zales_items = initialize_retailer_items(
    "zales",
    "https://www.zales.com/earrings/womens-earrings/c/0104020100?icid=MEGA:EARRING_GENDER:LADIES&loadMore={page_number}",
    zales_kay_jared_selectors,
    zales_stone_types,
    zales_metal_types,
)

kay_stone_types = [
    "alexandrite",
    "amethyst",
    "apatite",
    "aquamarine",
    "citrine",
    "crystal",
    "cubic zirconia",
    "cultured pearl",
    "diamond",
    "lab-created diamond",
    "emerald",
    "garnet",
    "morganite",
    "mother of pearl",
    "multi",
    "onyx",
    "opal",
    "peridot",
    "quartz",
    "rhodolite",
    "ruby",
    "sapphire",
    "tanzanite",
    "topaz",
]

kay_metal_types = [
    "gold",
    "sterling silver",
    "platinum",
]

kay_items = initialize_retailer_items(
    "kay",
    "https://www.kay.com/earrings/womens-earrings/c/9000000197?icid=MM:EARRINGS:WOMENS&loadMore={page_number}",
    zales_kay_jared_selectors,
    kay_stone_types,
    kay_metal_types,
)

jared_stone_types = [
    "alexandrite",
    "amethyst",
    "aquamarine",
    "aquaprase",
    "birthstone",
    "chalcedony",
    "citrine",
    "diamond",
    "lab-created diamond",
    "emerald",
    "garnet",
    "moonstone",
    "morganite",
    "mother of pearl",
    "multi",
    "onyx",
    "opal",
    "pearl",
    "peridot",
    "quartz",
    "ruby",
    "sapphire",
    "tanzanite",
    "topaz",
    "tourmaline",
    "turquoise",
    "zircon",
]

jared_metal_types = [
    "gold",
    "platinum",
    "sterling silver",
]


jared_items = initialize_retailer_items(
    "jared",
    "https://www.jared.com/jewelry/earrings/c/7000000106?q=%3A_relevance_Ascending%3Agender_string%3AWOMEN&loadMore={page_number}",
    zales_kay_jared_selectors,
    jared_stone_types,
    jared_metal_types,
)

jomashop_stone_types = [
    "amethyst",
    "aquamarine",
    "black diamond",
    "blue topaz",
    "citrine",
    "cubic zirconia",
    "diamond",
    "diopside",
    "emerald",
    "garnet",
    "gemstone",
    "jade",
    "moissanite",
    "moonstone",
    "morganite",
    "opal",
    "pearl",
    "peridot",
    "quartz",
    "rubellite",
    "ruby",
    "sapphire",
    "spinel",
    "tanzanite",
    "topaz",
    "turquoise",
]

jomashop_metal_types = [
    "brass",
    "gold",
    "pewter",
    "platinum",
    "rhodium",
    "rose gold",
    "silver",
    "silver plated",
    "stainless steel",
    "sterling silver",
    "two-tone",
    "white gold",
    "yellow gold",
]

jomashop_items_selectors = {
    "product_boxes": ["div", {"class": "productItemBlock"}],
    "product_on_sale": ["div", {"class": "was-price-wrapper"}],
    "product_href": ["a", {"class": "productName-link"}],
    "image_src": ["img", {"class": "productImg"}],
    "title": ["span", {"class": "name-out-brand"}],
    "price": ["div", {"class": "now-price"}],
    "original_price": ["div", {"class": "was-wrapper"}],
}

jomashop_items = initialize_retailer_items(
    "jomashop",
    "https://www.jomashop.com/filters/jewelry?gender=Ladies&subtype=Earrings&p={page_number}",
    jomashop_items_selectors,
    jomashop_stone_types,
    jomashop_metal_types,
)


ross_simons_stone_types = [
    "agate",
    "amber",
    "amethyst",
    "aquamarine",
    "chalcedony",
    "citrine",
    "coral",
    "emerald",
    "garnet",
    "jade",
    "lapis",
    "larimar",
    "malachite",
    "mixed-stone",
    "moissanite",
    "moonstone",
    "morganite",
    "onyx",
    "opal",
    "peridot",
    "prasiolite",
    "quartz",
    "rhodolite",
    "ruby",
    "sapphire",
    "shell",
    "spinel",
    "tanzanite",
    "topaz",
    "tourmaline",
    "turquoise",
    "zircon",
    "pearls",
    "diamond",
    "cubic zirconia",
]

ross_simons_metal_types = [
    "gold",
    "sterling silver",
    "gold over silver",
    "other metal",
    "mixed metal",
    "platinum",
    "stainless steel",
]

ross_simons_items_selectors = {
    "product_boxes": ["div", {"class": "grid-tile"}],
    "product_on_sale": ["div", {"class": "price price-tier3"}],
    "product_href": ["a", {"class": "thumb-link rollover"}],
    "image_src": [
        "img",
        {"class": "c-product-tile__image-src lazy rollover-main-image"},
    ],
    "title": ["div", {"class": "product-name"}],
    "price": ["span", {"class": "c-product-pricing__sales__price"}],
    "original_price": ["div", {"class": "price price-tier3"}],
}

ross_simons_items = initialize_retailer_items(
    "ross_simons",
    "https://www.ross-simons.com/jewelry/earrings/?start={page_number}&sz=120",
    ross_simons_items_selectors,
    ross_simons_stone_types,
    ross_simons_metal_types,
)


superjeweler_stone_types = [
    "amethyst",
    "aquamarine",
    "black diamond",
    "black moissanite",
    "blue diamond",
    "blue topaz",
    "citrine",
    "cubic zirconia",
    "diamond",
    "emerald",
    "garnet",
    "green amethyst",
    "jade",
    "lab grown diamond",
    "lemon quartz",
    "marcasite",
    "moissanite",
    "morganite",
    "mystic topaz",
    "onyx",
    "opal",
    "pearl",
    "peridot",
    "pink sapphire",
    "pink topaz",
    "ruby",
    "sapphire",
    "smoky quartz",
    "tanzanite",
]

superjeweler_metal_types = [
    "white gold",
    "yellow gold",
    "rose gold",
    "platinum",
    "sterling silver",
    "rose gold plated silver",
]

superjeweler_items_selectors = {
    "product_boxes": ["div", {"class": "sj-grid-element"}],
    "product_on_sale": ["p", {"class": "regular-price-value"}],
    "product_href": ["a", {"class": "short_desc_container"}],
    "image_src": ["img", {"class": "star"}],
    "title": ["h6", {"class": "t-dgrey md-mb0 sm-mb0 xs-mb0"}],
    "price": ["p", {"class": "our-price-value"}],
    "original_price": ["p", {"class": "regular-price-value"}],
}

superjeweler_items = initialize_retailer_items(
    "superjeweler",
    "https://www.superjeweler.com/earrings",
    superjeweler_items_selectors,
    superjeweler_stone_types,
    superjeweler_metal_types,
)


reeds_stone_types = [
    "abalone shell",
    "amazonite",
    "amethyst",
    "aquamarine",
    "citrine",
    "crystal",
    "cubic zirconia",
    "diamond",
    "doublet",
    "drusy",
    "emerald",
    "garnet",
    "glass",
    "lab grown diamond",
    "lapis",
    "magnesite",
    "morganite",
    "mother of pearl",
    "multi stone",
    "onyx",
    "opal",
    "pearl",
    "peridot",
    "quartz",
    "rhodolite garnet",
    "ruby",
    "sapphire",
    "spinel",
    "swarovski crystals",
    "tanzanite",
    "topaz",
    "turquoise",
]

reeds_metal_types = [
    "brass",
    "gold",
    "gold filled",
    "gold plated",
    "gold tone",
    "gunmetal plated",
    "platinum",
    "rhodium plated",
    "rose gold",
    "rose gold plated",
    "rose gold tone",
    "ruthenium plated",
    "silver tone",
    "stainless steel",
    "sterling silver",
    "tri-tone",
    "two-tone",
    "white gold",
    "yellow gold",
]

reeds_items_selectors = {
    "product_boxes": ["div", {"class": "rfk_prodwrap"}],
    "product_on_sale": ["span", {"class": "original-price"}],
    "product_href": ["a", {"class": "rfk_container"}],
    "image_src": ["img", {"class": "rfk_image1"}],
    "title": ["span", {"itemprop": "name"}],
    "price": ["span", {"class": "final-price"}],
    "original_price": ["span", {"class": "original-price"}],
}

reeds_items = initialize_retailer_items(
    "reeds",
    "https://www.reeds.com/jewelry/earrings/all-earrings.html?genders=Ladies&rfk=1",
    reeds_items_selectors,
    reeds_stone_types,
    reeds_metal_types,
)
