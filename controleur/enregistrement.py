import json

from modele.joueur import Joueur
from modele.tournoi import Tournoi


class Enregistrement():

    def __init__(self, fichier):
        self.liste_joueur = []
        self.liste_tournoi = []
        self.compteur_id_joueur = 0
        self.compteur_id_tournoi = 0
        self.data_joueurs = {}
        self.data_tournois = {}
        # charge le fichier si celui ci existe
        if fichier != "":
            self.fichier = fichier
            self.__charge_donnees()
        else:
            self.fichier = "save/save.json"

    def enregiste_donnees_tournois(self, liste_tournoi, compteur_id_tournoi):
        data = {}
        # les données joueur n'ont pas changées donc pas besoin de les
        # recalculer
        data['joueurs'] = self.data_joueurs
        data_tournoi = {}
        # recupere toute les données de tout les tournois
        for tournoi in liste_tournoi:
            data_tournoi[tournoi.id] = tournoi.ressort_dict()
        data['tournois'] = data_tournoi
        # enregistre les compteur pour les prochain ID
        data['compteur_id_joueur'] = self.compteur_id_joueur
        data['compteur_id_tournoi'] = compteur_id_tournoi
        # enregistre les données dans le json
        with open(self.fichier, 'w') as f:
            json.dump(data, f)
        # recharge les données pour etre sur que ca a bien été pris en compte
        self.__charge_donnees()

    def enregiste_donnees_joueurs(self, liste_joueur, compteur_id_joueur):
        data = {}
        data_joueur = {}
        # recupere toute les données joueur de tout les joueur
        for joueur in liste_joueur:
            data_joueur[joueur.id] = joueur.ressort_dict()
        data['joueurs'] = data_joueur
        # les données tournois n'ont pas changées donc pas besoin de les
        # recalculer
        data['tournois'] = self.data_tournois
        # enregistre les compteur pour les prochain ID
        data['compteur_id_joueur'] = compteur_id_joueur
        data['compteur_id_tournoi'] = self.compteur_id_tournoi
        # enregistre les données dans le json
        with open(self.fichier, 'w') as f:
            json.dump(data, f)
        # recharge les données pour etre sur que ca a bien été pris en compte
        self.__charge_donnees()

    def __charge_donnees(self):
        # recupere les données du fichier
        with open(self.fichier, 'r') as f:
            data = f.read()
        # transforme la chaine de charactere en json facilement exploitable
        data = json.loads(data)
        # regarde si les données joueur ont changées si oui refait
        # tout les objets joueur
        if self.data_joueurs != data['joueurs']:
            self.compteur_id_joueur = data['compteur_id_joueur']
            self.data_joueurs = data['joueurs']
            self.liste_joueur = []
            for id, joueur in data['joueurs'].items():
                self.liste_joueur.append(
                    Joueur(
                        id,
                        joueur['nom'],
                        joueur['prenom'],
                        joueur['naissance'],
                        joueur['liste_id_tournoi']
                        )
                    )
        # regarde si les données tournois ont changées si oui refait
        # tout les objets tournoi
        if self.data_tournois != data['tournois']:
            self.data_tournois = data['tournois']
            self.compteur_id_tournoi = data['compteur_id_tournoi']
            self.liste_tournoi = []
            for id, tournoi in data['tournois'].items():
                self.liste_tournoi.append(
                    Tournoi(
                        id,
                        tournoi['liste_joueur'],
                        tournoi['nom'],
                        tournoi['lieu'],
                        int(tournoi['nombre_tour']),
                        float(tournoi['date_start']),
                        float(tournoi['date_end']),
                        int(tournoi['tour']),
                        tournoi['liste_tour']
                        )
                    )
        else:
            # arrive si rien n'a changé, erreur du coup car appel au debut
            # ou si quelque chose a changé dans le programme
            print("erreur, rien n'as changer entre les deux")
