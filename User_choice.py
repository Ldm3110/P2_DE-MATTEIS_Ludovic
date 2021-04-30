from Category_extractor import extract_one_book, stock_books_in_cat
from Website_extractor import extract_all_cat


def choose_extract(choix):
    if choix == 1:
        url = input("Indiquez l'url du livre : ")
        try:
            extract_one_book(url)
            print("Extraction terminée - Merci\n")
            choix = 0
            user_enter_choice(choix)
        except:
            print("Mauvaise URL - Que souhaitez-vous extraire ?")
            choix = 0
            user_enter_choice(choix)
    elif choix == 2:
        url_cat = input("Veuillez indiquer l'url de la catégorie : ")
        try:
            stock_books_in_cat(url_cat)
            print("Extraction terminée - Merci\n")
            choix = 0
            user_enter_choice(choix)
        except:
            print("Information incorrecte - Que souhaitez-vous extraire ?")
            choix = 0
            user_enter_choice(choix)
    elif choix == 3:
        extract_all_cat("https://books.toscrape.com/index.html")
        print("Extraction terminée - Merci\n")
        choix = 0
        user_enter_choice(choix)
    elif choix == 4:
        print("Merci à bientôt")
        SystemExit(0)


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
                print("Mauvais choix - Merci de saisir un chiffre entre 1 et 4")
                choix = 0
                user_enter_choice(choix)
        except ValueError:
            print("Mauvais choix - Merci de saisir un chiffre entre 1 et 4")
        choose_extract(choix)


print(
    "Que voulez-vous extraire ?\n\n"
    "Livre : Taper 1\n"
    "Catégorie : Taper 2\n"
    "Site complet : Taper 3\n"
    "Quitter App: Taper 4\n")

choix = 0
user_enter_choice(choix)
