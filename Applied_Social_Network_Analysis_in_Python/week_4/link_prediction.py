import networkx as nx

G = nx.Graph()
G.add_edges_from([
    ('A', 'B'),
    ('A', 'D'),
    ('A', 'E'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('C', 'F'),
    ('E', 'F'),
    ('F', 'G'),
    ('G', 'H'),
    ('G', 'I')
])

# %% New ipython cell ================

# Today we're going to discuss a very important problem:
# * Given a network, predict how it will look like in the future (predict the
# new links it'll have).

# This problem is very important. For instance, in friends recommendation.

# %% New ipython cell ================

# To solve this problem, we're going to look at some measures.

# The first one is *common neighbors*.
# We define it as comm_neigh(X, Y) = | N(X) inter N(Y) |
# where N(X) is the set of neighbors of node X.

# %% New ipython cell ================

# In networkx, we can find the common neighbors as:
common_neigh = [(e[0], e[1], len(list(nx.common_neighbors(G, e[0], e[1]))))
                for e in nx.non_edges(G)]

sorted(common_neigh, key=lambda x : x[2], reverse=True)

# %% New ipython cell ================

# Another measure is the jaccard coefficient.
# It looks at the number of common neighbors, but it normalizes it by the total
# number of neighbors:
# jacc_coeff(X, Y) = |N(X) inter N(Y)| / |N(X) U N(Y)|

# In networkx, we can use the method:
L = list(nx.jaccard_coefficient(G)) # this returns an iterator
L.sort(key=lambda x : x[2], reverse=True)
L

# %% New ipython cell ================

# The third measure is called the Resource Allocation Index.

# The intuition behind it is that it considers a resource (like a information)
# that a node can send to another node through their common neighbors.

# For formula is:
# res_alloc(X, Y) = sum (1/d_u),
# where u is a common neighbor of X and Y (and d_u is the degree of u).

# In networkx, we can use the method:
L = list(nx.resource_allocation_index(G)) # again an iterator
L.sort(key=lambda x : x[2], reverse=True)
L

# %% New ipython cell ================

# The fourth measure is called the Adamic-Adar Index.

# This is very close to the Resource Allocation Index, but instead of diving by
# the degree, we divide by the log of the degree:
# adamic_adar(X, Y) = sum (1/log(d_u)),

L = list(nx.adamic_adar_index(G)) # again an iterator
L.sort(key=lambda x : x[2], reverse=True)
L

# %% New ipython cell ================

# Measure number five is called the Prefectural Attachment Score

# As we recall from the Prefectural Attachment Model, nodes with higher degree
# have higher probability of having even more nodes connected to it.
# So if we're looking at two nodes that have a high degree, they are likely to
# be connected.

# It's just the product of the degrees of the two nodes:
# pref_attach(X, Y) = d_X * d_Y

L = list(nx.preferential_attachment(G))
L.sort(key=lambda x : x[2], reverse=True)
L

# %% New ipython cell ================

# Now we're going to look at measures that take into account the *community
# structure* of our network.
# Basic, we say that a node belongs to a community and nodes tend to form more
# connections with the its own community than with other communities.

# %% New ipython cell ================

# The sixth measure is the Community Common Neighbors

# This measure consider the number of common neighbors, but with a bonus for
# neighbors in same community

# It's also called the Common Neighbor Soundarajan-Hopcroft score:

# cn_soundrajan_hopcroft(X, Y) = |N(X) inter N(Y)| + sum(f(u)),
# for u common neighbor of X and Y.

# f is defined as:
# * f(u) is 1 with u is un the same community as X and Y
# * f(u) is 0 otherwise

# In networkx, we first need to tell which nodes belong to each community:
G.nodes['A']['community'] = 0
G.nodes['B']['community'] = 0
G.nodes['C']['community'] = 0
G.nodes['D']['community'] = 0
G.nodes['E']['community'] = 1
G.nodes['F']['community'] = 1
G.nodes['G']['community'] = 1
G.nodes['H']['community'] = 1
G.nodes['I']['community'] = 1

# And now we use:
L = list(nx.cn_soundarajan_hopcroft(G))
L.sort(key=lambda x : x[2], reverse=True)
L

# %% New ipython cell ================

# The last measure is called Community Resource Allocation Index

# It's similar to the Resource Allocation Index, but only considering nodes in
# the same community

# ra_soundarajan_hopcroft(X, Y) = sum(f(u)/d_u),
# where u is a common neighbor of X and Y
# and f is the same as before

L = list(nx.ra_index_soundarajan_hopcroft(G))
L.sort(key=lambda x : x[2], reverse=True)
L

# %% New ipython cell ================

# Finally, we need to use these measures to solve our problem.
# Typically, what we tend to do is use these measures as features for a
# classifier and train it to make prediction of whether or not the nodes will
# link together in the future.
