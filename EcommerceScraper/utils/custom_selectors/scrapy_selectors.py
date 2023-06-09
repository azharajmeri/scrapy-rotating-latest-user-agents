import logging

from scrapy.http.response.html import HtmlResponse

LOG_MESSAGE = "Unable to locate '%s' with '%s' selector '%s' in URL '%s': Element not found in the webpage"


def css_selector(response: HtmlResponse, selection_path: str, element: str, logger: logging.Logger):
    if not (value := response.css(selection_path).get()):
        logger.info(LOG_MESSAGE,
                    element, 'css', selection_path, response.url)
    return value


def css_get_all_selector(response: HtmlResponse, selection_path: str, element: str, logger: logging.Logger):
    if not (value := response.css(selection_path).getall()):
        logger.info(LOG_MESSAGE,
                    element, 'css', selection_path, response.url)
    return value


def xpath_selector(response: HtmlResponse, selection_path: str, element: str, logger: logging.Logger):
    if not (value := response.xpath(selection_path).get()):
        logger.info(LOG_MESSAGE,
                    element, 'xpath', selection_path, response.url)
    return value


def xpath_get_all_selector(response: HtmlResponse, selection_path: str, element: str, logger: logging.Logger):
    if not (value := response.xpath(selection_path).getall()):
        logger.info(LOG_MESSAGE,
                    element, 'xpath', selection_path, response.url)
    return value
