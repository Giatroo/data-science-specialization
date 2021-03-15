import networkx as nx
G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)

# %% New ipython cell ================

# Betweenness Centrality makes the assumption that important nodes are those
# that connect other nodes.

# We define the betweeness centrality of a node v by picking two nodes s and t
# and getting the ratio of how many times v appers in a shortest path from s to
# t divided by the total number of shortest paths between those two nodes. And
# we sum all of these ratios for every node in our network.

# One decision we have to make is if the node v can be s or t.

# Sometimes it's also good to normalize the betweeness centrality to compare
# these values between different networks. To do so, we divide the centrality of
# a node by the number of possible paths that graph could have excluding the
# node.
# If it's an undirected graph, it's (N-1)(N-2)/2 and if it's an directed graph,
# it's (N-1)(N-2)

btwnCent = nx.betweenness_centrality(G, normalized=True, endpoints=False)
btwnCent

# %% New ipython cell ================

import operator
sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5]

# %% New ipython cell ================

# The problem with betweeness centrality is that it's very expensive. The
# algorithm takes O(N^3) time.
# We can though use an approximation and don't check all pairs s,t, but just a
# sample of them.
btwnCent_approx = nx.betweenness_centrality(G, normalized=True,
                                            endpoints=False, k=10)
sorted(btwnCent_approx.items(), key=operator.itemgetter(1), reverse=True)[:5]

# We use k to determine the number of pairs to compute.
# If you run this cell again, you will see the results change, because it's a
# random sample.

# %% New ipython cell ================

# We can also just use a subset of nodes that are important to us and just look
# at pairs presents in a subset of targets and a subset of sources
btwCent_subset = nx.betweenness_centrality_subset(G,
                                 [34, 33, 21, 30, 16, 27, 15, 23, 10],
                                 [1, 4, 13, 11, 6, 12, 17, 7],
                                 normalized=True)
btwCent_subset

# Here, t will always be a node from the target subset and s will always be a
# node from the source subsets.

# %% New ipython cell ================

# We also can use this concept to edges
btwnCent_edge = nx.edge_betweenness_centrality(G, normalized=True)
sorted(btwnCent_edge.items(), key=operator.itemgetter(1), reverse=True)[:5]

# %% New ipython cell ================

btwnCent_edge_subset = nx.edge_betweenness_centrality_subset(G,
                                    [34, 33, 21, 30, 16, 27, 15, 23, 10],
                                    [1, 4, 13, 11, 6, 12, 17, 7],
                                    normalized=True)
sorted(btwnCent_edge_subset.items(), key=operator.itemgetter(1), reverse=True)[:5]
