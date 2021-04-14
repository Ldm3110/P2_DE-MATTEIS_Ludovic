import requests
from bs4 import BeautifulSoup
from extractBook import extract_book

'''
=================================
Extraction de la totalité du site
=================================
'''


def extract_all():
    url_all = []

    for i in range(1, 51):
        url = "https://books.toscrape.com/catalogue/category/books_1/page-" + str(i) + ".html"
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            h3 = soup.findAll('h3')
            for ref in h3:
                href = ref.find('a')
                url_end = href['href'].replace("../..", '')
                hrefs = "http://books.toscrape.com/catalogue" + url_end
                url_all.append(hrefs)
                extract_book(hrefs)
