import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from scrapers.scrape import scrape_all

if __name__ == '__main__':
    scrape_all()