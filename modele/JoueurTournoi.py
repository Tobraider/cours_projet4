class JoueurTournoi():

    def __init__(self, id, liste_joueur_vu, score=0) -> None:
        self.id_joueur = id
        self.score = score
        self.liste_joueur_vu = list(liste_joueur_vu)

    def dict(self):
        data = {'score': self.score, 'liste_joueur_vu': self.liste_joueur_vu}
        return data
