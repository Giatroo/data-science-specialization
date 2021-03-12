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

nx.is_connected(G)

# %% New ipython cell ================

nx.number_connected_components(G)

# %% New ipython cell ================

G.remove_edge('D', 'E')

# %% New ipython cell ================

nx.number_connected_components(G)

# %% New ipython cell ================

gen = nx.connected_components(G)

# %% New ipython cell ================

next(gen)

# %% New ipython cell ================

next(gen)

# %% New ipython cell ================

nx.node_connected_component(G, 'I')
