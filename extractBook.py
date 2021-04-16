from bs4 import BeautifulSoup
import requests
import csv

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


def convert_description(div, extract):
    soup = BeautifulSoup(extract.text, "html.parser")
    if div:
        dict_book['product_description'] = soup.select('article > p')[0].text.replace(',', '')
    else:
        dict_book['product_description'] = 'no description'


def extract_tr(tr):
    dict_book['universal_product_code (upc)'] = tr[0].find('td').text
    dict_book['price_including_tax'] = tr[2].find('td').text.replace('Â£', '£')
    dict_book['price_excluding_tax'] = tr[3].find('td').text.replace('Â£', '£')
    dict_book['number_available'] = tr[5].find('td').text


def extract_img(img):
    image = img['src'].replace('../..', '')
    url_begin = "http://books.toscrape.com"
    dict_book['image_url'] = url_begin + image


def convert_rating_string(str):
    """ Return the conversion in integer or an error message """
    num_table = ['One', 'Two', 'Three', 'Four', 'Five']
    for i, numTable in enumerate(num_table):
        if str == numTable:
            return i + 1


def extract_book(url_enter):
    """ extraction of all categories """
    extract = requests.get(url_enter)
    if extract.ok:
        soup = BeautifulSoup(extract.text, 'html.parser')
        dict_book['product_page_url'] = url_enter
        dict_book['title'] = soup.find('h1').text

        """ cherche et extrait les infos contenus dans les <tr> """
        tr = soup.findAll('tr')
        extract_tr(tr)

        """ extrait la description du livre via convert_description """
        div = soup.find('div', {'id': 'product_description'})
        convert_description(div, extract)

        """ transforme le nombre d'étoiles en un int via convert_rating_string """
        dict_book['review_rating'] = convert_rating_string(soup.findAll("p")[2]["class"][1])

        dict_book['category'] = soup.find('ul').findAll('li')[2].text.strip()

        """ extraction de l'url de l'image """
        img = soup.find('div', {'class': 'item active'}).find('img')
        extract_img(img)
        dict_final.append(dict_book)

        """ Create the .csv file  """
        with open('Book.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=labels)
            """ Writing the header on .csv file """
            writer.writeheader()
            """ Writing all the line on .csv file """
            for elem in dict_final:
                writer.writerow(elem)


url = "https://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html"
extract_book(url)
