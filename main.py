from extractBook import extract_book
from extractCat import extract_category
from extractAll import extract_all

"""
======================================================================
Interface utilisateur qui permettra de savoir ce qui doit être extrait
======================================================================
"""


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
        extract_category(choice)
        print("Extraction terminée - Merci\n")
    elif choix == 3:
        extract_all()
        print("Extraction terminée - Merci\n")
    elif choix == 4:
        break

    """ La première extraction est terminée - l'user peut choisir d'en faire une autre sinon il peut quitter le programme """
    choix = int(input("Votre choix : "))
