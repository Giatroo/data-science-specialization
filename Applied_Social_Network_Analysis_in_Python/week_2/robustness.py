import networkx as nx

# Robustness is the ability of a network to maintain its general structural
# properties when it faces failures or attacks.

# In our case:
# Attacks would be the removal of nodes or edges.
# And the structural properties would be its connectivity.

# It's important on some cases like:
# airport closures, internet router failures or power line failures

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

nx.node_connectivity(G)

# %% New ipython cell ================

# If we remove 'E', than the network will not be connected anymore
nx.minimum_node_cut(G)

# %% New ipython cell ================

nx.edge_connectivity(G)

# %% New ipython cell ================

# If we remove the edge ('F', 'G'), than the network will not be connected
# anymore
nx.minimum_edge_cut(G)

# Robust networks need many nodes or edges removed to become disconnected

# %% New ipython cell ================

# This is the amount of nodes we need to remove to block the 'comunication'
# between 'A' and 'E'
nx.node_connectivity(G, 'A', 'E')

# %% New ipython cell ================

# In this case, we just need to remove 'C'
nx.minimum_node_cut(G, 'A', 'E')

# %% New ipython cell ================

# As you can see, 'C' is present in all paths from 'A' to 'E'
list(nx.all_simple_paths(G, 'A', 'E'))

# %% New ipython cell ================

# And, of course, we can do the same for edges:
nx.edge_connectivity(G, 'A', 'E')

# %% New ipython cell ================

nx.minimum_edge_cut(G, 'A', 'E')
