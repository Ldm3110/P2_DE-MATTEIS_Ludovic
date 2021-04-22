import requests
from bs4 import BeautifulSoup
from Category_extractor import nb_pages

'''
=================================
Extraction de la totalité du site
=================================
'''


def extract_all_cat(url):
    page = requests.get(url)
    if page.ok:
        extract = BeautifulSoup(page.text, 'html.parser')
        ul = extract.find('ul', {'class': 'nav nav-list'}).find('ul')
        for adresse in ul.findAll('li'):
            hrefs = adresse.find('a')['href']
            url_cat = ("https://books.toscrape.com/" + hrefs)
            nb_pages(url_cat)
