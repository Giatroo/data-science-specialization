import nltk

# %% New ipython cell ================

# You can remove the packages on /home/giatro/nltk_data/
nltk.download()

# %% New ipython cell ================

from nltk.book import *

# %% New ipython cell ================

text1

# %% New ipython cell ================

sents()

# %% New ipython cell ================

sent1

# %% New ipython cell ================

text7

# %% New ipython cell ================

sent7

# %% New ipython cell ================

len(sent7)

# %% New ipython cell ================

# Total words
len(text7)

# %% New ipython cell ================

# Unique words
len(set(text7))

# %% New ipython cell ================

# First ten words
list(set(text7))[:10]

# %% New ipython cell ================

# Here we have a Frequency Distribution Dictionary:
dist = FreqDist(text7)

# %% New ipython cell ================

len(dist)

# %% New ipython cell ================

vocab1 = dist.keys()
vocab1 # all the words

# %% New ipython cell ================

dist['four']

# %% New ipython cell ================

# Here we can select the most common words with length grater than 5
# This excludes words like 'a', 'for', ',' that will be common in every text
freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 100]
freqwords


# %% New ipython cell ================

for word in freqwords:
    print(f'Word {word} has a frequency of {dist[word]}.')

# %% New ipython cell ================

# Normalization and Stemming:

# Normalizing a word is when a word is when we have multiple forms of a word and
# we just want the 'normalized', the 'standart' form of it.
# For instance, we might have the words:
input1 = 'List listed lists listing listings'
# Can all be normalized to 'list'

words1 = input1.lower().split()
words1

# %% New ipython cell ================

# Stemming means finding this 'standart' or 'root' form of any given word
# There are many ways to do Stemming, Porter is one of them
porter = nltk.PorterStemmer()

# %% New ipython cell ================

[porter.stem(t) for t in words1]
# Now we can count the word list or any derivation of it

# %% New ipython cell ================

# Lemmatization:
# Lemmatization is doing a stemming, but in a any that the normalized words are
# still meaningful.

udhr = nltk.corpus.udhr.words('English-Latin1')

# %% New ipython cell ================

udhr[:20]

# %% New ipython cell ================

[porter.stem(t) for t in udhr[:20]]

# %% New ipython cell ================

WNlemma = nltk.WordNetLemmatizer()
[WNlemma.lemmatize(t) for t in udhr[:20]]

# %% New ipython cell ================

# Tokenization

text11 = "Children shouldn't drink a sugary drink before bed."
text11.split()

# %% New ipython cell ================

nltk.word_tokenize(text11)

# %% New ipython cell ================

# Sentence Splitting

text12 = "This is the first sentence. A gallon of milk in the U.S. costs $2.99.  Is this the third sentence? Yes, it is!"


sentences = nltk.sent_tokenize(text12)

# %% New ipython cell ================

len(sentences)

# %% New ipython cell ================

sentences
