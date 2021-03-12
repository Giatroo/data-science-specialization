import networkx as nx

# Clustering Coefficient measure the degree to which nodes in a network tend to
# 'cluster' or form triangles.

# %% New ipython cell ================

# Local Clustering Coefficient:
# It's the number of connections between the neighbors of a node divided by the
# maximum number of connection the neighbors could have.

# So if a node has a degree of 4 (i.e. 4 neighbors), then the possible amount of
# connections between them is (4*(4-1))/2 = 6. If there are just two of these
# six possible connections, then the local clustering coef is equal to 2/6=1/3

G = nx.Graph()
G.add_edges_from([('A', 'K'),
                  ('A', 'B'),
                  ('A', 'C'),
                  ('B', 'C'),
                  ('B', 'K'),
                  ('C', 'E'),
                  ('C', 'F'),
                  ('D', 'E'),
                  ('E', 'F'),
                  ('E', 'H'),
                  ('F', 'G'),
                  ('I', 'J')])

# %% New ipython cell ================

nx.clustering(G, 'F')

# %% New ipython cell ================

nx.clustering(G, 'A')

# %% New ipython cell ================

# If a node has a degree of 1, it's local clustering coef is zero by def.
nx.clustering(G, 'I')

# %% New ipython cell ================

# Global Clustering Coefficient:

# There are two ways to get a global measure of global clustering.
# The 1) is to average all the local clusterings:
nx.average_clustering(G)

# %% New ipython cell ================

# The 2) is to count the number of 'open triads' and 'closed triads'

# An 'open triad' is a subgraph with three nodes that are connected by two
# edges.
# An 'closed triads' (or a triangle) is a subgraph with three nodes that are
# connected by three edges.

# Each 'closed triads' has 3 'open triads' inside it, so the formula is:
# Transitivity = (3*closed)/(open)

# And that give us the percentage of 'open triads' that are triangles in a
# network.

nx.transitivity(G)
