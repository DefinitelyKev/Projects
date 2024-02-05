from urllib.parse import urlencode
import scrapy
from ..items import WebScraperPokemonItem

API_KEY = "1cf92351ea2ec051d9fc9a36e577c62a0e1ec1a2"


class ScrapPokemonSpider(scrapy.Spider):
    name = "scrap_pokemon"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"proxy": f"http://{API_KEY}:@proxy.zenrows.com:8001"},
            )

    def parse(self, response):
        products = response.css(".product")

        for product in products:
            try:
                name = product.css("h2::text").get()
                image_url = response.urljoin(product.css("img").attrib.get("src", ""))
                price = "".join(product.css(".price *::text").getall())
                product_url = response.urljoin(product.css("a").attrib.get("href", ""))

                product_obj = WebScraperPokemonItem(
                    name=name,
                    image_url=image_url,
                    price=price,
                    product_url=product_url,
                )

                yield product_obj

            except Exception as err:
                self.logger.error(f"Error parsing product: {err}")

        next_page = response.css("a.next.page-numbers::attr(href)").get()

        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
