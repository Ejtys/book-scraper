import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


import requests
from bs4 import BeautifulSoup


"""Scrape book from books.toscrape.com"""
class BookScraper:

    """Require url of book from book.toscrape.com website."""
    def __init__(self, url:str) -> None:
        self.soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    @property
    def title(self):
        return self.soup.select_one('li.active').string
    
    @property
    def description(self):
        return self.soup.select('article.product_page p')[3].string
    
    @property
    def category(self):
        return self.soup.select('div.page_inner li a')[2].string

    @property
    def price(self):
        p = self.soup.select_one('p.price_color').string
        return float(p[1:])

    @property
    def price_cents(self):
        return int(self.price * 100)
