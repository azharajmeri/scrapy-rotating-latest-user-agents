import scrapy

from EcommerceScraper.items import EcommercescraperItem
from EcommerceScraper.utils.custom_logging import setup_logger
from EcommerceScraper.utils.custom_selectors.scrapy_selectors import css_selector, css_get_all_selector
from EcommerceScraper.utils.spider_utils import get_retailer_name

# setting up the logger
logger = setup_logger('aritzia info logger', 'logs/aritzia_spider.log')


class AritziaSpider(scrapy.Spider):
    name = "aritzia_spider"
    allowed_domains = ["www.aritzia.com"]

    def start_requests(self):
        yield scrapy.Request(url=self.product_url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        BRAND_SELECTOR_PATH = "div.js-product-detail__product-brand.flex a::text"
        NAME_SELECTOR_PATH = "h1.js-product-detail__product-name.f1::text"
        PRICE_SELECTOR_PATH = "span.price-default span::text"
        IMAGES_SELECTOR_PATH = "div.js-product-detail__images-container a::attr(href)"

        brand = css_selector(response, BRAND_SELECTOR_PATH, 'BRAND NAME', logger)
        name = css_selector(response, NAME_SELECTOR_PATH, 'PRODUCT NAME', logger)
        price = css_selector(response, PRICE_SELECTOR_PATH, 'PRODUCT PRICE', logger)
        images = css_get_all_selector(response, IMAGES_SELECTOR_PATH, 'PRODUCT IMAGES', logger)

        item = EcommercescraperItem()
        item['product_name'] = name.strip("\n") if name else None
        item['brand_name'] = brand.strip("\n") if brand else None
        item['product_image'] = list(set(images))
        item['product_price'] = price
        item['retailer_name'] = get_retailer_name(response.url, logger)

        yield {"status": "success", "data": item}
