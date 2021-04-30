import requests
from bs4 import BeautifulSoup
from Book_extractor import write_book

"""
=============================================
Extraction de tous les livres d'une catégorie
=============================================
"""

urls = []


def extract_books_in_cat(url, start_url):
    '''
    Va extraire tous les livres de la catégorie
    :param url: url de la catégorie
    :return: liste des urls de la catégorie
    '''
    reponse = requests.get(url)
    if reponse.ok:
        page = BeautifulSoup(reponse.content, 'html.parser')
        cat = page.find('ul').findAll('li')[2].text.strip()
        for ref in page.findAll('h3'):
            href = ref.find('a')
            url_exit = href['href'].replace("../../..", "http://books.toscrape.com/catalogue")
            urls.append(url_exit)
        try:
            end_url = page.find('li', {'class': 'next'}).find('a')['href']
            next_page = start_url + end_url
            extract_books_in_cat(next_page, start_url)
        except AttributeError:
            pass
    return urls


def stock_books_in_cat(url):
    '''
    Va extraire tous les livres de la catégorie concernée et les stockés dans [urls]
    :param url: url de la catégorie
    :return: liste dans laquelle il y aura toutes les urls des livres de la catégorie
    '''
    global category
    urls[:] = []
    request = requests.get(url)
    if request.ok:
        extract = BeautifulSoup(request.content, 'html.parser')
        category = extract.find('ul').findAll('li')[2].text.strip()
    start_url = url.replace("index.html", "")
    books_in_cat = extract_books_in_cat(url, start_url)
    write_book(books_in_cat, category)


def extract_one_book(url_book):
    '''
    Reçoit l'url du livre lors de l'extraction d'un seul livre via User_choice.py et extrait la catégorie avant
    d'envoyer cette url et la catégorie à write_book
    :param url_book: url du livre
    :return: rien - les informations sont transmises à write_book
    '''
    book = []
    book.append(url_book)
    ext_cat_book = requests.get(url_book)
    if ext_cat_book.ok:
        extract = BeautifulSoup(ext_cat_book.content, 'html.parser')
        category = extract.find('ul').findAll('li')[2].text.strip()
    write_book(book, category)
