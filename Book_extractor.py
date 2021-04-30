# -*- coding: utf-8 -*-

import time
from bs4 import BeautifulSoup
import requests
import csv
import os

from progress.bar import Bar, IncrementalBar

'''
==================================================
Extraction des différentes informations des livres
==================================================
'''


def convert_description(div, extract):
    '''
    Reçoit le lien de la div contenant potentiellement la description et l'extraction du site
    :param div: div repérant la présence de la description
    :param extract: résultat du request sur l'url du site
    :return: description sinon "no description"
    '''
    soup = BeautifulSoup(extract.content, "html.parser")
    if div:
        return soup.select('article > p')[0].text.replace(',', '')
    else:
        return 'no description'


def extract_img(img):
    '''
    Extrait l'url de l'image
    :param img: lien vers l'image
    :return: url complet de l'image
    '''
    image = img['src'].replace('../..', "http://books.toscrape.com")
    return image


def convert_rating_string(str):
    '''
    Convertit le nombre indiquant la note du livre contenu dans la "class"
    exemple : <p class="star-rating Four">
    :param str: "class" du <p>
    :return: note sous forme de chiffre (de 1 à 5)
    '''
    num_table = ['One', 'Two', 'Three', 'Four', 'Five']
    for i, numTable in enumerate(num_table):
        if str == numTable:
            return i + 1


def dl_image(url_img, titre, categorie):
    '''
    Crée un dossier dans le dossier de la catégorie de livre et portant le nom "Book_Cover"
    si celui-ci n'existe pas déjà
    Télécharge l'image via l'url
    Enregistre l'image dans le dossier "Book_Cover"
    :param url_img: url de l'image récupérée def extract_img(img)
    :param titre: titre du livre
    :param categorie: catégorie du livre
    :return: aucune information, l'image est enregistrée directement dans le dossier
    '''
    if not os.path.isdir('./Catégorie(s)/' + categorie + '/Book_Cover'):
        os.mkdir('./Catégorie(s)/' + categorie + '/Book_Cover')
    else:
        pass
    reponse = requests.get(url_img)
    img = url_img.replace('http://books.toscrape.com/media/cache/', '').replace('/', '_')
    open('./Catégorie(s)/' + categorie + '/Book_Cover/' + img, 'wb').write(reponse.content)


def extract_book(book_url):
    """ extraction of all categories """
    extract = requests.get(book_url)
    if extract.ok:
        soup = BeautifulSoup(extract.content, 'html.parser')
        product_page_url = book_url
        tr = soup.findAll('tr')
        universal_product_code = tr[0].find('td').text
        title = soup.find('h1').text.replace(':', '-').replace('/', '-').replace('"', '')
        price_including_tax = tr[2].find('td').text.replace('Â£', '£')
        price_excluding_tax = tr[3].find('td').text.replace('Â£', '£')
        number_available = tr[5].find('td').text
        div = soup.find('div', {'id': 'product_description'})
        product_description = convert_description(div, extract)
        review_rating = convert_rating_string(soup.findAll("p")[2]["class"][1])
        category = soup.find('ul').findAll('li')[2].text.strip()
        img = soup.find('div', {'class': 'item active'}).find('img')
        image_url = extract_img(img)

        return (product_page_url,
                universal_product_code,
                title, price_including_tax,
                price_excluding_tax,
                number_available,
                product_description,
                category,
                review_rating,
                image_url)


def write_book(listing, categorie):
    '''
    Reçoit les informations de chaque livre 1b1 et l'écrit dans le csv correspondant à sa catégorie
    :param listing: dict contenant toutes les informations du livre
    :return: rien - écriture dans un fichier csv
    '''

    '''Création du dossier qui recevra les différentes catégories'''
    if not os.path.isdir('./Catégorie(s)'):
        os.mkdir('./Catégorie(s)')
    else:
        pass

    '''Création d'un dossier livre si celui-ci n'existe pas déjà'''
    if not os.path.isdir('./Catégorie(s)/' + categorie):
        os.mkdir('./Catégorie(s)/' + categorie)
    else:
        pass

    with open('./Catégorie(s)/' + categorie + '/Book(s)_' + categorie + '.csv', 'w',
              encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')

        ''' Writing the header on .csv file'''
        writer.writerow(
            ["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax",
             "price_excluding_tax",
             "number_available", "product_description", "category", "review_rating", "image_url"])

        '''Writing all the line on .csv file'''
        print("Extraction de(s) " + str(len(listing)) + " livre(s) de la catégorie " + categorie)
        time.sleep(0.5)
        with IncrementalBar('Récupération des données', max=len(listing)) as bar:
            for product_page_url in listing:
                # récupération des donnés de livre
                (product_page_url,
                 universal_product_code,
                 title, price_including_tax,
                 price_excluding_tax,
                 number_available,
                 product_description,
                 category,
                 review_rating,
                 image_url) = extract_book(product_page_url)
                dl_image(image_url, title, category)

                # write row with books data
                writer.writerow([
                    product_page_url,
                    universal_product_code,
                    title, price_including_tax,
                    price_excluding_tax,
                    number_available,
                    product_description,
                    category,
                    review_rating,
                    image_url
                ])
                bar.next()
            '''s = open('./Catégorie(s)/' + categorie + '/Book(s)_' + categorie + '.csv', 'r',
                     encoding='utf-8').read()
            open('./Catégorie(s)/' + categorie + '/Book(s)_' + categorie + '2.csv', 'w',
                 encoding='utf-8-sig').write(s)'''
    print("")
