import networkx as nx
from networkx.algorithms import bipartite

# %% New ipython cell ================

B = nx.Graph()
# bipartite = 0 means that these nodes are going to be one side of my bipartite
# graph (one set)
B.add_nodes_from(['A', 'B', 'C', 'D', 'E'], bipartite=0)
B.add_nodes_from([1, 2, 3, 4], bipartite=1)

# %% New ipython cell ================

B.add_edges_from([('A', 1), ('B', 1), ('C', 1), ('C', 3),
                  ('D', 2), ('E', 3), ('E', 4)])

# %% New ipython cell ================

# Inside bipartite, we have some algorithms we can perform
bipartite.is_bipartite(B)

# %% New ipython cell ================

B.add_edge('A', 'B')
bipartite.is_bipartite(B)

# %% New ipython cell ================

B.remove_edge('A', 'B')

# %% New ipython cell ================

# We can ask if a set of nodes is a bipartition of the graph
X = {1, 2, 3, 4}
bipartite.is_bipartite_node_set(B, X)

# %% New ipython cell ================

X = {'A', 'B', 'C', 'D', 'E'}
bipartite.is_bipartite_node_set(B, X)

# %% New ipython cell ================

X = {1, 2, 3, 4, 'A'}
bipartite.is_bipartite_node_set(B, X)

# %% New ipython cell ================

bipartite.sets(B)

# %% New ipython cell ================

B = nx.Graph()
B.add_edges_from([('A', 1), ('B', 1), ('C', 1), ('D', 1), ('H', 1),
                  ('B', 2), ('C', 2), ('D', 2), ('E', 2), ('G', 2),
                  ('E', 3), ('F', 3), ('H', 3), ('J', 3),
                  ('E', 4), ('I', 4), ('J', 4)])

X = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'}
P = bipartite.projected_graph(B, X)
P.edges()

# %% New ipython cell ================

X = {1, 2, 3, 4}
P = bipartite.projected_graph(B, X)
P.edges()

# %% New ipython cell ================

P = bipartite.weighted_projected_graph(B, X)
P.edges(data=True)

# %% New ipython cell ================

bipartite.sets(B)
