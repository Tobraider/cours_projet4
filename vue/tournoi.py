import time


class VueTournoi ():

    def affiche_all_tournoi(liste_tournois):
        i = 0
        pas_fini = True
        print('LISTE DES TOURNOIS')
        lebontournois = None
        # boucle pour les faute dans input
        while pas_fini:
            if i < len(liste_tournois):
                j = 0
                # sort les tournoi 50 par 50
                while j < 50 and i < len(liste_tournois):
                    date_debut = time.localtime(liste_tournois[i].date_start)
                    # si date de fin alors tournoi fini
                    if liste_tournois[i].date_end != 0:
                        date_fin = time.localtime(liste_tournois[i].date_end)
                        print(liste_tournois[i].id + '         '
                              + liste_tournois[i].nom + '         '
                              + liste_tournois[i].lieu + '         DEBUT : '
                              + str(date_debut.tm_hour) + ":"
                              + str(date_debut.tm_min) + "  "
                              + str(date_debut.tm_mday) + "/"
                              + str(date_debut.tm_mon) + "/"
                              + str(date_debut.tm_year) + '         FIN : '
                              + str(date_fin.tm_hour) + ":"
                              + str(date_fin.tm_min) + "  "
                              + str(date_fin.tm_mday) + "/"
                              + str(date_fin.tm_mon) + "/"
                              + str(date_fin.tm_year) + '     FINI')
                    # si tournoi sans date de fin
                    else:
                        print(liste_tournois[i].id + '         '
                              + liste_tournois[i].nom + '         '
                              + liste_tournois[i].lieu + '         DEBUT : '
                              + str(date_debut.tm_hour) + ":"
                              + str(date_debut.tm_min) + "  "
                              + str(date_debut.tm_mday) + "/"
                              + str(date_debut.tm_mon) + "/"
                              + str(date_debut.tm_year) + '         '
                              + str(liste_tournois[i].tour) + '/'
                              + str(liste_tournois[i].nombre_tour))
                    j += 1
                    i += 1
            # change le menu selon s'il reste ou non des tournoi
            if i < len(liste_tournois):
                print('rentrer le numero du tournoi pour le selectionner  /  '
                      + '" " : afficher les 50 suivant  /  '
                      + 'exit : revenir en arriere')
                result = input()
            else:
                print('rentrer le numero du tournoi pour le selectionner  /  '
                      + 'exit : revenir en arriere')
                result = input()
            if result == ' ' and i < len(liste_tournois):
                pas_fini = True
            elif result == 'exit':
                pas_fini = False
            # sinon alors id tournoi donc verifi si nombre
            elif result.isdigit():
                # recherche le tournoi dans la liste
                for tournoi in liste_tournois:
                    if tournoi.id == result:
                        lebontournois = tournoi
                if lebontournois is not None:
                    pas_fini = False
                else:
                    print("ce tournoi n'existe pas")
            else:
                if i < len(liste_tournois):
                    print("je ne comprends pas votre reponse, veulliez"
                          + " repondre un nombre, ' ' pour afficher les"
                          + " 50 suivant ou exit pour revenir en arriere")
                else:
                    print("je ne comprends pas votre reponse, veulliez "
                          + "repondre un nombre ou exit pour revenir en "
                          + "arriere")
        return lebontournois

    def affiche_joueur_tournois(liste_joueur):
        i = 0
        pas_fini = True
        print('LISTE DES JOUEUR PAR ORDRE ALPHABETIQUE')
        # passe tout les joueur
        while pas_fini and i < len(liste_joueur):
            if i < len(liste_joueur):
                j = 0
                # les affiche 50 par 50, str(liste_joueur[i][1]) est le score
                while j < 50 and i < len(liste_joueur):
                    print(liste_joueur[i][0].nom + '         '
                          + liste_joueur[i][0].prenom + '         '
                          + str(liste_joueur[i][1]))
                    j += 1
                    i += 1
            # change le menu selon s'il reste ou non des joueur
            if i < len(liste_joueur):
                print('1 : afficher les 50 suivant  /  2 : revenir en arriere'
                      + '  /  3 : revenir au menu principal')
                result = input()
            else:
                print('2 : revenir en arriere  /  3 : revenir au menu'
                      + ' principal')
                result = input()
            if result == '1' and i < len(liste_joueur):
                pas_fini = True
            elif result == '2':
                pas_fini = False
                return ''
            elif result == '3':
                pas_fini = False
                return 'end'
            else:
                if i < len(liste_joueur):
                    print('je ne comprends pas votre reponse, veulliez '
                          + 'repondre 1 pour afficher les 50 suivant, 2 '
                          + 'pour revenir en arriere ou 3 pour revenir au'
                          + ' menu principal')
                else:
                    print('je ne comprends pas votre reponse, veulliez '
                          + 'repondre 2 pour revenir en arriere ou 3 pour'
                          + ' revenir au menu principal')

    def affiche_tour_tournois(liste_tour):
        i = 1
        pas_fini = True
        print('LISTE DES TOUR')
        lebontour = None
        # boucle pour les faute dans input
        while pas_fini:
            if i <= len(liste_tour):
                j = 0
                # affiche les tour 50 par 50
                while j < 50 and i <= len(liste_tour):
                    date_debut = time.localtime(
                        liste_tour['round '+str(i)].date_start
                        )
                    # si match fini affiche date de fin
                    if liste_tour['round '+str(i)].date_end != 0:
                        date_fin = time.localtime(liste_tour[
                            'round '+str(i)
                            ].date_end)
                        print(
                            'round '
                            + str(i)
                            + '         MATCH FAIT : '
                            + str(liste_tour[
                                'round ' + str(i)
                            ].nombre_match_fini)
                            + '/'
                            + str(liste_tour['round '+str(i)].nombre_match)
                            + "      DEBUT : "
                            + str(date_debut.tm_hour)
                            + ":"
                            + str(date_debut.tm_min)
                            + "  "+str(date_debut.tm_mday)
                            + "/"+str(date_debut.tm_mon)
                            + "/"+str(date_debut.tm_year)
                            + '      FIN : '
                            + str(date_fin.tm_hour)
                            + ":"
                            + str(date_fin.tm_min)
                            + "  "
                            + str(date_fin.tm_mday)
                            + "/"
                            + str(date_fin.tm_mon)
                            + "/"
                            + str(date_fin.tm_year)
                            )
                    else:
                        print(
                            'round '
                            + str(i)
                            + '         MATCH FAIT : '
                            + str(liste_tour[
                                'round ' + str(i)
                            ].nombre_match_fini)
                            + '/'
                            + str(liste_tour['round '+str(i)].nombre_match)
                            + "      DEBUT : "
                            + str(date_debut.tm_hour)
                            + ":"
                            + str(date_debut.tm_min)
                            + "  "
                            + str(date_debut.tm_mday)
                            + "/"
                            + str(date_debut.tm_mon)
                            + "/"
                            + str(date_debut.tm_year)
                            )
                    j += 1
                    i += 1
            if i <= len(liste_tour):
                print('rentrer le numero du round pour le selectionner  /  '
                      + '" " : afficher les 50 suivant  /  exit : revenir en'
                      + ' arriere /  end : revenir au menu principal')
                result = input()
            else:
                print('rentrer le numero du round pour le selectionner  /  '
                      + 'exit : revenir en arriere  /  end : revenir au menu'
                      + ' principal')
                result = input()
            if result == ' ' and i <= len(liste_tour):
                pas_fini = True
            elif result == 'exit':
                pas_fini = False
                lebontour = 'exit'
            elif result == 'end':
                pas_fini = False
                lebontour = 'end'
            # selection d'un round pour voir ses match
            # verifi si un numero
            elif result.isdigit():
                for cle in liste_tour.keys():
                    # regarde si un tournoi correspont a la demande
                    if cle == 'round '+str(result):
                        lebontour = cle
                if lebontour is not None:
                    pas_fini = False
                else:
                    print("ce tour n'existe pas")
            else:
                if i <= len(liste_tour):
                    print("je ne comprends pas votre reponse, veulliez "
                          + "repondre le numero du round pour le "
                          + "selectionner, ' ' pour afficher les 50 suivant"
                          + ", exit pour revenir en arriere ou end pour "
                          + "revenir au menu principal")
                else:
                    print("je ne comprends pas votre reponse, veulliez "
                          + "repondre le numero du round pour le selectionner"
                          + ", exit pour revenir en arriere ou end pour "
                          + "revenir au menu principal")
        return lebontour

    def affiche_match_tournoi(liste_match, liste_joueur, round):
        i = 0
        pas_fini = True
        print('LISTE DES MATCH DU '+round.upper())
        # affiche tout les match du tour
        while pas_fini and i < len(liste_match):
            if i < len(liste_match):
                j = 0
                # les affiche 50 par 50
                while j < 50 and i < len(liste_match):
                    c = 0
                    k = 0
                    # va chercher les info des joueur_tournoi dans joueur
                    while c <= 2 and k < len(liste_joueur):
                        if liste_joueur[k].id == \
                           liste_match[i][0][0].id_joueur:
                            joueur_un = liste_joueur[k]
                            c += 1
                        if liste_joueur[k].id == \
                           liste_match[i][1][0].id_joueur:
                            joueur_deux = liste_joueur[k]
                            c += 1
                        k += 1
                    if liste_match[i][0][1] == 1:
                        print(
                            joueur_un.nom
                            + '  '
                            + joueur_un.prenom
                            + '    /    '
                            + joueur_deux.nom
                            + '  '
                            + joueur_deux.prenom
                            + '   ->    '
                            + joueur_un.nom
                            + '  '
                            + joueur_un.prenom)
                    elif liste_match[i][0][1] == 0.5:
                        print(
                            joueur_un.nom
                            + '  '
                            + joueur_un.prenom
                            + '    /    '
                            + joueur_deux.nom
                            + '  '
                            + joueur_deux.prenom
                            + '   ->    EGALITE')
                    elif liste_match[i][1][1] == 1:
                        print(
                            joueur_un.nom
                            + '  '
                            + joueur_un.prenom
                            + '    /    '
                            + joueur_deux.nom
                            + '  '
                            + joueur_deux.prenom
                            + '   ->    '
                            + joueur_deux.nom
                            + '  '
                            + joueur_deux.prenom)
                    else:
                        print(
                            joueur_un.nom
                            + '  '
                            + joueur_un.prenom
                            + '    /    '
                            + joueur_deux.nom
                            + '  '
                            + joueur_deux.prenom
                            + '   ->    MATCH PAS FINI')
                    j += 1
                    i += 1
            # change les menu selon s'il reste ou pas des match
            if i < len(liste_match):
                print('1 : afficher les 50 suivant  /  2 : revenir en '
                      + 'arriere  /  3 : revenir au menu principal')
                result = input()
            else:
                print('2 : revenir en arriere  /  3 : revenir au menu '
                      + 'principal')
                result = input()
            if result == '1' and i < len(liste_match):
                pas_fini = True
            elif result == '2':
                pas_fini = False
                return ''
            elif result == '3':
                pas_fini = False
                return 'end'
            else:
                if i < len(liste_match):
                    print('je ne comprends pas votre reponse, veulliez '
                          + 'repondre 1 pour afficher les 50 suivant, 2 '
                          + 'pour revenir en arriere ou 3 pour revenir au '
                          + 'menu principal')
                else:
                    print('je ne comprends pas votre reponse, veulliez '
                          + 'repondre 2 pour revenir en arriere ou 3 pour'
                          + ' revenir au menu principal')

    def affiche_menu_tournoi(tournoi):
        c = 1
        # boucle pour permettre les erreurs inputb et le retour arriere
        while c:
            print("TOURNOI SELECTIONNE : "+tournoi.nom)
            print("lieu : "+tournoi.lieu)
            print("nombre de joueur : "+str(len(tournoi.liste_joueur)))
            date_debut = time.localtime(tournoi.date_start)
            print(
                'DEBUT : '
                + str(date_debut.tm_hour)
                + ":"
                + str(date_debut.tm_min)
                + "  "
                + str(date_debut.tm_mday)
                + "/"
                + str(date_debut.tm_mon)
                + "/"
                + str(date_debut.tm_year))
            if tournoi.date_end != 0:
                date_fin = time.localtime(tournoi.date_end)
                print(
                    'FIN : '
                    + str(date_fin.tm_hour)
                    + ":"
                    + str(date_fin.tm_min)
                    + "  "
                    + str(date_fin.tm_mday)
                    + "/"
                    + str(date_fin.tm_mon)
                    + "/"
                    + str(date_fin.tm_year))
            print("")
            print("")
            print("")
            print("ACTION :")
            print("1  :  liste de tout les joueur du tournois")
            print("2  :  liste de tout les tour du tournois")
            if tournoi.nombre_tour >= tournoi.tour:
                print("3  :  administrer le tournois")
            print("exit  :  pour revenir pour la liste des tournois")
            print("end  :  pour revenir au menu principal")
            result = input()
            # verifie les resultat de input est correct
            if result == '1' or result == '2' or result == 'exit' \
               or result == 'end':
                c = 0
                return result
            # on ne peut pas administrer un tournoi deja fini
            elif tournoi.nombre_tour >= tournoi.tour and result == '3':
                c = 0
                return result
            else:
                print("je ne comprends pas votre reponse, veuillez ecrire "
                      + "le nombre ou mot devant l'action voulu")

    def creation_tournoi(bdd):
        c = 1
        quitter = False
        # boucle pour revenir en arrire
        while not quitter and c:
            # liste des info a recupe
            liste_phrase = ['nom du tournoi',
                            'lieu du tournoi',
                            'nomnbre de tours',
                            'liste des joueurs en competition']
            liste_result = []
            i = 0
            # boucle pour revenir en arriere dans la question
            while not quitter and i < len(liste_phrase):
                valeur_ok = True
                print('CREATION DU JOUEUR')
                for j in range(i):
                    print(liste_phrase[j], ":", str(liste_result[j]))
                print("'back' pour revenir a la question precedente et "
                      + "'exit' pour quitter ce menu")
                # message change si on est en selection de joueur
                if i == 3:
                    while i == 3:
                        print(liste_phrase[i])
                        if liste_result[3] != []:
                            print('joueur deja selectionné')
                            for joueur in liste_result[3]:
                                print(joueur.nom, joueur.prenom)
                            if len(liste_result[3]) >= 2:
                                print(
                                    "si vous rentrer un joueur deja dans la "
                                    + "liste des selectionné alors cela le "
                                    + "retire. 'end' pour finir la selection,"
                                    + " 'back' pour revenir a la question "
                                    + "precedente et 'exit' pour quitter ce "
                                    + "menu")
                            else:
                                print(
                                    "si vous rentrer un joueur deja dans la "
                                    + "liste des selectionné alors cela le "
                                    + "retire. 'back' pour revenir a la "
                                    + "question precedente et 'exit' pour "
                                    + "quitter ce menu")
                        else:
                            print(
                                "si vous rentrer un joueur deja dans la liste"
                                + " des selectionné alors cela le retire. "
                                + "'back' pour revenir a la question "
                                + "precedente et 'exit' pour quitter ce menu")
                        print('nom du joueur :')
                        nom = input()
                        if nom == 'back':
                            i += -1
                            valeur_ok = False
                        # permet de quitter lors de cette selection
                        elif nom == 'end':
                            i += 1
                        # permet de quitter lors de cette selection
                        elif nom == 'exit':
                            quitter = True
                            valeur_ok = False
                        else:
                            print('prenom du joueur :')
                            prenom = input()
                            trouver = False
                            # cherche le joueur
                            for joueur in bdd.liste_joueur:
                                if joueur.nom == nom and \
                                   joueur.prenom == prenom:
                                    trouver = True
                                    # ajout ou supprime la personne
                                    if joueur not in liste_result[3]:
                                        liste_result[3].append(joueur)
                                        print("joueur ajouté")
                                    else:
                                        liste_result[3].remove(joueur)
                                        print("joueur supprimé")
                            if not trouver:
                                print("le joueur n'est pas present dans la "
                                      + "base de donnée du logiciel")
                # si on selectionne pas les joueur
                else:
                    print(liste_phrase[i])
                    result = input()
                    if result == 'back':
                        if i != 0:
                            i += -1
                        valeur_ok = False
                    elif result == 'exit':
                        quitter = True
                        valeur_ok = False
                    elif i == 3 and len(result[3]) >= 2 and result == 'end':
                        i += 1
                        valeur_ok = False
                    elif i == 2:
                        if not result.isdigit():
                            valeur_ok = False
                            print("ceci n'est pas un chiffre valide")
                if valeur_ok:
                    if i >= len(liste_result):
                        liste_result.append(result)
                        i += 1
                        if i == 3:
                            # creer ou vide la liste pour les joueur
                            # du tournoi
                            if len(liste_result) < 4:
                                liste_result.append([])
                            else:
                                liste_result[3] = []
                    else:
                        liste_result[i] = result
                        i += 1
            j = 1
            # boucle pour les faute d'input
            while not quitter and j:
                # recapitulatif des données du tournoi
                print("VOULEZ VOUS VRAIMENT ENREGISTRER LE JOUEUR SUIVANT :")
                print("nom :", liste_result[0])
                print("lieu :", liste_result[1])
                print("nombre de tour :", liste_result[2])
                liste_joueur_inscript = ""
                for joueur in liste_result[3]:
                    liste_joueur_inscript += joueur.nom+' '+joueur.prenom+"; "
                liste_joueur_inscript = liste_joueur_inscript[:-2]
                print("joueur inscrit :", liste_joueur_inscript)
                print('1 : oui  /  2 : nom')
                result = input()
                if result == '1':
                    print('le tournoi va etre enregistré')
                    j = 0
                    c = 0
                elif result == '2':
                    j = 0
                else:
                    print('je ne comprends pas votre reponse, veulliez '
                          + 'repondre 1 pour oui et 2 pour non')
        if quitter:
            liste_result = []
        return liste_result

    def admin_tournoi():
        print("id du tournoi a administrer ou 'exit' pour revenir au "
              + "menu princial")
        id_voulu = input()
        # check que la reponse soit possible
        if id_voulu == 'exit' or id_voulu.isdigit():
            return id_voulu
        else:
            print("reponse incorrecte veuillez rentrer le numero qui fait "
                  + "l'id du tournoi pour le selectionner si vous le "
                  + "connaissez pas aller le recuperer dans la liste des "
                  + "tournois ou exit pour revenir au menu principal")

    def admin_tournoi_la(tournoi, liste_joueur):
        print("LE TOURNOI EST AU ROUND "+str(tournoi.tour))
        print("LES MATCH PAS FINI SONT :")
        i = 0
        pas_fini = True
        print('LISTE DES TOUR')
        lebonmatch = [None]
        liste_match = tournoi.liste_tour[
            'round '+str(tournoi.tour)
        ].liste_match
        # pour permettre les faute input
        while pas_fini:
            if i < len(liste_match):
                j = 0
                # affiche les matchs 50 par 50
                while j < 50 and i < len(liste_match):
                    if liste_match[i][0][1] == -1:
                        c = 0
                        k = 0
                        # recupere info de joueur_tournoi dans joueur
                        while c <= 2 and k < len(liste_joueur):
                            if liste_joueur[k].id == liste_match[
                                i
                            ][
                                0
                            ][
                                0
                            ].id_joueur:
                                joueur_un = liste_joueur[k]
                                c += 1
                            if liste_joueur[k].id == liste_match[
                                i
                            ][
                                1
                            ][
                                0
                            ].id_joueur:
                                joueur_deux = liste_joueur[k]
                                c += 1
                            k += 1
                        print(str(i) + '         ' + joueur_un.nom
                              + '  ' + joueur_un.prenom + '/'
                              + joueur_deux.nom + '  ' + joueur_deux.prenom)
                        j += 1
                    i += 1
            # menu change si tout afficher ou non
            if i < len(liste_match):
                print('rentrer le numero du match pour le selectionner  / '
                      + ' " " : afficher les 50 suivant  /  exit : revenir en'
                      + ' arriere /  end : revenir au menu principal')
                result = input()
            else:
                print('rentrer le numero du match pour le selectionner  / '
                      + ' exit : revenir en arriere  /  end : revenir au menu'
                      + ' principal')
                result = input()
            if result == ' ' and i < len(liste_match):
                pas_fini = True
            elif result == 'exit':
                pas_fini = False
                lebonmatch[0] = 'exit'
            elif result == 'end':
                pas_fini = False
                lebonmatch[0] = 'end'
            # selection de match par id donc nombre
            elif result.isdigit():
                if int(result) < len(liste_match):
                    if liste_match[int(result)][0][1] == -1:
                        c = 1
                        lebonmatch[0] = result
                        # boucle pour faute input
                        while c:
                            cc = 0
                            k = 0
                            # recupe info joueur
                            while c <= 2 and k < len(liste_joueur):
                                if liste_joueur[k].id == liste_match[
                                    int(result)
                                ][
                                    0
                                ][
                                    0
                                ].id_joueur:
                                    joueur_un = liste_joueur[k]
                                    cc += 1
                                if liste_joueur[k].id == liste_match[
                                    int(result)
                                ][
                                    1
                                ][
                                    0
                                ].id_joueur:
                                    joueur_deux = liste_joueur[k]
                                    cc += 1
                                k += 1
                            print("0 : pour egalité, 1 si " + joueur_un.nom
                                  + "  "+joueur_un.prenom+" a gagné, 2 si "
                                  + joueur_deux.nom+"  "+joueur_deux.prenom
                                  + " a gagné ou 3 pour selectionner un autre"
                                  + " match")
                            re_result = input()
                            if re_result == '0':
                                lebonmatch.append(0)
                                c = 0
                                pas_fini = False
                            elif re_result == '1':
                                lebonmatch.append(1)
                                c = 0
                                pas_fini = False
                            elif re_result == '2':
                                lebonmatch.append(2)
                                c = 0
                                pas_fini = False
                            elif re_result == '3':
                                c = 0
                            else:
                                print("cette reponse n'est pas valide")
                    else:
                        print("ce match est deja fini")
                else:
                    print("ce tour n'existe pas")
            else:
                if i < len(liste_match):
                    print("je ne comprends pas votre reponse, veulliez "
                          + "repondre le numero du round pour le selectionner"
                          + ", ' ' pour afficher les 50 suivant, exit pour "
                          + "revenir en arriere ou end pour revenir au menu "
                          + "principal")
                else:
                    print("je ne comprends pas votre reponse, veulliez "
                          + "repondre le numero du round pour le selectionner"
                          + ", exit pour revenir en arriere ou end pour "
                          + "revenir au menu principal")
        return lebonmatch
