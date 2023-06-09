import urllib


def get_retailer_name(url, logger):
    try:
        return urllib.parse.urlparse(url).netloc.split('.')[-2]
    except Exception as e:
        logger.error(f"ERROR - Unable to extract RETAILER NAME for URL: {url} | {type(e)}: {e}")
