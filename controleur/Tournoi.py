from vue.tournoi import VueTournoi
from modele.Tournoi import Tournoi


class TournoiControleur():

    def __init__(self, bdd) -> None:
        self.bdd = bdd
        self.liste_tournoi = self.bdd.liste_tournoi
        self.compteur_id = self.bdd.compteur_id_tournoi

    def affiche_all_tournoi(self):
        c = 1
        # boucle pour pouvoir revenir en arriere
        while c:
            tournoi = VueTournoi.affiche_all_tournoi(self.liste_tournoi)
            if tournoi is not None:
                cc = 1
                # boucle pour pouvoir revenir en arriere
                while cc:
                    result = VueTournoi.affiche_menu_tournoi(tournoi)
                    re_result = ''
                    if result == '1':
                        re_result = self.affiche_joueur_tournois(tournoi)
                    elif result == '2':
                        re_result = self.affiche_tour_tournois(tournoi)
                    elif result == '3':
                        re_result, tournoi = self.admin_tournoi_la(
                            self.liste_tournoi.index(tournoi)
                            )
                    elif result == 'exit':
                        cc = 0
                    elif result == 'end':
                        c = 0
                        cc = 0
                    # a prendre en compte pour revenir au menu principal
                    # de n'importe quel menu
                    if re_result == 'end':
                        c = 0
                        cc = 0
            else:
                c = 0

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

    def affiche_joueur_tournois(self, tournoi):
        liste_trier = []
        liste_joueur = []
        # recupere l'objet joueur pour ses info et l'ajoute
        # avec son score dans le tournoi
        for cle in list(tournoi.liste_joueur.keys()):
            c = 1
            i = 0
            while c and i < len(self.bdd.liste_joueur):
                if self.bdd.liste_joueur[i].id == cle:
                    liste_joueur.append((self.bdd.liste_joueur[i],
                                         tournoi.liste_joueur[cle].score
                                         ))
                i += 1
        # trie les joueur par ordre alphabetique
        for joueur, score in liste_joueur:
            i = 0
            pas_bon = True
            while pas_bon and i < len(liste_trier):
                # regarde si le nom est le meme pour passer au prenom direct
                # si encore le meme alors le mets devant l'autre
                if joueur.nom == liste_trier[i][0].nom:
                    if joueur.prenom == liste_trier[i][0].prenom:
                        pas_bon = False
                    else:
                        pas_bon = self.test_deux_mot(joueur.prenom,
                                                     liste_trier[i][0].prenom
                                                     )
                else:
                    pas_bon = self.test_deux_mot(joueur.nom,
                                                 liste_trier[i][0].nom
                                                 )
                if pas_bon:
                    i += 1
            if pas_bon:
                liste_trier.append((joueur, score))
            else:
                liste_trier.insert(i, (joueur, score))
        # afficher les joueur par ordre alphabetique
        # peut retourner end pour revenir au menu principal
        return VueTournoi.affiche_joueur_tournois(liste_trier)

    def affiche_tour_tournois(self, tournoi):
        c = 1
        # boucle pour revenir en arriere
        while c:
            # recupere un ID de tour
            id_tour = VueTournoi.affiche_tour_tournois(tournoi.liste_tour)
            if id_tour == 'exit':
                c = 0
                return ''
            elif id_tour == 'end':
                c = 0
                return 'end'
            else:
                # affiche les matchs de ce tour
                result = VueTournoi.affiche_match_tournoi(
                    tournoi.liste_tour[id_tour].liste_match,
                    self.bdd.liste_joueur,
                    id_tour
                    )
                if result == 'end':
                    c = 0
                    return 'end'

    def creation_tournoi(self):
        result = VueTournoi.creation_tournoi(self.bdd)
        if result != []:
            # creer un tournoi avec les info recuperées dans result
            self.compteur_id = str(int(self.compteur_id)+1)
            self.liste_tournoi.append(Tournoi(self.compteur_id,
                                              result[3],
                                              result[0],
                                              result[1],
                                              result[2]
                                              ))
            self.bdd.enregiste_donnees_tournois(self.liste_tournoi,
                                                self.compteur_id
                                                )
            self.liste_tournoi = self.bdd.liste_tournoi
            self.compteur_id = self.bdd.compteur_id_tournoi
            print('id du tournoi : '+self.compteur_id)
            print("LISTE DES PROCHAIN MATCH DU TOURNOI "
                  + self.liste_tournoi[len(self.liste_tournoi)-1].nom
                  )
            for match in self.liste_tournoi[
                len(self.liste_tournoi)-1
            ].liste_tour[
                'round '
                + str(self.liste_tournoi[len(self.liste_tournoi)-1].tour)
            ].liste_match:
                cc = 0
                i = 0
                # recupere les données des deux joueur
                while cc < 2 and i < len(self.bdd.liste_joueur):
                    if self.bdd.liste_joueur[i].id == match[0][0].id_joueur:
                        joueur_un = self.bdd.liste_joueur[i]
                        cc += 1
                    elif self.bdd.liste_joueur[i].id == match[1][0].id_joueur:
                        joueur_deux = self.bdd.liste_joueur[i]
                        cc += 1
                    i += 1
                print(joueur_un.nom
                      + '  '
                      + joueur_un.prenom
                      + '  /  '
                      + joueur_deux.nom
                      + '  '
                      + joueur_deux.prenom
                      )

    def admin_tournoi(self):
        c = 1
        tournoi_voulu = None
        # boucle pour pouvoir revenir en arriere
        while c:
            result = VueTournoi.admin_tournoi()
            if result == 'exit':
                c = 0
            else:
                cc = 1
                i = 0
                # parcour de tout les tournoi pour trouver un tournoi
                # avec cet ID
                while cc and i < len(self.liste_tournoi):
                    if result == self.liste_tournoi[i].id:
                        if self.liste_tournoi[i].tour > \
                          self.liste_tournoi[i].nombre_tour:
                            print("ce tournoi est deja fini")
                            cc = 0
                        else:
                            tournoi_voulu = self.liste_tournoi[i]
                            cc = 0
                    i += 1
                if cc:
                    print("il n'existe pas de tournoi avec cet ID")
                if tournoi_voulu is not None:
                    # si return end alors l'utilisateur veut retourner
                    # au menu principal
                    if self.admin_tournoi_la(i - 1)[0] == 'end':
                        c = 0
                    tournoi_voulu = None

    def admin_tournoi_la(self, index_tournoi):
        c = 1
        # boucle pour pouvoir repeter l'action
        while c:
            id_du_tournoi = self.liste_tournoi[index_tournoi].id
            result = VueTournoi.admin_tournoi_la(
                self.liste_tournoi[index_tournoi],
                self.bdd.liste_joueur
                )
            if result[0] == 'end':
                c = 0
                return 'end', self.liste_tournoi[index_tournoi]
            elif result[0] == 'exit':
                c = 0
                return '', self.liste_tournoi[index_tournoi]
            # alors id match donnée
            else:
                # result peut etre egale a 0,1,2
                # selon la ou on en est dans le tournoi et le tour
                result = self.liste_tournoi[
                        index_tournoi
                    ].findematch(int(result[0]), result[1])
                if result[0] == 0:
                    print("LISTE DES PROCHAIN MATCH :")
                    # sort tout les prochain match
                    for match in result[1]:
                        cc = 0
                        i = 0
                        # va chercher les info dans l'objet joueur
                        while cc < 2 and i < len(self.bdd.liste_joueur):
                            if self.bdd.liste_joueur[i].id == \
                              match[0][0].id_joueur:
                                joueur_un = self.bdd.liste_joueur[i]
                                cc += 1
                            elif self.bdd.liste_joueur[
                                i
                            ].id == match[1][0].id_joueur:
                                joueur_deux = self.bdd.liste_joueur[i]
                                cc += 1
                            i += 1
                        print(joueur_un.nom
                              + '  '
                              + joueur_un.prenom
                              + '  /  ' + joueur_deux.nom
                              + '  ' + joueur_deux.prenom
                              )
                # enregistre les changement et recharge le json
                self.bdd.enregiste_donnees_tournois(self.liste_tournoi,
                                                    self.compteur_id
                                                    )
                self.liste_tournoi = self.bdd.liste_tournoi
                self.compteur_id = self.bdd.compteur_id_tournoi
                cc = 1
                i = 0
                # recherche le tournoi avec l'id donné pour
                # etre sur que tout est OK
                while cc and i < len(self.liste_tournoi):
                    if id_du_tournoi == self.liste_tournoi[i].id:
                        tournoi = self.liste_tournoi[i]
                        cc = 0
                    i += 1
                # si tournoi fini
                if result[0] == 1:
                    c = 0
                    return '', tournoi
