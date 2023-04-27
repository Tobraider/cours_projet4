from vue.menu import Menu


class console():

    def __init__(self, joueur_controleur, tournoi_controleur):
        self.joueur_controleur = joueur_controleur
        self.tournoi_controleur = tournoi_controleur
        self.c = 1
        # execute la premiere fonction du programme
        self.bienvenu()

    def bienvenu(self):
        print("INITIALISATION FINI, BIENVENU")
        self.start()

    def start(self):
        # liste de chaque action selon le choix pris
        liste_action = [self.joueur_controleur.affiche_all_joueur,
                        self.joueur_controleur.creation_joueur,
                        self.tournoi_controleur.affiche_all_tournoi,
                        self.tournoi_controleur.creation_tournoi,
                        self.tournoi_controleur.admin_tournoi,
                        self.end
                        ]
        # boucle jusqu'a demande de sortir
        while self.c:
            liste_action[int(Menu.affiche())]()

    def end(self):
        self.c = 0
