JBHIFI_selectors = {
    "title": ["div", "class", "_10ipotx7 _10ipotx7"],
    "price": ["div", "class", "PriceTag_actualWrapperDefault__1eb7mu9p"],
    "on_sale": ["div", "class", "_35s76zl"],
    "price_off": ["span", "class", "PriceTag_footerPriceWrapper__1eb7mu9l"],
}
# products = soup.find_all("div", class_="_10ipotx17 _10ipotx1a")

umart_selctors = {
    "title": ["div", "class", "goods_name"],
    "price": ["span", "class", "goods-price ele-goods-price"],
    "brand": ["span", "itemprop", "brand"],
    "availability": ["span", "class", "goods_stock"],
    "on_sale": ["span", "class", "is_hot_btn"],
    "price_off": ["span", "class", "discount"],
}

umart_categories = {
    "cases": "computer-parts/cases-139",
    "cooling": "computer-parts/cooling-191",
    "cpus": "computer-parts/cpu-processors-611",
    "gpus": "computer-parts/graphics-cards-gpu-610",
    "fans": "computer-parts/fans-and-accessories-669",
    "ram": "computer-parts/memory-ram-108",
    "mother_boards": "computer-parts/motherboards-104",
    "psus": "computer-parts/power-supply-psu-140",
    "sound_cards": "computer-parts/sound-cards-32",
    "ssds": "storage-devices/ssd-hard-drives-580",
    "hdds": "storage-devices/hard-drives-hdd-127",
    "headphones": "peripherals/headphones-147",
    "keyboards": "peripherals/keyboards-40",
    "microphones": "peripherals/microphones-496",
    "monitors": "peripherals/monitors-142",
    "mouses": "peripherals/mouse-mouse-pads-24",
    "mouse_pad": "peripherals/mouse-mouse-pads-24",
    "speakers": "peripherals/speakers-43",
    "webcams": "peripherals/web-cams-508",
}

# Need new function for brand
computer_alliance_selctors = {
    "title": ["h2", "class", "equalize"],
    "price": ["span", "class", "price"],
    "brand": ["span", "class", "None"],
    "availability": ["a", "class", ["instock", "lowstock"]],
    "on_sale": ["span", "class", "save"],
    "price_off": ["span", "class", "save"],
}

computer_alliance_categories = {
    "cases": "cases",
    "cooling": "cpu-cooling",
    "cpus": "cpus",
    "gpus": "graphics-cards",
    "fans": "case-fans",
    "ram": "desktop-ram",
    "mother_boards": "motherboards",
    "psus": "power-supplies",
    "sound_cards": "sound-cards",
    "ssds": "ssd-drives-internal",
    "hdds": "hard-drives-(3.5)",
    "headphones": "headphones-headsets",
    "keyboards": "keyboards",
    "microphones": "microphones",
    "monitors": "monitors",
    "mouses": "mice-input-devices",
    "mouse_pad": "mousepads",
    "speakers": "audio-speakers",
    "webcams": "webcams-laptops-pc",
}

# Need new function for brand and availability
center_com_selectors = {
    "title": ["div", "class", "product-title"],
    "price": ["span", "class", "actual-price"],
    "brand": ["span", "class", "None"],
    "availability": ["span", "class", ["instock", "preorder"]],
    "on_sale": ["span", "class", "old-price"],
    "price_off": ["span", "class", "old-price"],
}

center_com_categories = {
    "cases": "cases-no-psu-included",
    "cooling": "cooling",
    "cpus": "cpu-processors",
    "gpus": "nvidia-amd-graphics-cards",
    "fans": "case-fans",
    "ram": "memory-ram",
    "mother_boards": "motherboards",
    "psus": "power-supplies",
    "sound_cards": "sound-cards",
    "ssds": "solid-state-drives",
    "hdds": "internal-desktop-hard-drives",
    "headphones": "headphones-headsets",
    "keyboards": "keyboards",
    "microphones": "microphones",
    "monitors": "monitors",
    "mouses": "mice-input-devices",
    "mouse_pad": "mousepads",
    "speakers": "audio-speakers",
    "webcams": "webcams-laptops-pc",
}

pc_case_gear_selectors = {
    "title": ["a", "class", "product-title"],
    "price": ["span", "class", "price"],
    "brand": ["span", "class", "None"],
    "availability": ["span", "class", "tool-tip-wrapper"],
    "on_sale": ["span", "class", "None"],
    "price_off": ["span", "class", "None"],
}

pc_case_gear_categories = {
    "cases": "Cases",
    "cooling": "Cooling",
    "cpus": "CPUs",
    "gpus": "Graphics%20Cards",
    "fans": "Fans%20%26%20Accessories",
    "ram": "Memory",
    "mother_boards": "Motherboards",
    "psus": "Power%20Supplies",
    "sound_cards": "Sound%20Cards",
    "ssds": "Hard%20Drives%20%26%20SSDs",
    "hdds": "Hard%20Drives%20%26%20SSDs",
    "headphones": "Headphones",
    "keyboards": "Keyboards",
    "microphones": "Microphones",
    "monitors": "Monitors",
    "mouses": "Mice%20%26%20Mouse%20Pads",
    "mouse_pad": "Mice%20%26%20Mouse%20Pads",
    "speakers": "Speakers",
    "webcams": "Streaming%20%26%20Video%20Capture",
}

mwave_selectors = {
    "title": ["div", "class", "nameListView"],
    "price": ["div", "class", "current"],
    "brand": ["span", "class", "None"],
    "availability": ["a", "class", ["btnAddToCart", "btnRight"]],
    "on_sale": ["div", "class", "wasprice"],
    "price_off": ["div", "class", "wasprice"],
}

mwave_categories = {
    "cases": "cases",
    "cooling": "cooling",
    "cpus": "cpu",
    "gpus": "graphics card",
    "fans": "fans",
    "ram": "ram",
    "mother_boards": "motherboards",
    "psus": "power supply",
    "sound_cards": "sound cards",
    "ssds": "ssd",
    "hdds": "hdd",
    "headphones": "headphones",
    "keyboards": "keyboards",
    "microphones": "microphones",
    "monitors": "monitors",
    "mouses": "mouse",
    "mouse_pad": "mouse pad",
    "speakers": "speaker system",
    "webcams": "HD Webcam",
}
