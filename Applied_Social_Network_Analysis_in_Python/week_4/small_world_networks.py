import networkx as nx

# %% New ipython cell ================

# In real world networks, we usually see networks that have a very small average
# path length between each node and also lots of triangles (a very high average
# clustering coefficient).

# There's a model that can generate networks like these and it's called the
# Small World Model.

# * This model starts with a ring of n nodes, where each node is connected to
# its k nearest neighbors.
# * Then we fix a parameter p between 0 and 1 (included).
# * Now we consider each edge (u, v). With probability p, we select a node w at
# random and rewire the edge (u, v) so it becomes (u, w)
# * Done

# %% New ipython cell ================

# The ideia is that when we start with each node linked to its k nearest
# neighbors, we have a bunch of triangles and thus a large average clustering
# coefficient. But, as each node is only connected to its k nearest neighbors,
# to go from one side of the network to the other, we have to travel a very long
# distance. That's why we rewire some edges with some probability p.

# If p is very large (like p=1), our network will be completely random.
# Therefore, the average distance between nodes will be very low, but we'll
# break our original structure with lots of triangles.

# Therefore, there's a sweet spot for the p value between not changing the
# original graph at all (p=0) and making it random (p=1).

# When we plot the changes in the avg clustering coefficient and avg shortest
# path length, we see that the avg. shortest path length decreses very rapidly
# (with just p=0.01 it's already very small because just few bridges are able to
# make the distances very low) and we see that the avg. clustering coefficient
# also drops, but very slower.

# For instance, a network of 1000 nodes with k=6 and p=0.04 has:
# * 8.99 avg. shortest path length;
# * 0.53 avg. clustering coefficient.

# %% New ipython cell ================

# In networkx, we can use the function watts_strogatz_graph(n, k, p), which
# returns a small world network with n nodes, starting with a ring lattice with
# each node connected to its k nearest neighbors, and rewiring probability p.

G = nx.watts_strogatz_graph(50, 5, 0.04)
nx.draw_networkx(G)

# %% New ipython cell ================

G = nx.watts_strogatz_graph(1000, 6, 0.04)
degrees = dict(G.degree())
degree_values = sorted(set(degrees.values()))
n_nodes = float(nx.number_of_nodes(G))
histogram = [list(degrees.values()).count(i) / n_nodes for i in degree_values]

import matplotlib.pyplot as plt
plt.bar(degree_values, histogram)
plt.xlabel('Degree'); plt.ylabel('Fraction of Nodes')
plt.show()

# %% New ipython cell ================

# As we can see here, this model gets the properties we wanted, but it doesn't
# have the power law degree distribution that many reals networks have.

# We can also have some problems with a small world model:

# %% New ipython cell ================

# Sometimes, we can end up with a disconnected network, and that's something we
# don't want.
# We can prevent it using:
# nx.connected_watts_strogatz_graph(n, k, p, t)
# It runs watts_strogatz_graph(n, k, p) up to t times, until it returns a
# connected small world network. If it runs more than t times, it returns an
# error.

# There's also the newman_watts_strogatz_graph(n, k, p), which runs a model
# similar to the small world model, but rather than rewiring edges, new edges
# are added with probability p.
