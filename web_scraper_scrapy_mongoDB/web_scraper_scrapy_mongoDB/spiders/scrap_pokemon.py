import scrapy


class ScrapPokemonSpider(scrapy.Spider):
    name = "scrap_pokemon"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "myproject.middlewares.CustomProxyMiddleware": 350,
            "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 400,
        },
    }

    def parse(self, response):
        products = response.css(".product")

        for product in products:
            price_and_currency_element = product.css(".price *::text").getall()
            price = "".join(price_and_currency_element)

            yield {
                "name": product.css("h2::text").get(),
                "image": product.css("img").attrib["src"],
                "price": price,
                "url": product.css("a").attrib["href"],
            }

        next_page = response.css("a.next.page-numbers::attr(href)").get()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page))


class CustomProxyMiddleware(object):
    def __init__(self):
        self.proxy = (
            "https://api.proxynova.com/proxychecker/curl?proxy=103.162.154.20:8888"
        )

    def process_request(self, request, spider):
        if "proxy" not in request.meta:
            request.meta["proxy"] = self.proxy

    def get_proxy(self):
        return self.proxy
