import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=6, relation='family')
G.add_edge('B', 'C', weight=13, relation='friend')

# %% New ipython cell ================

# List of all edges
G.edges()

# %% New ipython cell ================

# data = True to show all attributes the edge has
G.edges(data=True)

# %% New ipython cell ================

# How we just show the relation
G.edges(data='relation')

# %% New ipython cell ================

# We can access an edge like so:
G['A']['B']
# This returns a dictionary with all attributes of that edge

# %% New ipython cell ================

G['B']['C']['weight']

# %% New ipython cell ================

G['C']['B']['weight']

# %% New ipython cell ================

G = nx.MultiGraph()
G.add_edge('A', 'B', weight=6, relation='family')
G.add_edge('A', 'B', weight=18, relation='friend')
G.add_edge('C', 'B', weight=13, relation='friend')

# %% New ipython cell ================

# As now we have a multigraph, this will return a dictionary of dicionaries
G['A']['B']

# %% New ipython cell ================

# This returns the first edge
G['A']['B'][0]

# %% New ipython cell ================

# Even if there's only one edge between two nodes, it will be a dictionary with
# just one dictionary. That good, because them we don't need to care much about
# if the nodes have just one edge or multiple ones.
G['C']['B']

# %% New ipython cell ================

# We can also have *node attributes*
G.add_node('A', role='trader')
G.add_node('B', role='trader')
G.add_node('C', role='manager')

# %% New ipython cell ================

# And we can access them just like the edges
G.nodes()

# %% New ipython cell ================

G.nodes(data=True)

# %% New ipython cell ================

G.nodes(data='role')

# %% New ipython cell ================

# To access a node, we can use:
G.nodes['A']

# %% New ipython cell ================

G.nodes['A']['role']
