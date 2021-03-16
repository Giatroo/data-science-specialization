import networkx as nx
G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)

# %% New ipython cell ================

# Degree centrality makes the assumption that important nodes have many
# connections. That's the most basic measure of centrality: number of neighbors
# (or degree of a node)

# In a directed network, we must choose between the in and out degree or a
# combination of both

# We define the degree centrality in an undirected network as
# C_deg(v) = d_v / (N-1)

# where d_v is the degree of a vertex v and N is the number of nodes in the
# graph.

# Therefore, a node has a degree centrality of 1 if it's connected to every
# other node in the network.

degCent = nx.degree_centrality(G)
degCent # this returns a dictionary with every node

# %% New ipython cell ================

# For directed graphs, we can use
# nx.in_degree_centrality(G)
# or
# nx.out_degree_centrality(G)

# %% New ipython cell ================

# Closeness centrality makes the assumption that important nodes are close to
# other nodes.

# For a node v, we define it as N-1 divided by the sum of the distance from v to
# u, where u iterates through all nodes.

closeCent = nx.closeness_centrality(G)
closeCent

# %% New ipython cell ================

closeCent[32]

# %% New ipython cell ================

# Let's see how to get this value
s = sum(nx.shortest_path_length(G, 32).values())

# %% New ipython cell ================

# Same value
(len(G.nodes())-1)/s

# %% New ipython cell ================

# Of course, we are making the assumption that all nodes are connected.
# We have a few options.

# One option is instead of having N-1 in the numerator, we consider only the
# amount of nodes a particular node can reach.

# A second option is again considering only the nodes a particular node can
# reach, but we also normalize the value to make it more fair between big and
# small components.

nx.closeness_centrality(G, wf_improved=True)

# Here the values are actually the same because there's just one component.
