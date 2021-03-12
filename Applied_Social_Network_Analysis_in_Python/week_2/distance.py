import networkx as nx

# %% New ipython cell ================

G = nx.Graph()
G.add_edges_from([('A', 'K'),
                  ('A', 'B'),
                  ('B', 'C'),
                  ('B', 'K'),
                  ('C', 'E'),
                  ('C', 'F'),
                  ('D', 'E'),
                  ('E', 'F'),
                  ('E', 'H'),
                  ('E', 'I'),
                  ('F', 'G'),
                  ('I', 'J')])

# %% New ipython cell ================

# Distance between two points:
nx.shortest_path(G, 'A', 'H')

# %% New ipython cell ================

nx.shortest_path_length(G, 'A', 'H')

# %% New ipython cell ================

# BFS:
T = nx.bfs_tree(G, 'A')
T.edges()

# %% New ipython cell ================

# Distance of all nodes to a source node:
nx.shortest_path_length(G, 'A')

# %% New ipython cell ================

# Global distance measures:
# Average distance:
nx.average_shortest_path_length(G)

# %% New ipython cell ================

# Diameter: (maximum distance between any pair of nodes)
nx.diameter(G)

# %% New ipython cell ================

# Eccentricity: (maximum distance that a node is from a specific node)
nx.eccentricity(G)
# Lower eccentricity means a node is on the center of the graph

# %% New ipython cell ================

# Radius: (minimum eccentricity)
nx.radius(G)

# %% New ipython cell ================

# The periphery is the set of nodes that have eccentricity equal to the
# diameter:
nx.periphery(G)

# %% New ipython cell ================

# The center is the set of nodes that have eccentricity equal to the radius
nx.center(G)

# %% New ipython cell ================

# Let's test those concepts in a real network:
G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)

# %% New ipython cell ================

nx.average_shortest_path_length(G)

# %% New ipython cell ================

nx.radius(G)

# %% New ipython cell ================

nx.diameter(G)

# %% New ipython cell ================

nx.periphery(G)

# %% New ipython cell ================

nx.center(G)
