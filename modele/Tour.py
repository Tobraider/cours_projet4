import time


class Tour():

    def __init__(self, liste_paire, date_start=time.time(),
                 date_end=0, nombre_match_fini=0):
        self.date_start = date_start
        self.date_end = date_end
        self.nombre_match = len(liste_paire)
        self.liste_match = liste_paire
        self.nombre_match_fini = nombre_match_fini

    def match_fini(self, match, vainqueur):
        # met a jour les score dans les match
        if vainqueur == 0:
            self.liste_match[match][0][1] = 0.5
            self.liste_match[match][1][1] = 0.5
        elif vainqueur == 1:
            self.liste_match[match][0][1] = 1
            self.liste_match[match][1][1] = 0
        elif vainqueur == 2:
            self.liste_match[match][0][1] = 0
            self.liste_match[match][1][1] = 1
        # met a jour les score des joueur du tournoi
        self.liste_match[match][0][0].score += self.liste_match[match][0][1]
        self.liste_match[match][1][0].score += self.liste_match[match][1][1]
        self.nombre_match_fini += 1

    def ressort_dict(self):
        data = {}
        data['date_start'] = self.date_start
        data['date_end'] = self.date_end
        data['nombre_match'] = self.nombre_match
        data['nombre_match_fini'] = self.nombre_match_fini
        data['liste_match'] = self.__ressort_match_list()
        return data

    def __ressort_match_list(self):
        data = []
        # passe les match un a un pour en extraire id du joueur et le
        # score du match
        for match in self.liste_match:
            data.append(([match[0][0].id_joueur, match[0][1]],
                         [match[1][0].id_joueur, match[1][1]]))
        return data
