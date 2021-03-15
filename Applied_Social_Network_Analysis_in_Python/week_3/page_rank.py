import networkx as nx

# %% New ipython cell ================

# Basic Page Ranking:

# In page ranking, important nodes are the ones that are referenced by other
# important nodes.

# Suppose we have n nodes and we will do k steps.

# In the beginning, all nodes will have a PageRank of 1/n
# Then we perform the *Basic PageRank Update Rule* k times.

# The Basic PageRank Update Rule is: each node gives an equal share of its
# current PageRank to all the nodes it links to.
# Then, the PageRank of each node is the sum of all the PageRank it received
# from other nodes.

# %% New ipython cell ================

# The PageRank of a node at step k is the probability that a *random walker*
# lands on the node after taking k steps.

# That means that if we have a cycle in our network that doesn't points to nodes
# outside the cycle, this cycle will have a very high PageRank and all the other
# nodes will have a page rank that will approach zero.

# To fix this problem, we introduce a 'damping parameter' called alpha.

# Now, the random walker have to make a coin flip of probability alpha before
# going to a new edge. It means that it will pick a new edge only with
# probability alpha and with probability 1-alpha it will pick a completely new
# node and restart its random walk from there. It means that now it will not get
# stuck in a cycle, because after some steps, we might pick a new node outside
# the cycle and do another random walk.

# This new algorithm is called the Scaled PageRank.
# And now the interpretation is that the Scaled PageRank of k steps and damping
# factor alpha of a node n is the probability that a random walker with damping
# factor alpha lands on a node n after k steps.

# And again, for most networks these values will convert of a particular value
# for each node.

# In practice we tend to choose values around 0.8 or 0.9 for alpha.

# %% New ipython cell ================

# In networkx we can use the function pagerank(G, alpha=0.8)
