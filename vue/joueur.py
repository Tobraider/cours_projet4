import datetime


class VueJoueur():

    def creation_joueur():
        c = 1
        quitter = False
        # boucle pour revenir en arriere
        while not quitter and c:
            # liste des info voulu
            liste_phrase = ['nom du joueur',
                            'prenom du joueur',
                            'date de naissance : jour',
                            'date de naissance : mois',
                            'date de naissance : année'
                            ]
            liste_result = []
            i = 0
            # boucle pour revenir en arriere
            while not quitter and i < len(liste_phrase):
                valeur_ok = True
                print('CREATION DU JOUEUR')
                # donne toute les valeurs deja rentré juste la
                for j in range(i):
                    print(liste_phrase[j], ":", str(liste_result[j]))
                print("'back' pour revenir a la question precedente "
                      + "et 'exit' pour quitter ce menu")
                print(liste_phrase[i])
                result = input()
                # revient a la question d'avant
                if result == 'back':
                    if i != 0:
                        i += -1
                    valeur_ok = False
                # revient au menu principale
                elif result == 'exit':
                    quitter = True
                    valeur_ok = False
                # verifie que ce soit bien des nombre pour la date
                elif i == 2 or i == 3:
                    if not result.isdigit():
                        valeur_ok = False
                        print("ceci n'est pas un chiffre valide")
                # verifie que ce soit bien un nombre
                elif i == 4:
                    if result.isdigit():
                        # test si la date existe
                        try:
                            datetime.date(int(result),
                                          int(liste_result[3]),
                                          int(liste_result[2])
                                          )
                        except ValueError:
                            # reviens a la question du jour
                            valeur_ok = False
                            print("La date n'est pas valide")
                            i = 2
                # si valeur ok alors l'ajoute a la liste des données
                if valeur_ok:
                    if i >= len(liste_result):
                        liste_result.append(result)
                        i += 1
                    else:
                        liste_result[i] = result
                        i += 1
            j = 1
            # si tout bon donne un resumé de tout
            while not quitter and j:
                print("VOULEZ VOUS VRAIMENT ENREGISTRER LE JOUEUR SUIVANT :")
                print("nom :", liste_result[0])
                print("prenom :", liste_result[1])
                print("date de naissance :",
                      liste_result[2]
                      + "/"
                      + liste_result[3]
                      + "/"
                      + liste_result[4])
                print('1 : oui  /  2 : nom')
                result = input()
                # si oui alors mets la date en une donnée
                if result == '1':
                    print('le joueur va etre enregistré')
                    liste_result[2] = liste_result[2] + "/" + liste_result[3] + "/" + liste_result[4]
                    j = 0
                    c = 0
                # revient a la liste des question
                elif result == '2':
                    j = 0
                else:
                    print('je ne comprends pas votre reponse, '
                          + 'veulliez repondre 1 pour oui et 2 pour non')
        if quitter:
            liste_result = []
        return liste_result

    def affiche_all_joueur(liste_joueur):
        i = 0
        pas_fini = True
        print('LISTE DES JOUEUR PAR ORDRE ALPHABETIQUE')
        # affiche des joueur jusque l'utilisateur le stop
        while pas_fini and i < len(liste_joueur):
            if i < len(liste_joueur):
                j = 0
                # les affiche 50 par 50
                while j < 50 and i < len(liste_joueur):
                    print(liste_joueur[i].nom
                          + '         '
                          + liste_joueur[i].prenom
                          + '         '
                          + liste_joueur[i].naissance)
                    j += 1
                    i += 1
            # regarde si peu afficher plus de joueur
            if i < len(liste_joueur):
                print('1 : afficher les 50 suivant  /  2 : quitter')
                result = input()
            else:
                print('2 : quitter')
                result = input()
            if result == '1' and i < len(liste_joueur):
                pas_fini = True
            elif result == '2':
                pas_fini = False
            else:
                if i < len(liste_joueur):
                    print('je ne comprends pas votre reponse, '
                          + 'veulliez repondre 1 pour afficher les '
                          + '50 suivant et 2 pour quitter')
                else:
                    print('je ne comprends pas votre reponse, veulliez'
                          + ' repondre 2 pour quitter')
