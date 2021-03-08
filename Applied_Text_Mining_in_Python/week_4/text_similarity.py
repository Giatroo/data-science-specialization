import nltk
from nltk.corpus import wordnet as wn

# %% New ipython cell ================

deer = wn.synset('deer.n.01')
elk = wn.synset('elk.n.01')
horse = wn.synset('horse.n.01')

# %% New ipython cell ================

# Path similarity:
print(deer.path_similarity(elk))
print(deer.path_similarity(horse))

# %% New ipython cell ================

# Lin similarity:
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')

print(deer.lin_similarity(elk, brown_ic))
print(deer.lin_similarity(horse, brown_ic))

# %% New ipython cell ================

# Collocations and Association:
from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()

finder = BigramCollocationFinder.from_words(text)
finder.nbest(bigram_measures.pmi, 10)
