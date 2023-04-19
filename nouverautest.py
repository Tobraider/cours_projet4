import networkx as nx
test = [1,2,3,4]
test.append((5,6))
# print(test[6])
import networkx as nx

# Créer un graphe non orienté
G = nx.Graph()

# Ajouter des nœuds et des arêtes au graphe
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4)])

# Récupérer toutes les arêtes connectées à un nœud spécifique
edges_of_node_3 = G.edges(3)

# Afficher les arêtes connectées à un nœud spécifique
print(edges_of_node_3)


import matplotlib.pyplot as plt

# créer un graphe orienté
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edge(1, 2)  # ajouter une arête orientée de 1 à 2
G.add_edge(2, 3)  # ajouter une arête orientée de 2 à 3
G.add_edge(3, 4)  # ajouter une arête orientée de 3 à 4

# dessiner le graphe
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, arrows=True)
plt.show()
