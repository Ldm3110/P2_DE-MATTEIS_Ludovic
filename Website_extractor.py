import requests
from bs4 import BeautifulSoup
from Category_extractor import stock_books_in_cat

'''
=================================
Extraction de la totalité du site
=================================
'''


def extract_all_cat(url):
    '''
    Reçoit l'url de la page d'accueil du livre
    :param url:
    :return:
    '''
    page = requests.get(url)
    if page.ok:
        extract = BeautifulSoup(page.content, 'html.parser')
        ul = extract.find('ul', {'class': 'nav nav-list'}).find('ul')
        for adresse in ul.findAll('li'):
            hrefs = adresse.find('a')['href']
            url_cat = ("https://books.toscrape.com/" + hrefs)
            stock_books_in_cat(url_cat)
