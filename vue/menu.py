class Menu():

    def affiche():
        c = 1
        # pour repeter la question si mauvaise rep
        while c:
            print('QUE VOULEZ VOUS FAIRE')
            print("0 : voir tout les joueur par ordre alphabetique")
            print("1 : enregistrer un nouveau joueur")
            print("2 : voir tout les tournois")
            print("3 : creer un nouveau tournoi")
            print("4 : administer un tournoi")
            print("5 : quitter")
            print("veuillez rentrer le numero de l'action voulu puis appuye"
                  + "z sur 'entrer'")
            result = input()
            # check que la rep est bonne
            if result == '0' or result == '1' or result == '2' \
               or result == '3' or result == '4' or result == '5':
                c = 0
                return result
            else:
                print('valeur incorrecte')
