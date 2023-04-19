from joueur import joueur
import networkx as nx
import random

import matplotlib.pyplot as plt

def trie(list_joueur):
    liste_joueurtrier = []
    for joueur in list_joueur:
        pasmi = True
        pos = 0
        while pasmi and pos<len(liste_joueurtrier):
            if liste_joueurtrier[pos].score < joueur.score:
                pasmi = False
            pos += 1
        if pasmi:
            liste_joueurtrier.append(joueur)
        else:
            liste_joueurtrier.insert(pos-1, joueur)
    if len(liste_joueurtrier) != len(list_joueur):
        print("ATTENTION LA CA PU ezuyigfdyezgfbhzfyuzhfvbyuzfguyzfhgyugzyfugzyfugyzfgzfgzyfguyzfguhzegfhjuzgfhuizghyfgzsukcghdsyufgudsyfgusygfyzsegfuye")
    # for i in liste_joueurtrier:
    #     print(i.nom, i.score)
    return liste_joueurtrier

def fonctiontest(liste_joueurtrier, matchdejafait):
    compteur = 0
    listepaire = []
    listejoueurnontrouver = []
    enregistrelistela = []
    while len(liste_joueurtrier) > 1:
        joueurun = liste_joueurtrier.pop(0)
        pasTrouve = True
        pos = 0
        while pasTrouve and pos<len(liste_joueurtrier):
            enregistrelistela.append((liste_joueurtrier[pos], joueurun))
            if liste_joueurtrier[pos] in joueurun.list_joueurPasDejaVu:
                pasTrouve = False
            pos += 1
        if pasTrouve:
            compteur += 0.5
            listejoueurnontrouver.append(joueurun)
        else:
            # print(len(liste_joueurtrier))
            # print(pos)
            joueurdeux = liste_joueurtrier.pop(pos - 1)
            # print(joueurun.list_joueurDejaVu)
            joueurun.list_joueurPasDejaVu.remove(joueurdeux)
            joueurdeux.list_joueurPasDejaVu.remove(joueurun)
            joueurun.list_joueurDejaVu.append(joueurdeux)
            joueurdeux.list_joueurDejaVu.append(joueurun)
            listepaire.append((joueurun, joueurdeux))
    if len(liste_joueurtrier) == 1:
        compteur += 0.5
        listejoueurnontrouver.append(liste_joueurtrier[0])
    print("il y a "+str(compteur)+" paire mauvaise")
    while len(listejoueurnontrouver) > 0:
        # print(listepaire)
        joueurun = listejoueurnontrouver.pop(0)
        listepaire, listejoueurnontrouver = commencementgraph(joueurun, listejoueurnontrouver, listepaire, enregistrelistela)
    for paire in listepaire:
        result(paire)
    matchdejafait, compteurnouveau = testepaire(listepaire, matchdejafait)
    print("apres modif il y a "+str(compteurnouveau)+" paire fausse")
    return matchdejafait


def testepaire(listepaire, matchdejafait):
    print("la je test les paires")
    compteur = 0
    for match in matchdejafait:
        for paire in listepaire:
            if (paire[0], paire[1]) in match or (paire[1], paire[0]) in match:
                compteur += 1
            if paire[1] in paire[0].list_joueurPasDejaVu:
                print("erreur joueur pas deja vu")
            if not paire[1] in paire[0].list_joueurDejaVu:
                print("erreur joueur deja vu")
            if paire[0] in paire[1].list_joueurPasDejaVu:
                print("erreur joueur pas deja vu")
            if not paire[0] in paire[1].list_joueurDejaVu:
                print("erreur joueur deja vu")
    matchdejafait.append(listepaire)
    return matchdejafait,compteur

def result(paire):
    gagnant = random.randint(0, 3)
    if gagnant == 0:
        paire[0].score += 1
    elif gagnant == 1:
        paire[1].score += 1
    else:
        paire[0].score += 0.5
        paire[1].score += 0.5

def jetestlapaire(paire, toutlesmatch, graph):
    if not (paire[0], paire[1]) in toutlesmatch and not (paire[1], paire[0]) in toutlesmatch:
        print("bigbigerreur")
        print(paire[0].nom, paire[1].nom)
        affichegraph(graph)
    

def testmatch(toutlesnoeud, toutlesmatch):
    pasbon = True
    c = 0
    while pasbon and c<len(toutlesnoeud):
        joueurun = toutlesnoeud[c][0]
        joueurdeux = toutlesnoeud[c][1]
        if (joueurun, joueurdeux) in toutlesmatch or (joueurdeux, joueurun) in toutlesmatch:
            pasbon=False
        else:
            c+=1
    return joueurdeux


def parcourgraph(debut, fin, graph, pas, toutlesmatch, enregistrelistela, listedejatest=[],compteur=0):
    # print(toutlesmatch)
    lui = debut
    gpas = True
    # print("je me rappel d'un temps ou je n'avais pas ca " + str(pas) + " " + str(compteur))
    if pas != 0:
        listedejatest.append(lui)
        lesarretes = list(graph.out_edges(lui))
        j = 0
        while gpas and j<len(lesarretes):
            if not lesarretes[j][1] in listedejatest:
                lenoeudsuivant = list(graph.out_edges(lesarretes[j][1]))
                listedejatest.append(lenoeudsuivant[0])
                lebonnoeud = testmatch(lenoeudsuivant, toutlesmatch)
                # listedejatest.append(lebonnoeud)
                # print(len(lenoeudsuivant))
                # for i in lenoeudsuivant:
                #     jetestlapaire(i, toutlesmatch, graph)
                # IL FAUT VERIFIER QUE CELUI PRIS SOIT BIEN CELUI QUI EXISTE ET COMME CA MEME POUR LA SUPPRESSION CA DEVRAI ALLER !!!!
                result, graph, toutlesmatch, fin = parcourgraph(lebonnoeud, fin, graph, pas-1, toutlesmatch, enregistrelistela, listedejatest=listedejatest,compteur=j)
                if result:
                    gpas = False
                    toutlesmatch = retirmatch(lesarretes[j][1], lebonnoeud, toutlesmatch, compteur)
                    toutlesmatch = ajoutmatch(lui, lesarretes[j][1], toutlesmatch)
                else:
                    j += 1
                listedejatest.remove(lenoeudsuivant[0])
            else:
                result = False
                j+=1
        listedejatest.remove(lui)
        return result, graph, toutlesmatch, fin
    else:
        possibilite, graph = ressorttoutelespossibilit(lui, graph)
        pos = 0
        cpasbon = True
        while cpasbon and pos<len(possibilite):
            if not possibilite[pos] in listedejatest:
                # print(toutlesmatch)
                aveclui, graph = matchcreer(possibilite[pos], toutlesmatch, graph, fin, debut, enregistrelistela)
                cpossiblite, graph = ressorttoutelespossibilit(aveclui, graph)
                poslui = 0
                while cpasbon and poslui<len(fin):
                    if fin[poslui] in cpossiblite:
                        cpasbon = False
                    else:
                        poslui += 1
            pos += 1
        if cpasbon:
            return False, graph, toutlesmatch, fin
        else:
            toutlesmatch = ajoutmatch(fin[poslui], aveclui, toutlesmatch)
            toutlesmatch = retirmatch(possibilite[pos-1], aveclui, toutlesmatch, 1)
            toutlesmatch = ajoutmatch(possibilite[pos-1], lui, toutlesmatch)
            fin.pop(poslui)
            return True, graph, toutlesmatch, fin


def commencementgraph(debut, fin, toutlesmatch, enregistrelistela):
    pastrouver = True
    pas = 0
    graph = nx.DiGraph()
    graph.add_node(debut)
    while pastrouver:
        # print(toutlesmatch)
        result, graph, toutlesmatch, fin = parcourgraph(debut, fin, graph, pas, toutlesmatch, enregistrelistela, compteur=-1)
        if result:
            pastrouver = False
        else:
            pas += 1
            print("je passe ici cet fois enfin !!!!")
    return toutlesmatch, fin


def ressorttoutelespossibilit(lui, graph):
    possiblite = []
    envoiegraph = []
    for joueurla in lui.list_joueurPasDejaVu:
        cpasbon = True
        pos = 0
        while cpasbon and pos<len(possiblite):
            if abs(lui.score - joueurla.score) < abs(lui.score - possiblite[pos].score):
                cpasbon = False
            pos += 1
        if cpasbon:
            possiblite.append(joueurla)
            envoiegraph.append((lui, joueurla))
        else:
            possiblite.insert(pos-1, joueurla)
            envoiegraph.insert(pos-1, (lui, joueurla))
    graph.add_edges_from(envoiegraph)
    return possiblite, graph


def matchcreer(lui, toutlesmatch, graph, lalistela, debut, enregistrelistela):
    # print(toutlesmatch)
    aveclui = None
    for paire in toutlesmatch:
        # print(paire[0].nom, paire[1].nom)
        # print("jepasseici")
        # print(lui.nom)
        if lui in paire:
            aveclui = paire[paire.index(lui) - 1]
            # print(lui.nom, aveclui.nom)
            graph.add_edge(lui, aveclui)
            # print("jepasseici")
    if aveclui == None:
        for paire in toutlesmatch:
            print(paire[0].nom, paire[1].nom)
        print(lui.nom)
        print(debut.nom)
        for i in enregistrelistela:
            if debut in i:
                print(i[0].nom, i[1].nom)
        for i in enregistrelistela:
            if lui in i:
                print(i[0].nom, i[1].nom)
        if lui in debut.list_joueurPasDejaVu:
            print("alors la je ne comprend absolument rien ptn !")
        print(graph)
        for i in lalistela:
            print(i.nom)
        affichegraph(graph)
    return aveclui, graph

def affichegraph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, arrows=True)
    plt.show()


def ajoutmatch(joueurUn, joueurDeux, toutlesmatch):
    joueurUn.list_joueurPasDejaVu.remove(joueurDeux)
    joueurDeux.list_joueurPasDejaVu.remove(joueurUn)
    joueurUn.list_joueurDejaVu.append(joueurDeux)
    joueurDeux.list_joueurDejaVu.append(joueurUn)
    toutlesmatch.append((joueurUn, joueurDeux))
    return toutlesmatch

def retirmatch(joueurUn, joueurDeux, toutlesmatch, quimappel):
    paire = [(joueurUn, joueurDeux),(joueurDeux, joueurUn)]
    if paire[0] in toutlesmatch:
        toutlesmatch.remove(paire[0])
        joueurUn.list_joueurPasDejaVu.append(joueurDeux)
        joueurDeux.list_joueurPasDejaVu.append(joueurUn)
        joueurUn.list_joueurDejaVu.remove(joueurDeux)
        joueurDeux.list_joueurDejaVu.remove(joueurUn)
    elif paire[1] in toutlesmatch:
        toutlesmatch.remove(paire[1])
        joueurUn.list_joueurPasDejaVu.append(joueurDeux)
        joueurDeux.list_joueurPasDejaVu.append(joueurUn)
        joueurUn.list_joueurDejaVu.remove(joueurDeux)
        joueurDeux.list_joueurDejaVu.remove(joueurUn)
    else:
        print("attention pas de match supprmier la :(" + str(quimappel))
        if quimappel == 0:
            print("cle0quimappel")
        if quimappel == 1:
            print("cle0quimappel")
    return toutlesmatch





# def testnoeud(noeud, jeveuxeux, graph):
#     listejoueurtrier = []
#     for joueurla in noeud.list_joueurDejaVu:
#         cpasbon = True
#         pos = 0
#         while cpasbon and pos<len(listejoueurtrier):
#             if abs(noeud.score - joueurla.score) < abs(noeud.score - listejoueurtrier[pos].score):
#                 cpasbon = False
#             pos += 1
#         if cpasbon:
#             listejoueurtrier.append(joueurla)
#         else:
#             listejoueurtrier.insert(pos-1, joueurla)
#     cpasbon = True
#     pos = 0
#     while cpasbon and pos<len(listejoueurtrier):
#         for lui in jeveuxeux:
#             if lui in listejoueurtrier[pos].list_joueurDejaVu:
#                 cpasbon = False
#                 aveclui = lui
#         else:
#             graph.add_edge(noeud, listejoueurtrier[pos])
#         pos += 1
#     if cpasbon:
#         return False, graph
#     else:
#         return True, aveclui, listejoueurtrier[pos-1]
        


def printtout(matchdejafait):
    for match in matchdejafait:
        for paire in match:
            print(paire[0].nom, paire[1].nom)




class joueurTournoi(joueur):

    def __init__(self, name) -> None:
        super().__init__(name, "prenom", "naissance")
        self.score = 0
        self.list_joueurPasDejaVu = []
        self.list_joueurDejaVu = []
    
    def ajoutlistedejavula(self, listejoueur):
        listejoueur.remove(self)
        self.list_joueurPasDejaVu = listejoueur

list_joueurcreer = []
matchdejafait = []
# for i in range(random.randrange(100, 1000, 2)):
for i in range(250):
    list_joueurcreer.append(joueurTournoi(str(i)))
for joueurla in list_joueurcreer:
    joueurla.ajoutlistedejavula(list(list_joueurcreer))
compteurdetour = 0
for i in range(len(list_joueurcreer)):
    compteurdetour+=1
    matchdejafait = fonctiontest(trie(list_joueurcreer),matchdejafait)
    print("on a fait "+str(compteurdetour)+" tour")
    # for joueurla in list_joueurcreer:
        # print(joueurla.list_joueurDejaVu)
    # printtout(matchdejafait)
    if list_joueurcreer[0].list_joueurPasDejaVu == []:
        for joueurla in list_joueurcreer:
            joueurla.ajoutlistedejavula(list(list_joueurcreer))
printtout(matchdejafait)
print(len(list_joueurcreer))