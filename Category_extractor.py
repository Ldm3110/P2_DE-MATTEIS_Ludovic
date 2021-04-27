import requests
from bs4 import BeautifulSoup
from Book_extractor import write_book

"""
=============================================
Extraction de tous les livres d'une catégorie
=============================================
"""

list_choice = {
    "Travel": "travel_2",
    "Mystery": "mystery_3",
    "Historical Fiction": "historical-fiction_4",
    "Sequential Art": "sequential-art_5",
    "Classics": "classics_6",
    "Philosophy": "philosophy_7",
    "Romance": "romance_8",
    "Womens Fiction": "womens-fiction_9",
    "Fiction": "fiction_10",
    "Childrens": "childrens_11",
    "Religion": "religion_12",
    "Nonfiction": "nonfiction_13",
    "Music": "music_14",
    "Default": "default_15",
    "Science Fiction": "science-fiction_16",
    "Sports and Games": "sports-and-games_17",
    "Add a comment": "add-a-comment_18",
    "Fantasy": "fantasy_19",
    "New Adult": "new-adult_20",
    "Young Adult": "young-adult_21",
    "Science": "science_22",
    "Poetry": "poetry_23",
    "Paranormal": "paranormal_24",
    "Art": "art_25",
    "Psychology": "psychology_26",
    "Autobiography": "autobiography_27",
    "Parenting": "parenting_28",
    "Adult Fiction": "adult-fiction_29",
    "Humor": "humor_30",
    "Horror": "horror_31",
    "History": "history_32",
    "Food and Drink": "food-and-drink_33",
    "Christian Fiction": "christian-fiction_34",
    "Business": "business_35",
    "Biography": "biography_36",
    "Thriller": "thriller_37",
    "Contemporary": "contemporary_38",
    "Spirituality": "spirituality_39",
    "Academic": "academic_40",
    "Self Help": "self-help_41",
    "Historical": "historical_42",
    "Christian": "christian_43",
    "Suspense": "suspense_44",
    "Short Stories": "short-stories_45",
    "Novels": "novels_46",
    "Health": "health_47",
    "Politics": "politics_48",
    "Cultural": "cultural_49",
    "Erotica": "erotica_50",
    "Crime": "crime_51"
}

urls = []


def find_cat(v):
    '''
    reçoit le choix de l'utilisateur et va récupérer dans list_choice la forme
    de la catégorie de l'url
    :param v: choix de l'utilisateur - ex : Travel
    :return: catégorie dans l'url - ex : Travel -> travel_2
    '''
    for k, val in list_choice.items():
        if v == k:
            return val


def extract_books_in_cat(url):
    '''
    Va extraire tous les livres de la catégorie
    :param url: url de la catégorie
    :return: liste des urls de la catégorie
    '''
    reponse = requests.get(url)
    if reponse.ok:
        page = BeautifulSoup(reponse.text, 'html.parser')
        cat = page.find('ul').findAll('li')[2].text.strip()
        categorie = find_cat(cat)
        for ref in page.findAll('h3'):
            href = ref.find('a')
            url_exit = href['href'].replace("../../..", "http://books.toscrape.com/catalogue")
            urls.append(url_exit)
        try:
            end_url = page.find('li', {'class': 'next'}).find('a')['href']
            next_page = "https://books.toscrape.com/catalogue/category/books/" + categorie + '/' + end_url
            extract_books_in_cat(next_page)
        except AttributeError:
            pass
    return urls


def nb_pages(url):
    '''
    Va extraire tous les livres de la catégorie concernée et les stockés dans [urls]
    :param url: url de la catégorie
    :return: liste dans laquelle il y aura toutes les urls des livres de la catégorie
    '''
    urls[:] = []
    request = requests.get(url)
    if request.ok:
        extract = BeautifulSoup(request.text, 'html.parser')
        category = extract.find('ul').findAll('li')[2].text.strip()
    urls_in_cat = extract_books_in_cat(url)
    write_book(urls_in_cat, category)


def extract_url_category(choix):
    '''
    Lorsque l'utilisateur choisi d'extraire une catégorie dans User_choice.py
    il envoi le nom de la catégorie
    :param choix: str - ex : Travel
    :return: rien, une fois l'url formé il va être traité par nb_pages
    '''
    cat_url = "http://books.toscrape.com/catalogue/category/books/" + find_cat(choix) + "/index.html"
    nb_pages(cat_url)


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
        extract = BeautifulSoup(ext_cat_book.text, 'html.parser')
        category = extract.find('ul').findAll('li')[2].text.strip()
    write_book(book, category)
