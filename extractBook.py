from bs4 import BeautifulSoup
import requests
import csv
import os.path

'''
==================================================
Extraction des différentes informations des livres
==================================================
'''

dict_final = []
labels = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
          'price_excluding_tax',
          'number_available', 'product_description', 'category', 'review_rating', 'image_url']
dict_book = {'product_page_url': '', 'universal_product_code (upc)': '', 'title': 'title',
             'price_including_tax': '',
             'price_excluding_tax': '', 'number_available': '',
             'product_description': '', "category": '', 'review_rating': '',
             'image_url': ''}

""" extrait la description du livre via convert_description """


def convert_description(div, extract):
    soup = BeautifulSoup(extract.text, "html.parser")
    if div:
        dict_book['product_description'] = soup.select('article > p')[0].text.replace(',', '')
    else:
        dict_book['product_description'] = 'no description'


""" cherche et extrait les infos contenus dans les <tr> """


def extract_tr(tr):
    dict_book['universal_product_code (upc)'] = tr[0].find('td').text
    dict_book['price_including_tax'] = tr[2].find('td').text.replace('Â£', '£')
    dict_book['price_excluding_tax'] = tr[3].find('td').text.replace('Â£', '£')
    dict_book['number_available'] = tr[5].find('td').text


""" extraction de l'url de l'image """


def extract_img(img):
    url_img = img['src'].replace('../..', "http://books.toscrape.com")
    dict_book['image_url'] = url_img
    return url_img


""" transforme le nombre d'étoiles en un int via convert_rating_string """


def convert_rating_string(str):
    num_table = ['One', 'Two', 'Three', 'Four', 'Five']
    for i, numTable in enumerate(num_table):
        if str == numTable:
            return i + 1


""" Télécharge l'image et l'enregistre dans un dossier nommé Book_Cover """


def dl_image(url_img, titre):
    if not os.path.isdir('./' + dict_book['category'] + '/Book_Cover'):
        os.mkdir('./' + dict_book['category'] + '/Book_Cover')
    else:
        pass
    reponse = requests.get(url_img)
    f = open('./' + dict_book['category'] + '/Book_Cover/' + titre + '.jpg', 'wb')
    f.write(reponse.content)
    f.close()


""" Extrait toutes les infos du livre """


def extract_book(url_enter):
    """ extraction of all categories """
    extract = requests.get(url_enter)
    if extract.ok:
        soup = BeautifulSoup(extract.text, 'html.parser')
        dict_book['product_page_url'] = url_enter
        dict_book['title'] = soup.find('h1').text
        tr = soup.findAll('tr')
        extract_tr(tr)
        div = soup.find('div', {'id': 'product_description'})
        convert_description(div, extract)
        dict_book['review_rating'] = convert_rating_string(soup.findAll("p")[2]["class"][1])
        dict_book['category'] = soup.find('ul').findAll('li')[2].text.strip()
        img = soup.find('div', {'class': 'item active'}).find('img')
        image = extract_img(img)
        dict_final.append(dict_book)

        """ Création d'un dossier livre si celui-ci n'existe pas déjà """
        if not os.path.isdir('./' + dict_book['category']):
            os.mkdir('./' + dict_book['category'])
        else:
            pass

        dl_image(image, dict_book['title'])

        """ Create the .csv file  """
        with open('./' + dict_book['category'] + '/Book(s).csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=labels)
            """ Writing the header on .csv file """
            writer.writeheader()
            """ Writing all the line on .csv file """
            for elem in dict_final:
                writer.writerow(elem)


"""

''' url utilisé pour le test '''
url = "https://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html"
extract_book(url)

"""