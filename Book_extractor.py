from bs4 import BeautifulSoup
import requests
import csv
import os

'''
==================================================
Extraction des différentes informations des livres
==================================================
'''

dict_final = []
labels = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
          'price_excluding_tax',
          'number_available', 'product_description', 'category', 'review_rating', 'image_url']


def convert_description(div, extract):
    '''
    Reçoit le lien de la div contenant potentiellement la description et l'extraction du site
    :param div: div repérant la présence de la description
    :param extract: résultat du request sur l'url du site
    :return: description sinon "no description"
    '''
    soup = BeautifulSoup(extract.text, "html.parser")
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
    f = open('./Catégorie(s)/' + categorie + '/Book_Cover/' + titre + '.jpg', 'wb')
    f.write(reponse.content)
    f.close()


def extract_book(listing):
    for elem in listing:
        """ extraction of all categories """
        dict_book = {'product_page_url': '', 'universal_product_code (upc)': '', 'title': 'title',
                     'price_including_tax': '',
                     'price_excluding_tax': '', 'number_available': '',
                     'product_description': '', "category": '', 'review_rating': '',
                     'image_url': ''}
        extract = requests.get(elem)
        if extract.ok:
            soup = BeautifulSoup(extract.text, 'html.parser')
            dict_book['product_page_url'] = elem
            dict_book['title'] = soup.find('h1').text
            tr = soup.findAll('tr')
            dict_book['universal_product_code (upc)'] = tr[0].find('td').text
            dict_book['price_including_tax'] = tr[2].find('td').text.replace('Â£', '£')
            dict_book['price_excluding_tax'] = tr[3].find('td').text.replace('Â£', '£')
            dict_book['number_available'] = tr[5].find('td').text
            div = soup.find('div', {'id': 'product_description'})
            dict_book['product_description'] = convert_description(div, extract)
            dict_book['review_rating'] = convert_rating_string(soup.findAll("p")[2]["class"][1])
            dict_book['category'] = soup.find('ul').findAll('li')[2].text.strip()
            img = soup.find('div', {'class': 'item active'}).find('img')
            dict_book['image_url'] = extract_img(img)
            dict_final.append(dict_book)

            '''Création du dossier qui recevra les différentes catégories'''
            if not os.path.isdir('./Catégorie(s)'):
                os.mkdir('./Catégorie(s)')
            else:
                pass

            '''Création d'un dossier livre si celui-ci n'existe pas déjà'''
            if not os.path.isdir('./Catégorie(s)/' + dict_book['category']):
                os.mkdir('./Catégorie(s)/' + dict_book['category'])
            else:
                pass

            dl_image(dict_book['image_url'], dict_book['title'], dict_book['category'])

            ''' Create the .csv file  '''
            with open('./Catégorie(s)/' + dict_book['category'] + '/Book(s)_' + dict_book['category'] + '.csv', 'w',
                      encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=labels)
                ''' Writing the header on .csv file'''
                writer.writeheader()
                '''Writing all the line on .csv file'''
                for elem in dict_final:
                    writer.writerow(elem)
