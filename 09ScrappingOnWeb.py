# file 032simple_html.py ------------------------------------------------------
"""
We are at information era, and we must be able to seek and bring information
from many different sources. We'll learn about a library that helps us with this
job. Our souce? The internet!
"""

from bs4 import BeautifulSoup
# Many many things on internet are in html format, and we should be able to 
# read and seek for patterns to get the information
SIMPLE_HTML = '''<html>
<head>/<head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul> 
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)


find_title()

find_list_items()

find_subtitle()

find_other_paragraph()
# file 033middle_html.py ------------------------------------------------------

import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']
    print(item_name)


def find_item_link():
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator).attrs['href']
    print(item_link)


def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string
    pattern = '\£([0-9,]*\.[0-9]*)'
    price = re.search(pattern, item_price).group(1)
    price = float(price)
    print(price)


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']
    classes = [c for c in classes if c != 'star-rating']
    # rating_classes = filter(lambda x: x != 'star-rating', classes)
    print(classes[0])


find_item_name()
find_item_link()
find_item_price()
find_item_rating()
# file 034ParsingBetter.py ----------------------------------------------------
import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an
    item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = 'article.product_pod h3 a'
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = 'article.product_pod h3 a'
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = 'article.product_pod p.price_color'
        item_price = self.soup.select_one(locator).string
        pattern = '\£([0-9,]*\.[0-9]*)'
        price = re.search(pattern, item_price).group(1)
        price = float(price)
        return price

    @property
    def rating(self):
        locator = 'article.product_pod p.star-rating'
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        classes = [c for c in classes if c != 'star-rating']
        # rating_classes = filter(lambda x: x != 'star-rating', classes)
        return classes[0]


item = ParsedItem(ITEM_HTML)
print(item.price)
print(item.rating)
print(item.name)
print(item.link)
# file 035ParsingLevelMax.py --------------------------------------------------
import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParsedItemLocators:
    """
    Locators for an item in HTML page.

    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """

    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an
    item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        pattern = '\£([0-9,]*\.[0-9]*)'
        price = re.search(pattern, item_price).group(1)
        price = float(price)
        return price

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        classes = [c for c in classes if c != 'star-rating']
        # rating_classes = filter(lambda x: x != 'star-rating', classes)
        return classes[0]


item = ParsedItem(ITEM_HTML)
print(item.price)
print(item.rating)
print(item.name)
print(item.link)

# file 03RequestWebPage.py ----------------------------------------------------
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])
