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

if __name__=="__main__":
    bs = BookScraper('https://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html')
    print(bs.soup.select_one('p.price_color').string[1:])
    print(bs.price_cents)