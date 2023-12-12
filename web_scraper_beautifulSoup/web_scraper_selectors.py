umart_selctors = {
    "title": ["div", "class", "goods_name"],
    "price": ["span", "class", "goods-price ele-goods-price"],
    "brand": ["span", "itemprop", "brand"],
    "availability": ["span", "class", "goods_stock"],
    "on_sale": ["span", "class", "is_hot_btn"],
    "price_off": ["span", "class", "discount"],
}

umart_categories = {
    "cases": ["computer-parts/cases-139"],
    "cooling": ["computer-parts/cooling-191"],
    "cpus": ["computer-parts/cpu-processors-611"],
    "gpus": ["computer-parts/graphics-cards-gpu-610"],
    "fans": ["computer-parts/fans-and-accessories-669"],
    "ram": ["computer-parts/memory-ram-108"],
    "mother_boards": ["computer-parts/motherboards-104"],
    "psus": ["computer-parts/power-supply-psu-140"],
    "sound_cards": ["computer-parts/sound-cards-32"],
    "ssds": ["storage-devices/ssd-hard-drives-580"],
    "hdds": ["storage-devices/hard-drives-hdd-127"],
    "headphones": ["peripherals/headphones-147"],
    "keyboards": ["peripherals/keyboards-40"],
    "microphones": ["peripherals/microphones-496"],
    "monitors": ["peripherals/monitors-142"],
    "mouses": ["peripherals/mouse-mouse-pads-24"],
    "speakers": ["peripherals/speakers-43"],
    "webcams": ["peripherals/web-cams-508"],
}

# Need new function for brand
computeralliance_selectors = {
    "title": ["h2", "class", "equalize"],
    "price": ["span", "class", "price"],
    "brand": ["span", "class", "None"],
    "availability": ["a", "class", ["instock", "lowstock"]],
    "on_sale": ["span", "class", "save"],
    "price_off": ["span", "class", "save"],
}

computeralliance_categories = {
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
    "speakers": "audio-speakers",
    "webcams": "webcams-laptops-pc",
}

# Need new function for brand and availability
centercom_selectors = {
    "title": ["div", "class", "product-title"],
    "price": ["span", "class", "actual-price"],
    "brand": ["span", "class", "None"],
    "availability": ["span", "class", ["instock", "preorder"]],
    "on_sale": ["span", "class", "old-price"],
    "price_off": ["span", "class", "old-price"],
}

centercom_categories = {
    "cases": ["cases-no-psu-included"],
    "cooling": ["cooling"],
    "cpus": ["cpu-processors"],
    "gpus": ["nvidia-amd-graphics-cards"],
    "fans": ["case-fans"],
    "ram": ["memory-ram"],
    "mother_boards": ["motherboards"],
    "psus": ["power-supplies"],
    "sound_cards": ["sound-cards"],
    "ssds": ["solid-state-drives"],
    "hdds": ["internal-desktop-hard-drives"],
    "headphones": ["headphones-headsets"],
    "keyboards": ["keyboards"],
    "microphones": ["microphones"],
    "monitors": ["monitors"],
    "mouses": ["mice-input-devices"],
    "speakers": ["audio-speakers"],
    "webcams": ["webcams-laptops-pc"],
}

pccasegear_selectors = {
    "title": ["a", "class", "product-title"],
    "price": ["div", "class", "price"],
    "brand": ["span", "class", "None"],
    "availability": ["span", "class", "tool-tip-wrapper"],
    "on_sale": ["span", "class", "None"],
    "price_off": ["span", "class", "None"],
}

pccasegear_categories = {
    "cases": ["25_547/cases/all-models"],
    "cooling": ["207_23/cooling/cpu-cooling"],
    "cpus": [
        "187_2205/cpus/amd-am4-4000",
        "187_2138/cpus/amd-am4-5000",
        "187_2217/cpus/amd-am5-7000",
        "187_2110/cpus/intel-1200-10th-gen",
        "187_2180/cpus/intel-1700-12th-gen",
        "187_2219/cpus/intel-1700-13th-gen",
        "187_2260/cpus/intel-1700-14th-gen",
    ],
    "gpus": [
        "193_876/graphics-cards/nvidia-graphics-cards",
        "193_877/graphics-cards/amd-graphics-cards",
        "193_2225/graphics-cards/intel-graphics-cards",
        "193_1587/graphics-cards/accessories",
    ],
    "fans": ["9_1982/fans-accessories/all-models"],
    "ram": [
        "186_538/memory/all-ddr3-memory",
        "186_1782/memory/all-ddr4-memory",
        "186_2181/memory/all-ddr5-memory",
    ],
    "mother_boards": [
        "138_1874/motherboards/amd-socket-am4-2nd-gen",
        "138_2023/motherboards/amd-socket-am4-3rd-gen",
        "138_2220/motherboards/amd-socket-am5",
        "138_2153/motherboards/intel-1200-11th-gen",
        "138_2179/motherboards/intel-1700-12th-gen",
        "138_2221/motherboards/intel-1700-13th-gen"
        "138_2259/motherboards/intel-1700-14th-gen",
        "138_1877/motherboards/motherboard-accessories",
    ],
    "psus": ["15_535/power-supplies/all-models"],
    "sound_cards": ["211/sound-cards"],
    "ssds": ["210_902/hard-drives-ssds/solid-state-drives-ssd"],
    "hdds": ["210_344/hard-drives-ssds/3-5-hard-drives"],
    "headphones": ["116_998/headphones/all-models"],
    "keyboards": ["113_257/keyboards/all-keyboards"],
    "microphones": ["2048_2049/microphones/all-microphone-models"],
    "monitors": ["558_1094/monitors/all-monitor-models"],
    "mouses": ["258_698/mice-mouse-pads/all-models"],
    "speakers": ["567_571/speakers/all-models"],
    "webcams": ["1141/streaming-video-capture"],
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
    "cases": ["cases-enclosures/computer-cases-pc-cases"],
    "cooling": [
        "pc-cooling/cpu-fan-heatsinks",
        "pc-cooling/cpu-water-cooling",
    ],
    "cpus": [
        "cpu-processors/amd-desktop-cpu",
        "cpu-processors/intel-desktop-cpu",
    ],
    "gpus": [
        "graphics-cards/amd-graphics-cards",
        "graphics-cards/nvidia-graphics-cards",
        "graphics-cards/intel-video-cards",
    ],
    "fans": [
        "pc-cooling/case-fans",
        "pc-cooling/controllers-panels",
    ],
    "ram": [
        "memory/pc-ddr3",
        "memory/pc-ddr4",
        "memory/pc-ddr5",
    ],
    "mother_boards": [
        "motherboards/amd-compatible-motherboards",
        "motherboards/intel-compatible-motherboards",
    ],
    "psus": ["power-supplies/atx-power-supplies"],
    "sound_cards": ["audio/sound-cards"],
    "ssds": ["hdds/solid-state-drives-ssd"],
    "hdds": ["hdds/desktop-3.5-hdd-sata"],
    "headphones": ["audio/gaming-headsets"],
    "keyboards": ["input-devices/keyboards"],
    "microphones": ["audio/microphones"],
    "monitors": ["monitors"],
    "mouses": ["input-devices/computer-mouse"],
    "speakers": ["audio/speakers"],
    "webcams": ["input-devices/web-internet-cameras"],
}

scorptec_selectors = {
    "title": ["div", "class", "detail-product-title"],
    "price": ["div", "class", "detail-product-price"],
    "brand": ["span", "class", "None"],
    "availability": ["div", "class", "detail-product-stock status-box"],
    "on_sale": ["div", "class", "detail-product-save"],
    "price_off": ["div", "class", "detail-product-before-price"],
}

scorptec_categories = {
    "cases": ["cases/all-cases"],
    "cooling": ["cooling/cpu-coolers"],
    "cpus": [
        "cpu/intel10thgen",
        "cpu/intel-1200-11th-gen",
        "cpu/intel-1700-12th-gen",
        "cpu/intel-1700-13th-gen",
        "cpu/intel-1700-14th-gen",
        "cpu/intel-socket-1200",
        "cpu/intel-socket-1700",
        "cpu/amd-socket-am4",
        "cpu/amd-socket-am5",
        "cpu/amd-am4-5000",
        "cpu/amd-am5-7000",
        "cpu/amd-threadripper",
    ],
    "gpus": [
        "graphics-cards/amd",
        "graphics-cards/nvidia",
        "graphics-cards/intel",
        "graphics-cards/accessories",
    ],
    "fans": [
        "cooling/fans",
        "cooling/fan-controllers",
    ],
    "ram": [
        "memory/ddr5-desktop-memory",
        "memory/ddr4-desktop-memory",
        "memory/ddr3-desktop-memory",
    ],
    "mother_boards": [
        "motherboards/intel-socket-1200",
        "motherboards/intel-socket-1700",
        "motherboards/amd-socket-am4",
        "motherboards/amd-socket-am5",
        "motherboards/amd-threadripper",
        "motherboards/asrock-motherboards",
        "motherboards/asus-motherboards",
        "motherboards/gigabyte-motherboards",
        "motherboards/msi-motherboards",
    ],
    "psus": ["power-supplies/all-power-supplies"],
    "sound_cards": ["soundcards/internal"],
    "ssds": ["hard-drives-&-ssds/solid-state-drives-ssd"],
    "hdds": ["hard-drives-&-ssds/hdd-3.5-drives"],
    "headphones": ["headphones/all-headphones"],
    "keyboards": [
        "keyboards/mechanical-keyboards",
        "keyboards/non-mechanical-keyboards",
        "keyboards/keyboard-&-mouse-set",
        "keyboards/wireless-keyboards",
    ],
    "microphones": ["microphones/all-microphones"],
    "monitors": ["monitors/all-monitors"],
    "mouses": ["mouse-&-mouse-pads/mouse"],
    "speakers": ["speakers/all-speakers"],
    "webcams": ["web-cameras/web-cameras"],
}

retailer_info = {
    "umart": {
        "url": "https://www.umart.com.au/pc-parts/{sub_catergory}?page={page_number}&mystock=1-7-6&sort=salenum&order=ASC&pagesize=3",
        "div_find": ["div", "row goods-item"],
        "items_per_page": 120,
        "categories": umart_categories,
        "selectors": umart_selctors,
    },
    "centercom": {
        "url": "https://www.centrecom.com.au/{sub_catergory}?orderby=20&viewmode=list&pagenumber={page_number}",
        "div_find": ["div", "item-box"],
        "items_per_page": 30,
        "categories": centercom_categories,
        "selectors": centercom_selectors,
    },
    "pccasegear": {
        "url": "https://www.pccasegear.com/category/{sub_catergory}/{page_number}",
        "div_find": ["div", "product-container list-view"],
        "items_per_page": 999,
        "categories": pccasegear_categories,
        "selectors": pccasegear_selectors,
    },
    "mwave": {
        "url": "https://www.mwave.com.au/{sub_catergory}/page-{page_number}?view=40&display=list",
        "div_find": ["li", "listItem"],
        "items_per_page": 40,
        "categories": mwave_categories,
        "selectors": mwave_selectors,
    },
    "scorptec": {
        "url": "https://www.scorptec.com.au/product/{sub_catergory}?page={page_number}",
        "div_find": ["div", "row product-list-detail"],
        "items_per_page": 30,
        "categories": scorptec_categories,
        "selectors": scorptec_selectors,
    },
}
