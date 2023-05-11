import time
import random

from modele.Tour import Tour
from modele.JoueurTournoi import JoueurTournoi


class Tournoi():

    def __init__(self, id, liste_joueur, nom,
                 lieu, nombre_tour=4, date_start=time.time(),
                 date_end=0, tour=0, liste_tour=[],
                 liste_id_joueur_tout_jouer=[]):
        self.id = id
        self.nom = nom
        self.lieu = lieu
        self.nombre_tour = nombre_tour
        self.date_start = date_start
        self.date_end = date_end
        self.tour = tour
        self.liste_joueur = {}
        self.liste_id = []
        # si tour != 0 alors pas creation mais chargement
        if self.tour != 0:
            for id, joueur in liste_joueur.items():
                self.liste_joueur[id] = JoueurTournoi(
                    id,
                    joueur['liste_joueur_vu'],
                    float(joueur['score'])
                    )
                self.liste_id.append(id)
        else:
            for joueur in liste_joueur:
                self.liste_joueur[joueur.id] = JoueurTournoi(joueur.id, [])
                self.liste_id.append(joueur.id)
                joueur.liste_id_tournoi.append(self.id)
        self.liste_tour = {}
        # si tour != 0 alors pas creation mais chargement
        if self.tour != 0:
            for id, tour in liste_tour.items():
                liste_match = []
                for match in tour['liste_match']:
                    # va chercher dans la liste_joueur car enregistré que l'ID
                    liste_match.append(
                        ([self.liste_joueur[match[0][0]], match[0][1]],
                         [self.liste_joueur[match[1][0]], match[1][1]]
                         )
                        )
                self.liste_tour[id] = Tour(liste_match,
                                           float(tour['date_start']),
                                           float(tour['date_end']),
                                           int(tour['nombre_match_fini'])
                                           )
        # liste importante, en cas de nombre impaire de joueur,
        # defini qui ne va pas jouer
        if liste_id_joueur_tout_jouer == []:
            self.liste_id_joueur_tout_jouer = list(self.liste_id)
        else:
            self.liste_id_joueur_tout_jouer = liste_id_joueur_tout_jouer
        if self.tour == 0:
            self.__premier_round()

    def __premier_round(self):
        self.tour += 1
        liste_paire = []
        id_joueur_joue_pas = None
        # verifie si nombre de joueur est impaire
        if len(self.liste_id) % 2:
            # defini de maniere aleatiore qui ne joue pas
            id_joueur_joue_pas = self.liste_id_joueur_tout_jouer[
                random.randint(0, len(self.liste_id_joueur_tout_jouer)-1)
                ]
            self.liste_id.remove(id_joueur_joue_pas)
        nombre_paire = len(self.liste_id)/2
        liste_id_joueur_joue = list(self.liste_id)
        if id_joueur_joue_pas is not None:
            # rajoute celui qui a ete supprimer car ne joue pas le round
            self.liste_id.append(id_joueur_joue_pas)
        # creer toute les paires
        for i in range(int(nombre_paire)):
            joueur_un = liste_id_joueur_joue.pop(0)
            # prends un deuxieme joueur aleatoire
            joueur_deux = liste_id_joueur_joue.pop(
                random.randint(0, len(liste_id_joueur_joue)-1)
                )
            # distribu le noir et le blanc de maniere aleatoire
            noir_blanc = random.randint(0, 1)
            if noir_blanc:
                liste_paire.append(([self.liste_joueur[joueur_un], -1],
                                    [self.liste_joueur[joueur_deux], -1]))
                self.liste_joueur[
                    joueur_deux
                    ].liste_joueur_vu.append(joueur_un)
                self.liste_joueur[
                    joueur_un
                    ].liste_joueur_vu.append(joueur_deux)
            else:
                liste_paire.append(([self.liste_joueur[joueur_deux], -1],
                                    [self.liste_joueur[joueur_un], -1]))
                self.liste_joueur[
                    joueur_deux
                    ].liste_joueur_vu.append(joueur_un)
                self.liste_joueur[
                    joueur_un
                    ].liste_joueur_vu.append(joueur_deux)
        self.liste_tour["round " + str(self.tour)] = Tour(liste_paire)

    def __nouveau_tour(self):
        self.tour += 1
        print('DEBUT DU ROUND ' + str(self.tour))
        liste_paire = self.__creation_de_paire()
        self.liste_tour["round " + str(self.tour)] = Tour(liste_paire)

    def __creation_de_paire(self):
        liste_paire = []
        joueur_joue_pas = None
        # verifie si nombre de joueur est impaire
        if len(self.liste_id) % 2:
            # defini de maniere aleatiore qui ne joue pas
            joueur_joue_pas = self.liste_id_joueur_tout_jouer[
                random.randint(0, len(self.liste_id_joueur_tout_jouer)-1)
                ]
            self.liste_id.remove(joueur_joue_pas)
        nombre_paire = len(self.liste_id)/2
        liste_joueur_trier = self.__trie(list(self.liste_id))
        if joueur_joue_pas is not None:
            # rajoute celui qui a ete supprimer car ne joue pas le round
            self.liste_id.append(joueur_joue_pas)
        joueur_sans_paire = None
        i = 0
        # tant que toute les paires ne sont pas faites
        while i < nombre_paire:
            # prends le premier joueur de la liste
            premier_joueur = liste_joueur_trier[0].pop()
            # si la liste est vide cela signifie qu'il n'y a plus de joueur
            # avec le meme score que lui, on passe a la suivante
            if liste_joueur_trier[0] == []:
                liste_joueur_trier.pop(0)
            pas_trouver = True
            # commence a -1 car on ajoute un au debut de la boucle
            j = -1
            # len(liste_joueur_trier)-1 car j commence a -1
            while pas_trouver and j < len(liste_joueur_trier) - 1:
                j += 1
                k = 0
                # cherche un joueur avec qui faire une paire avec qui
                # il a pas encore joué
                while pas_trouver and k < len(liste_joueur_trier[j]):
                    if not liste_joueur_trier[j][k] \
                      in self.liste_joueur[premier_joueur].liste_joueur_vu:
                        pas_trouver = False
                    else:
                        k += 1
            # si pas_trouver est egale a True alors il n'a pas de joueur
            # restant avec qui il peut aller donc on fait une paire avec
            # les cas comme lui
            if pas_trouver:
                # si deja un mec comme lui fait la paire
                if joueur_sans_paire:
                    liste_paire.append((
                        [self.liste_joueur[premier_joueur], -1],
                        [joueur_sans_paire, -1]
                        ))
                    i += 1
                # sinon dit qu'il existe un mec comme lui
                else:
                    joueur_sans_paire = self.liste_joueur[premier_joueur]
            # sinon creer une paire avec le joueur trouvé
            else:
                deuxieme_joueur = liste_joueur_trier[j].pop(k)
                # si la liste est vide cela signifie qu'il n'y a plus de
                # joueur avec le meme score que lui
                if liste_joueur_trier[j] == []:
                    liste_joueur_trier.pop(j)
                # regarde s'il a deja vu tout les joueur sauf lui et celui
                # qu'il va rencontrer d'ou le -2
                if len(self.liste_joueur[premier_joueur].liste_joueur_vu) \
                   == len(self.liste_joueur) - 2:
                    self.liste_joueur[premier_joueur].liste_joueur_vu = []
                else:
                    self.liste_joueur[
                        premier_joueur
                        ].liste_joueur_vu.append(deuxieme_joueur)
                # regarde s'il a deja vu tout les joueur sauf lui et celui
                # qu'il va rencontrer d'ou le -2
                if len(self.liste_joueur[deuxieme_joueur].liste_joueur_vu) \
                   == len(self.liste_joueur) - 2:
                    self.liste_joueur[deuxieme_joueur].liste_joueur_vu = []
                else:
                    self.liste_joueur[
                        deuxieme_joueur
                        ].liste_joueur_vu.append(premier_joueur)
                # distribu le noir et le blanc de maniere aleatoire
                noir_blanc = random.randint(0, 1)
                if noir_blanc:
                    liste_paire.append((
                        [self.liste_joueur[premier_joueur], -1],
                        [self.liste_joueur[deuxieme_joueur], -1]
                        ))
                else:
                    liste_paire.append((
                        [self.liste_joueur[deuxieme_joueur], -1],
                        [self.liste_joueur[premier_joueur], -1]
                        ))
                i += 1
        return liste_paire

    def __trie(self, liste_joueur):
        # prend le premier joueur dans la liste de liste
        liste_joueur_trier = [[liste_joueur.pop()]]
        # passe tout les joueur un a un
        for joueur in liste_joueur:
            i = 0
            mis = 0
            while not mis and i < len(liste_joueur_trier):
                if self.liste_joueur[joueur].score > self.liste_joueur[
                    liste_joueur_trier[i][0]
                ].score:
                    mis = 1
                elif self.liste_joueur[joueur].score == self.liste_joueur[
                    liste_joueur_trier[i][0]
                ].score:
                    mis = 2
                else:
                    i += 1
            # ajout une liste avec le joueur dedans
            if mis == 0:
                liste_joueur_trier.append([joueur])
            # si score > alors creer une nouvelle liste mis avant l'autre
            elif mis == 1:
                liste_joueur_trier.insert(i, [joueur])
            # ajout du joueur dans la liste de joueur
            # aillant le meme score que lui
            elif mis == 2:
                liste_joueur_trier[i].append(joueur)
        return liste_joueur_trier

    def findematch(self, match, vainqueur):
        self.liste_tour['round '+str(self.tour)].match_fini(match, vainqueur)
        # si le nombre de match fini est egale au nombre
        # de match fait alors fin du round
        if self.liste_tour['round '+str(self.tour)].nombre_match == \
           self.liste_tour['round '+str(self.tour)].nombre_match_fini:
            self.liste_tour['round '+str(self.tour)].date_end = time.time()
            print('LE ROUND '+str(self.tour)+' EST FINI')
            # si different alors il reste des round a faire
            if self.tour != self.nombre_tour:
                self.__nouveau_tour()
                return [0,
                        self.liste_tour['round '+str(self.tour)].liste_match
                        ]
            # sinon fin du tournoi
            else:
                # ajout un pour le savoir
                self.tour += 1
                print('LE TOURNOI EST FINI !')
                # enregistre la date de la fin du tournoi
                self.date_end = time.time()
                return [1]
        return [2]

    def ressort_dict(self):
        data = {}
        data['nom'] = self.nom
        data['lieu'] = self.lieu
        data['nombre_tour'] = self.nombre_tour
        data['date_start'] = self.date_start
        data['date_end'] = self.date_end
        data['tour'] = self.tour
        data['liste_id_joueur_tout_jouer'] = self.liste_id_joueur_tout_jouer
        data['liste_joueur'] = self.__ressort_dict_list_joueur()
        data['liste_tour'] = self.__ressort_dict_list_tour()
        return data

    def __ressort_dict_list_joueur(self):
        dict_joueur = {}
        # ressort en dict toute la liste des joueur du tournoi
        for id, joueur in self.liste_joueur.items():
            dict_joueur[id] = joueur.dict()
        return dict_joueur

    def __ressort_dict_list_tour(self):
        dict_tour = {}
        # ressort en dict tout les tour
        for id, tour in self.liste_tour.items():
            dict_tour[id] = tour.ressort_dict()
        return dict_tour
