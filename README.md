# scrapy-rotating-latest-user-agents
Rotating user agent mechanism in Scrapy. By rotating the user agents, the project aims to enhance web scraping efficiency and bypass potential restrictions imposed by websites.

### Getting Started

This assumes that `python` is linked to valid installation of python and that `pip` is installed and `pip`is valid
for installing python packages.

Installing, creating and activating virtualenv

    $ pip install virtualenv
    $ python -m virtualenv venv
    $ source venv/bin/activate


Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

    $ pip install -r requirements.txt

### Starting the crawl request

```commandline
scrapy crawl aritzia_spider -a product_url="https://www.aritzia.com/intl/en/product/babitz-halter-top/106641.html?dwvar_106641_color=1274"
```

### RESULT
    {
        'status': 'success', 
        'data': {
            'brand_name': 'Babaton',
            'product_image': ['https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_off_b.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_off_c.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_on_a.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_on_b.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_on_e.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_on_c.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_on_d.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_off_d.jpg',
                       'https://aritzia.scene7.com/is/image/Aritzia/large/s23_01_a02_106641_1274_off_a.jpg'],
             'product_name': 'babitz halter top',
             'product_price': '$78',
             'retailer_name': 'aritzia'
        }
    }
