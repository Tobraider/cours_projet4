import os

from controleur.enregistrement import Enregistrement
from controleur.Joueur import JoueurControleur
from controleur.Tournoi import TournoiControleur
from controleur.console import console

# verifi si le dossier existe
if not os.path.exists("save/"):
    # creer un fichier
    os.makedirs("path")
    fichier = ''
# verifi si le dossier existe
elif os.path.exists("save/save.json"):
    fichier = 'save/save.json'
else:
    fichier = ''

# charge le fichier de sauvegarde et initialise le controleur de la
# gestion de sauvegarde
bdd = Enregistrement(fichier)

# initialise le controleur joueur
joueur_controleur = JoueurControleur(bdd)

# intialise le controleur tournoi
tournoi_controleur = TournoiControleur(bdd)

# intialise le controleur console, ce controleur permet de faire tourner
# l'application
console_controleur = console(joueur_controleur, tournoi_controleur)
