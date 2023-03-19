import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import requests
from bs4 import BeautifulSoup

from .bookScraper import BookScraper
from models.bookModel import Book


"""Getting links to books pages from each page."""
def get_links(url:str) ->list[str]:
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    l= []
    for e in soup.select('div.image_container a'):
        l.append("https://books.toscrape.com/catalogue/" + e.attrs['href'])
    return l


"""Needs book page url. Adds scraped data to db."""
def scrape_book_to_db(url:str):
    bs = BookScraper(url)

    b = Book(bs.title)
    b.category = bs.category
    b.description = bs.description
    b.price_cents = bs.price_cents
    b.save()
    print(b)

"""Scrape all books from a page."""
def scrape_page_to_db(url:str):
    links= get_links(url)

    for link in links:
        print(link)
        scrape_book_to_db(link)

def scrape_all():
    for i in range(50):
        link = f'https://books.toscrape.com/catalogue/page-{i+1}.html'
        print()
        print(link)
        scrape_page_to_db(link)


