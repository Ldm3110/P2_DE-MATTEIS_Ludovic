# P2_DE-MATTEIS_Ludovic
Projet 2 de la formation Développeur d'application Python - OPENCLASSROOMS

Scraping du site https://books.toscrape.com/index.html


## 1. Initialisation du projet et installation des prérequis 

A l'aide du terminal (Mac/Linux) ou de l'invite de commande (Windows), rendez-vous à l'endroit prévu pour réceptionner votre projet.

### Cloner le projet
tapez :

    $ git clone https://github.com/Ldm3110/P2_DE-MATTEIS_Ludovic.git

### Activer l'environnement virtuel 

sous MAC/Linux :

    $ cd P2_DE-MATTEIS_Ludovic 
    $ python3 -m venv env 
    $ source env/bin/activate
    
sous Windows :

    $ cd P2_DE-MATTEIS_Ludovic 
    $ py -m venv env 
    $ \env\Scripts\activate
    
    
### Installer les 'requirements'
    
    $ pip install -r requirements.txt
    
   
## 2. Fonctionnement du projet

### Démarrage

sous MAC/Linux :

    $ python3 User_choice.py
    
sous Windows :

    $ py User_choice.py
    
    
Vous constatez alors l'affichage de :

    Que voulez-vous extraire ?

    Livre : Taper 1
    Catégorie : Taper 2
    Site complet : Taper 3
    Quitter App: Taper 4

    Votre choix : 

#### Choix 1
Vous souhaitez donc extraire un livre, l'utilitaire vous demande alors d'indiquer l'url du livre :
    
    Indiquez l'url du livre : 
    
Faites un copiez-coller de l'url du livre concerné à la suite de ce texte, comme par exemple

    Indiquez l'url du livre : https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html
    
Appuyer sur Entrée et laisser faire le programme
    
#### Choix 2
Vous désirez extraire une catégorie, comme pour le choix 1 l'utilitaire vous demandera de rentrer l'url de la catégorie concernée, par exemple

    Veuillez indiquer l'url de la catégorie : https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html

Appuyer sur Entrée et laisser faire le programme

#### Choix 3
Pour l'extraction du site entier vous n'avez rien à faire. En tapant simplement 3 lors du choix le programme executera automatiquement l'extraction complète de celui-ci.

#### Choix 4
Ce choix sert à mettre fin au programme. Tapez 4 si vous n'avez plus besoin de l'utiliser

### Votre extraction est terminée

Le programme vous proposera alors de taper à nouveau un choix, libre à vous de choisir 1, 2, 3 ou 4. Le fonctionnement restera le même que dans la partie "Démarrage"

#### Situer votre/vos extraction(s)
Lors du téléchargement des différents éléments, un fichier 'Catégorie' apparaitra dans le dossier de votre programme. En cliquant dessus vous verrez qu'un ou plusieurs dossiers seront affichés avec comme intitulé la catégorie des livres extraits (Travel, Sequential Art ...).

A l'intérieur de ces dossiers vous trouverez un dossier 'Book_cover' dans lequelle figurera les couvertures de livres au format .jpg et un fichier .csv qui contiendra les extractions de tous les éléments du ou des livres de la catégorie concernée.
