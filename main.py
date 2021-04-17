from extractBook import extract_book
from extractCat import extract_category
from extractAll import extract_all

"""
======================================================================
Interface utilisateur qui permettra de savoir ce qui doit être extrait
======================================================================
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

""" 

Permet de trouver la portion d'url de la catégorie demandée par l'utilisateur 
à l'aide du dictionnaire list_choice

"""


def find_cat(v):
    for k, val in list_choice.items():
        if v == k:
            return val


print(
    "Que voulez-vous extraire ?\n\nLivre : Taper 1\nCatégorie : Taper 2\nSite complet : Taper 3\nQuitter App: Taper 4\n")

choix = 0

""" Contrôle que l'utilisateur renseigne bien un choix en int sinon demande à celui-ci de recommencer """
while not choix:
    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("Mauvais choix - Merci de saisir un chiffre entre 1 et 4")
        pass

""" Le choix est entre 1 et 4 - en fonction va déterminer la suite du programme """
while choix != 4:
    if choix == 1:
        url = input("Indiquez l'url du livre : ")
        extract_book(url)
        print("Extraction terminée - Merci\n")
    elif choix == 2:
        choice = input("Indiquez la categorie :" + '\n')
        cat_url = "http://books.toscrape.com/catalogue/category/books/" + find_cat(str(choice)) + "/index.html"
        extract_category(cat_url)
        print("Extraction terminée - Merci\n")
    elif choix == 3:
        extract_all()
        print("Extraction terminée - Merci\n")
    elif choix == 4:
        break

    choix = int(input("Votre choix : "))
