import joueur
import time
import random
class tournoi():
    
    def __init__(self, list_joueur, nom, lieu, nbTour = 4, dateStart = time.localtime, dateEnd = None, tour = 0, list_tour = []) -> None:
        self.nom = nom
        self.lieu = lieu
        self.nb_tour = nbTour
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.tour = tour
        self.list_tour = list_tour
        self.list_joueur = []
        if type(list_joueur[0]) != joueurTournoi:
            for joueur in list_joueur:  #a verifier s'il ne le sont pas deja en vrai
                self.list_joueur.append(joueurTournoi(joueur))
        else:
            self.list_joueur = list_joueur
        self.list_joueurPasJoue = list(list_joueur)

    def debuttour(self):
        self.tour += 1
        liste_joueurtrier = []
        for joueur in self.list_joueur:
            pasmi = True
            pos = 0
            while pasmi and pos<len(liste_joueurtrier):
                if liste_joueurtrier[pos].scrore < joueur.score:
                    pasmi = False
                pos += 1
            liste_joueurtrier.insert(pos, joueur)
        newTour = tour("Round "+str(tour))
        if len(liste_joueurtrier)%2 == 1:
            if len(self.list_joueurPasJoue) == 1:
                liste_joueurtrier.remove(self.list_joueurPasJoue[0])
                self.list_joueurPasJoue = list(self.list_joueur)
            else:
                liste_joueurtrier.remove(self.list_joueurPasJoue[random.randint(0, len(self.list_joueurPasJoue))])
        while len(liste_joueurtrier) > 0:
            joueurun = liste_joueurtrier.pop()
            pasTrouve = True
            pos = 1
            while pasTrouve and pos<=len(liste_joueurtrier):
                if not liste_joueurtrier[pos*-1] in joueurun.list_joueurDejaVu:
                    pasTrouve = False
                pos += 1
            if pasTrouve:
                joueurdeux = liste_joueurtrier.pop()
                joueurun.list_joueurDejaVu = []
                joueurdeux.list_joueurDejaVu = []
            else:
                joueurdeux = liste_joueurtrier.pop(len(liste_joueurtrier)-pos)
                joueurun.list_joueurDejaVu.append(joueurdeux)
                joueurdeux.list_joueurDejaVu.append(joueurun)
            newTour.ajoutMatch(match(joueurun, joueurdeux))
        self.list_tour.append(newTour)


    def findematch(self, match, vainqueur): #doit etre appeler par la partie vue
        self.list_tour[-1].matchFini(match, vainqueur) 
        if self.list_tour[-1].nbMatch == self.list_tour[-1].nbMatchFini:
            if self.tour != self.nb_tour:
                self.debuttour()
        #peut eter voir pour trier toute la liste pour sortir le vainqueur oklm




class tour():

    def __init__(self, name) -> None:
        self.name = name
        self.dateStart = time.localtime
        self.dateEnd = None
        self.nbMatch = 0
        self.nbMatchFini = 0
        self.list_match = []
    
    def ajoutMatch(self, match):
        self.list_match.append(match)
        self.nbMatch += 1

    def matchFini(self, match, vainqueur): #vainqueur = 0 si egalité 1 si joueur 1 gagne et 2 si joueur 2 gagne
        if vainqueur == 0:
            self.list_match[match][1] = 0.5
            self.list_match[match][3] = 0.5
        if vainqueur == 0:
            self.list_match[match][1] = 1
            self.list_match[match][3] = 0
        if vainqueur == 0:
            self.list_match[match][1] = 0
            self.list_match[match][3] = 1    
        self.list_match[match][0].score += self.list_match[match][1]
        self.list_match[match][2].score += self.list_match[match][3]
        self.nbMatchFini += 1
    

class joueurTournoi(joueur):

    def __init__(self, joueur) -> None:
        super().__init__(joueur.nom, joueur.prenom, joueur.naissance)
        self.score = 0
        self.list_joueurDejaVu = []

def match(joueurun, joueurdeux) -> tuple:
    return joueurun.joueur, 0, joueurdeux.joueur, 0 