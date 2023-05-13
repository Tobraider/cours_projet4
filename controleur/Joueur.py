from vue.joueur import VueJoueur
from modele.joueur import Joueur


class JoueurControleur():

    def __init__(self, bdd) -> None:
        self.bdd = bdd
        self.liste_joueur = self.bdd.liste_joueur
        self.compteur_id = self.bdd.compteur_id_joueur

    def test_deux_mot(self, mot_un, mot_deux):
        # retourne vrai si le mot un est plus tot dans l'ordre
        # alphabetique que mot deux
        c = 1
        i = 0
        result = False
        while c and i < len(mot_un):
            if i == len(mot_deux):
                result = True
                c = 0
            elif mot_un[i].lower() > mot_deux[i].lower():
                # attention fait en sorte que ' ' soit la meme chose que '-'
                if mot_un[i] == ' ' or mot_un[i] == '-':
                    if mot_deux[i] != ' ':
                        c = 0
                else:
                    c = 0
                    result = True
            else:
                # attention fait en sorte que ' ' soit la meme chose que '-'
                if mot_deux[i] == ' ' or mot_deux[i] == '-':
                    if mot_un[i] != ' ':
                        c = 0
                        result = True
            i += 1
        return result

    def affiche_all_joueur(self):
        liste_trier = []
        # passe par chaque joueur pour le trier
        for joueur in self.liste_joueur:
            i = 0
            pas_bon = True
            while pas_bon and i < len(liste_trier):
                # regarde si le nom est le meme pour passer au prenom direct
                # si encore le meme alors le mets devant l'autre
                if joueur.nom == liste_trier[i].nom:
                    if joueur.prenom == liste_trier[i].prenom:
                        pas_bon = False
                    else:
                        pas_bon = self.test_deux_mot(joueur.prenom,
                                                     liste_trier[i].prenom
                                                     )
                else:
                    pas_bon = self.test_deux_mot(joueur.nom,
                                                 liste_trier[i].nom
                                                 )
                if pas_bon:
                    i += 1
            if pas_bon:
                liste_trier.append(joueur)
            else:
                liste_trier.insert(i, joueur)
        # affiche la liste triée
        VueJoueur.affiche_all_joueur(liste_trier)

    def creation_joueur(self):
        result = VueJoueur.creation_joueur()
        if result != []:
            # creer le joueur avec les données dans la liste
            self.compteur_id = str(int(self.compteur_id)+1)
            self.liste_joueur.append(Joueur(self.compteur_id,
                                            result[0],
                                            result[1],
                                            result[2]
                                            ))
            # enregistre et recharge le fichier
            self.bdd.enregiste_donnees_joueurs(self.liste_joueur,
                                               self.compteur_id
                                               )
            self.liste_joueur = self.bdd.liste_joueur
            self.compteur_id = self.bdd.compteur_id_joueur
