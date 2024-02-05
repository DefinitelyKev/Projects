base_urls = {
    "zales": "https://www.zales.com",
    "jared": "https://www.jared.com",
    "kay": "https://www.kay.com",
    "jomashop": "https://www.jomashop.com",
    "ross_simons": "https://www.ross-simons.com",
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
    "Diamond",
    "Lab-Created+Diamond",
    "No+Stone",
    "Morganite",
    "Sapphire",
    "Pearl",
    "Emerald",
    "Ruby",
    "Amethyst",
    "Topaz",
    "Opal",
    "Garnet",
    "Peridot",
    "Citrine",
    "Aquamarine",
    "Tanzanite",
    "Other",
    "Onyx",
    "Spinel",
    "Quartz",
    "Multi",
    "Alexandrite",
    "Cubic+Zirconia",
    "Birthstone",
]
zales_metal_types = [
    "Gold",
    "Sterling+Silver",
    "Platinum",
    "Other",
    "Stainless+Steel",
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
    "https://www.zales.com/earrings/c/0104000000?q=*%3A_relevance_Ascending%3Agender_string%3ALADIES%3A{type}Types_string_mv%3A{material}&loadMore={page_number}",
    zales_kay_jared_selectors,
    zales_stone_types,
    zales_metal_types,
)

kay_stone_types = [
    "Alexandrite",
    "Amethyst",
    "Apatite",
    "Aquamarine",
    "Citrine",
    "Crystal",
    "Cubic+Zirconia",
    "Cultured+Pearl",
    "Diamond",
    "Emerald",
    "Garnet",
    "Lab-Created+Diamond",
    "Morganite",
    "Mother+Of+Pearl",
    "Multi",
    "No+Stone",
    "Onyx",
    "Opal",
    "Other",
    "Peridot",
    "Quartz",
    "Rhodolite",
    "Ruby",
    "Sapphire",
    "Tanzanite",
    "Topaz",
]
kay_metal_types = [
    "Gold",
    "Sterling+Silver",
    "Platinum",
]

kay_items = initialize_retailer_items(
    "kay",
    "https://www.kay.com/earrings/womens-earrings/c/9000000197?q=*%3A_relevance_Ascending%3Agender_string%3AWOMEN%3A{type}Types_string_mv%3A{material}&loadMore={page_number}",
    zales_kay_jared_selectors,
    kay_stone_types,
    kay_metal_types,
)

jared_stone_types = [
    "Alexandrite",
    "Amethyst",
    "Aquamarine",
    "Aquaprase",
    "Birthstone",
    "Chalcedony",
    "Citrine",
    "Diamond",
    "Emerald",
    "Garnet",
    "Lab-Created+Diamond",
    "Moonstone",
    "Morganite",
    "Mother+Of+Pearl",
    "Multi",
    "No+Stone",
    "Onyx",
    "Opal",
    "Other",
    "Pearl",
    "Peridot",
    "Quartz",
    "Ruby",
    "Sapphire",
    "Tanzanite",
    "Topaz",
    "Tourmaline",
    "Turquoise",
    "Zircon",
]
jared_metal_types = [
    "Gold",
    "Platinum",
    "Sterling+Silver",
]


jared_items = initialize_retailer_items(
    "jared",
    "https://www.jared.com/jewelry/earrings/c/7000000106?q=*%3A_relevance_Ascending%3Agender_string%3AWOMEN%3A{type}Types_string_mv%3A{material}&loadMore={page_number}",
    zales_kay_jared_selectors,
    jared_stone_types,
    jared_metal_types,
)

jomashop_stone_types = [
    "Amethyst",
    "Aquamarine",
    "Black+Diamond",
    "Blue+Topaz",
    "Citrine",
    "Cubic+Zirconia",
    "Diamond",
    "Diopside",
    "Emerald",
    "Garnet",
    "Gemstone",
    "Jade",
    "Moissanite",
    "Moonstone",
    "Morganite",
    "None",
    "Opal",
    "Other",
    "Pearl",
    "Peridot",
    "Quartz",
    "Rubellite",
    "Ruby",
    "Sapphire",
    "Spinel",
    "Tanzanite",
    "Topaz",
    "Turquoise",
]
jomashop_metal_types = [
    "Brass",
    "Gold",
    "No+Metal+Type",
    "Pewter",
    "Platinum",
    "Rhodium",
    "Rose+Gold",
    "Silver",
    "Silver+Plated",
    "Stainless+Steel",
    "Sterling+Silver",
    "Two-Tone",
    "White+Gold",
    "Yellow+Gold",
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
    "https://www.jomashop.com/filters/jewelry?gender=Ladies&subtype=Earrings&{type}_type={material}&p={page_number}",
    jomashop_items_selectors,
    jomashop_stone_types,
    jomashop_metal_types,
)

# ross_simons_stone_type_sub_class = [
#     "gemstones",
#     "diamond",
#     "perals",
#     "faux_stone",
#     "other_stones",
# ]
ross_simons_stone_types = [
    "Agate",
    "Amber",
    "Amethyst",
    "Aquamarine",
    "Chalcedony",
    "Citrine",
    "Coral",
    "Emerald",
    "Garnet",
    "Jade",
    "Lapis",
    "Larimar",
    "Malachite",
    "Mixed-Stone",
    "Moissanite",
    "Moonstone",
    "Morganite",
    "Onyx",
    "Opal",
    "Peridot",
    "Prasiolite",
    "Quartz",
    "Rhodolite",
    "Ruby",
    "Sapphire",
    "Shell",
    "Spinel",
    "Tanzanite",
    "Topaz",
    "Tourmaline",
    "Turquoise",
    "Zircon",
    "Pearls",
    "Diamond",
    "Cubic+Zirconia",
    "Other+Stones",
]
ross_simons_metal_types = [
    "Gold",
    "Sterling+Silver",
    "Gold+Over+Silver",
    "Other+Metal",
    "Mixed+Metal",
    "Platinum",
    "Stainless+Steel",
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
    "https://www.ross-simons.com/jewelry/earrings/?prefn1={type}1&prefv1={material}&srule=sales-rank&start={page_number}&sz=120",
    ross_simons_items_selectors,
    ross_simons_stone_types,
    ross_simons_metal_types,
)

ross_simons_items.setdefault(
    "url_gemstone",
    "https://www.ross-simons.com/jewelry/earrings/?prefn1=stone2&prefv1=Gemstones%3B{material}&srule=sales-rank&start={page_number}&sz=120",
)
ross_simons_items.setdefault(
    "url_faux",
    "https://www.ross-simons.com/jewelry/earrings/?prefn1=stone2&prefv1=Faux%20Stone%3BCubic+Zirconia&srule=sales-rank&start={page_number}&sz=120",
)


superjeweler_stone_types = [
    "Amethyst",
    "Aquamarine",
    "Black+Diamond",
    "Black+Moissanite",
    "Blue+Diamond",
    "Blue+Topaz",
    "Citrine",
    "Cubic+Zirconia",
    "Diamond",
    "Emerald",
    "Garnet",
    "Green+Amethyst",
    "Jade",
    "Lab+Grown+Diamond",
    "Lemon+Quartz",
    "Marcasite",
    "Moissanite",
    "Morganite",
    "Mystic+Topaz",
    "Onyx",
    "Opal",
    "Pearl",
    "Peridot",
    "Pink+Sapphire",
    "Pink+Topaz",
    "Ruby",
    "Sapphire",
    "Smoky+Quartz",
    "Tanzanite",
]
superjeweler_metal_types = [
    "White+Gold",
    "Yellow+Gold",
    "Rose+Gold",
    "Platinum",
    "Sterling+Silver",
    "Rose+Gold+Plated+Silver",
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
    "Abalone+Shell",
    "Amazonite",
    "Amethyst",
    "Aquamarine",
    "Citrine",
    "Crystal",
    "Cubic+Zirconia",
    "Diamond",
    "Doublet",
    "Drusy",
    "Emerald",
    "Garnet",
    "Glass",
    "Lab+Grown+Diamond",
    "Lapis",
    "Magnesite",
    "Morganite",
    "Mother+Of+Pearl",
    "Multi+Stone",
    "No+Stone",
    "Onyx",
    "Opal",
    "Pearl",
    "Peridot",
    "Quartz",
    "Rhodolite+Garnet",
    "Ruby",
    "Sapphire",
    "Spinel",
    "Swarovski+Crystals",
    "Tanzanite",
    "Topaz",
    "Turquoise",
]
reeds_metal_types = [
    "Brass",
    "Gold+Filled",
    "Gold+Plated",
    "Gold+Tone",
    "Gunmetal+Plated",
    "Platinum",
    "Rhodium+Plated",
    "Rose+Gold",
    "Rose+Gold+Plated",
    "Rose+Gold+Tone",
    "Ruthenium+Plated",
    "Silver+Tone",
    "Stainless+Steel",
    "Sterling+Silver",
    "Tri-Tone",
    "Two-Tone",
    "White+Gold",
    "Yellow+Gold",
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
    "https://www.reeds.com/jewelry/earrings/all-earrings.html?{type}={material}&genders=Ladies&rfk=1",
    reeds_items_selectors,
    reeds_stone_types,
    reeds_metal_types,
)
