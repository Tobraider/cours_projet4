class Joueur():

    def __init__(self, id, nom,
                 prenom, naissance, liste_id_tournoi=[]):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.liste_id_tournoi = liste_id_tournoi

    def ressort_dict(self):
        return self.__dict__
