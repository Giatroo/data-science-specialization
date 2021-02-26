import nltk
from nltk.book import *

# %% New ipython cell ================

# Part-of-speech (POS) Tagging
# It's diving the words into categories:
# nouns, verbs, adjectives, conjunctions, ...

nltk.help.upenn_tagset('MD')

# %% New ipython cell ================

text11 = "Children shouldn't drink a sugary drink before bed."

# %% New ipython cell ================

text13 = nltk.word_tokenize(text11)

# %% New ipython cell ================

nltk.pos_tag(text13)

# %% New ipython cell ================

# Ambiguity in POS Tagging

text = 'Visiting aunts can be a nuisance'
# In this case, 'visiting' can be a verb or an adjective

text14 = nltk.word_tokenize(text)
nltk.pos_tag(text14)
# Here, it's classified as a verb
# In fact, we can't have both versions. POS Tagging will always give us the
# version that appers more in the texts

# %% New ipython cell ================

# Parsing Sentence Structure

text15 = nltk.word_tokenize("Alice loves Bob')

# %% New ipython cell ================

grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

parser = nltk.ChartParser(grammar)

# %% New ipython cell ================

trees = parser.parse_all(text15)

# %% New ipython cell ================

for tree in trees:
    print(tree)

# %% New ipython cell ================

tokens = nltk.word_tokenize(text)
nltk.pos_tag(tokens)

# %% New ipython cell ================


