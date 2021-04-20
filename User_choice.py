from Category_extractor import *
from Book_extractor import extract_book

"""
======================================================================
Interface utilisateur qui permettra de savoir ce qui doit être extrait
======================================================================
"""

cat_books = [
    "Travel",
    "Mystery",
    "Historical Fiction",
    "Sequential Art",
    "Classics",
    "Philosophy",
    "Romance",
    "Womens Fiction",
    "Fiction",
    "Childrens",
    "Religion",
    "Nonfiction",
    "Music",
    "Default",
    "Science Fiction",
    "Sports and Games",
    "Add a comment",
    "Fantasy",
    "New Adult",
    "Young Adult",
    "Science",
    "Poetry",
    "Paranormal",
    "Art",
    "Psychology",
    "Autobiography",
    "Parenting",
    "Adult Fiction",
    "Humor",
    "Horror",
    "History",
    "Food and Drink",
    "Christian Fiction",
    "Business",
    "Biography",
    "Thriller",
    "Contemporary",
    "Spirituality",
    "Academic",
    "Self Help",
    "Historical",
    "Christian",
    "Suspense",
    "Short Stories",
    "Novels",
    "Health",
    "Politics",
    "Cultural",
    "Erotica",
    "Crime"
]

""" Le choix est entre 1 et 4 - en fonction va déterminer la suite du programme """


def user_enter_choice(choix):
    '''
    Va contrôler que l'utilisateur ne renseigne qu'un chiffre de 1 à 4 sinon redemande un choix
    :param choix: par défaut choix = 0
    :return: rien, envoi après analyse le choix de l'user à choice
    '''
    while not choix:
        try:
            choix = int(input("Votre choix : "))
            if choix < 0 or choix > 4:
                choix = 0
                user_enter_choice(choix)
        except ValueError:
            print("Mauvais choix - Merci de saisir un chiffre entre 1 et 4")

    choose_extract(choix)


def choose_extract(choix):
    '''
    En fonction du choix de l'utilisateur va extraire le livre, la catégorie (après avoir demandé quelle
    catégorie est désirée) ou le site complet
    :param choix: choix de l'user en provenance de user_enter_choice
    :return: rien, le résultat sera les folders présents sur le poste de travail de l'user
    '''
    if choix == 1:
        book = []
        url = input("Indiquez l'url du livre : ")
        book.append(url)
        extract_book(book)
        print("Extraction terminée - Merci\n")
        choix = 0
        user_enter_choice(choix)
    elif choix == 2:
        try:
            ch_cat = str(input("Indiquez la categorie :" + '\n'))
            if ch_cat in cat_books:
                extract_url_category(ch_cat)
                print("Extraction terminée - Merci\n")
                choix = 0
                user_enter_choice(choix)
            else:
                choix = 0
                print("Mauvaise catégorie - Que souhaitez-vous extraire")
                user_enter_choice(choix)
        except ValueError:
            print("Mauvaise catégorie - Que souhaitez-vous extraire")
    elif choix == 3:
        pass  # Pas fonctionnel actuellement
    elif choix == 4:
        print("Merci à bientôt")
        SystemExit(0)


print(
    "Que voulez-vous extraire ?\n\n"
    "Livre : Taper 1\n"
    "Catégorie : Taper 2\n"
    "Site complet : Taper 3\n"
    "Quitter App: Taper 4\n")

""" Contrôle que l'utilisateur renseigne bien un choix en int sinon demande à celui-ci de recommencer """

choix = 0
user_enter_choice(choix)
