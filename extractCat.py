import requests
from bs4 import BeautifulSoup
from extractBook import extract_book

'''
========================================================
Extraction des différents url des livres d'une categorie
========================================================
'''


def extract_category(url):
    response = requests.get(url)
    if response.ok:
        url_cat = []
        soup = BeautifulSoup(response.text, 'html.parser')
        h3 = soup.findAll('h3')
        for ref in h3:
            href = ref.find('a')
            url_end = href['href'].replace("../../..", '')
            hrefs = "http://books.toscrape.com/catalogue" + url_end
            url_cat.append(hrefs)
            extract_book(hrefs)
