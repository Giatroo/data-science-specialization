import networkx as nx

# %% New ipython cell ================

# Now we have another algorithm used in web pages search.

# First, given a query to a search engine, we need to find potential root nodes
# that are very relevant web pages (potential *authorities*)
# Then, we need to find all the pages that link to a page in the root set
# (potential *hubs*).
# The *base set* is all the roots and nodes that point to them.
# And we consider all the edges from nodes in the base set that point to other
# nodes in the base set.

# So the difference between PageRank and hubs and authorities is that we're
# getting a subset of the whole network

# %% New ipython cell ================

# Them we run the HITS Algorithm on our network.

# It works again with k iterations and we keep track of the authority and hub
# score of each node.

# First, we assign each node an authority and hub score of 1.

# Then, we apply the Authority Update Rule: each node's authority score is the
# sum of hub scores of each node that point to it.
# And apply the Hub Update Rule: each node's hub score is the sum of authority
# scores of each node that it points to.
# And at the end of each iteration, we normalize both scores by dividing but the
# sum of that respective score.

# Again, those scores will converge in most graphs.

# %% New ipython cell ================

# To calculate those values, we use the networkx function
# hits(G)
# and it outputs two dictionaries
