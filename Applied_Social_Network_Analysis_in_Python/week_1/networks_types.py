import networkx as nx

# %% New ipython cell ================

G = nx.Graph()

# %% New ipython cell ================

G.add_edge('A', 'B')
G.add_edge('B', 'C')

# %% New ipython cell ================

# A directed graph:
G = nx.DiGraph()
G.add_edge('A', 'B') # A -> B
G.add_edge('B', 'C') # B -> C

# %% New ipython cell ================

# Weighted networks:
G = nx.Graph()
G.add_edge('A', 'B', weight=6)
G.add_edge('A', 'B', weight=30)

# %% New ipython cell ================

# Signed networks (each edge have a + ou - sign)
G = nx.Graph()
G.add_edge('A', 'B', sign='+')
G.add_edge('B', 'C', sign='-')

# %% New ipython cell ================

# Each edge can have a category (or relation)
G = nx.Graph()
G.add_edge('A', 'B', relation='friend')
G.add_edge('B', 'C', relation='coworker')
G.add_edge('D', 'E', relation='family')
G.add_edge('E', 'I', relation='neighbor')

# %% New ipython cell ================

# Multigraphs:
G = nx.MultiGraph()
G.add_edge('A', 'B', relation='friend')
G.add_edge('A', 'B', relation='neighbor')
