import networkx as nx
import numpy as np
import pandas as pd

# %% New ipython cell ================

G1 = nx.Graph()
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (0, 5),
                   (1, 3),
                   (1, 6),
                   (3, 4),
                   (4, 5),
                   (4, 7),
                   (5, 8),
                   (8, 9)])

nx.draw_networkx(G1)

# %% New ipython cell ================

# Let's now load a graph in the Adjecency List format:
!cat G_adjlist.txt

# %% New ipython cell ================

G2 = nx.read_adjlist('G_adjlist.txt', nodetype=int)
G2.edges()

# %% New ipython cell ================

# Obs.: draw_networkx works randomly, so it will not draw the same graph even if
# it has the same edges and verticies
nx.draw_networkx(G2)

# %% New ipython cell ================

# Adjecency Matrix format:
G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
G_mat

# %% New ipython cell ================

# To convert it into a graph, we just pass it into the Graph constructor
G3 = nx.Graph(G_mat)
G3.edges()

# %% New ipython cell ================

# Edgelist format (here, we added a weight column):
!cat G_edgelist.txt

# %% New ipython cell ================

G4 = nx.read_edgelist('G_edgelist.txt', data=[('Weight', int)])
G4.edges(data=True)

# %% New ipython cell ================

# We can also import graphs from Pandas:
G_df = pd.read_csv('G_edgelist.txt', delim_whitespace=True,
                   header=None, names=['n1', 'n2', 'weight'])
G_df

# %% New ipython cell ================

from networkx.convert_matrix import from_pandas_edgelist

G5 = from_pandas_edgelist(G_df, 'n1', 'n2', edge_attr='weight')
G5.edges(data=True)

# %% New ipython cell ================

# Let's now show a more complex example:
!head -5 chess_graph.txt

# %% New ipython cell ================

chess = nx.read_edgelist('chess_graph.txt',
                         data=[('outcome', int), ('timestamp', float)],
                         create_using=nx.MultiDiGraph())

# %% New ipython cell ================

chess.is_directed(), chess.is_multigraph()

# %% New ipython cell ================

chess.edges(data=True)

# %% New ipython cell ================

games_played = chess.degree()
games_played

# %% New ipython cell ================

max_value = max(dict(games_played).values())
max_key, = [i for i in dict(games_played).keys() if games_played[i] == max_value]

print(f'player {max_key} played {max_value} games.')

# %% New ipython cell ================

df = pd.DataFrame(chess.edges(data=True), columns=['white', 'black', 'outcome'])
df.head()

# %% New ipython cell ================


df['outcome'] = df['outcome'].map(lambda x : x['outcome'])
df.head()

# %% New ipython cell ================

won_as_white = df[df['outcome']==1].groupby('white').sum()
won_as_black = -df[df['outcome']==-1].groupby('black').sum()
win_count = won_as_white.add(won_as_black, fill_value=0)
win_count.head()

# %% New ipython cell ================

win_count.nlargest(5, 'outcome')
