import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'B'),
                  ('A', 'G'),
                  ('A', 'H'),
                  ('B', 'C'),
                  ('C', 'D'),
                  ('C', 'E'),
                  ('D', 'F'),
                  ('F', 'G'),
                  ('F', 'I'),
                  ('G', 'H'),
                  ('G', 'I')])

# %% New ipython cell ================

## Degree Distributions

# The degree of a node in an undirected graph is the number of neighbors it has.

# The *degree distribution* of a graph is the probability distribution of the
# degrees over the entire network.

# So if a network has:
# * 1 node with degree 1;
# * 4 node with degree 2;
# * 3 node with degree 3; and
# * 1 node with degree 4.

# The degree distribution is:
# P(1) = 1/9
# P(2) = 4/9
# P(3) = 1/3
# P(4) = 1/9

# We can plot the degree distribution of a network:
degrees = G.degree()
degrees

# %% New ipython cell ================

degree_values = sorted(set(dict(degrees).values()))
n_nodes = float(nx.number_of_nodes(G))
histogram = [list(dict(degrees).values()).count(i) / n_nodes for i in degree_values]

import matplotlib.pyplot as plt
plt.bar(degree_values, histogram)
plt.xlabel('Degree'); plt.ylabel('Fraction of Nodes')
plt.show()

# %% New ipython cell ================

# We can define the in-degree or out-degree distributions in the same way for
# directed graphs and use the functions G.in_degree() or G.out_degree().

# %% New ipython cell ================

# Power Law Degree Distribution

# In many graphs, we have many, many nodes with low degree and few nodes with a
# high degree. We call this the power law degree distribution.
# This kind of degree distribution have the formula P(k) = Ck^-a, where C is a
# constant and a is a positive constant.

# Prefectural Attachment Model

# We can use a model to generate a graph with the power law degree distribution
# property.

# To do so, we start with just two nodes connected by an edge.
# Than at each time we're going to add a new node, the this new node must be
# connected to a single old node.
# To choose the node in which the new node will be connected to, we use the
# current nodes's degree as a probability of picking that node.
# So the probability that our new node v will connect to an old node u of degree
# d_u is d_u divided by the sum of all nodes.

# This model approaches the power law P(k) = Ck^-3 with constant C.

# %% New ipython cell ================

# In networkx, the function barabasi_albert_graph(n, m) returns a network with n
# nodes. Each new node attaches to m existing nodes according to the
# Preferential Attachment model.

G = nx.barabasi_albert_graph(30, 1)
nx.draw_networkx(G)

# %% New ipython cell ================

G = nx.barabasi_albert_graph(100000, 1)
degrees = dict(G.degree())
degree_values = sorted(set(degrees.values()))
n_nodes = float(nx.number_of_nodes(G))
histogram = [list(degrees.values()).count(i) / n_nodes for i in degree_values]

plt.plot(degree_values, histogram, 'o')
plt.xlabel('Degree'); plt.ylabel('Fraction of Nodes')
plt.xscale('log'); plt.yscale('log')
plt.show()
