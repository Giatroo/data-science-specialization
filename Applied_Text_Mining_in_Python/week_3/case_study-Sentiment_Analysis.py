import pandas as pd
import numpy as np

df = pd.read_csv('Amazon_Unlocked_Mobile.csv')
df.head()

# %% New ipython cell ================

df.dropna(inplace=True)
df = df[df['Rating'] != 3]
df['Positively Rated'] = np.where(df['Rating'] > 3, 1, 0)
df.head(10)

# %% New ipython cell ================

df['Positively Rated'].mean()

# %% New ipython cell ================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df['Reviews'],
                                                    df['Positively Rated'],
                                                    random_state=0)

# %% New ipython cell ================

print('X_train first entry:\n\n', X_train[0])
print('\n\nX_train shape:', X_train.shape)

# %% New ipython cell ================

# Let's convert the text into a feature collection that sklearn can use.
# Here, we'll use the bag-of-words approach

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit(X_train)

# %% New ipython cell ================

vect.get_feature_names()[::2000]

# %% New ipython cell ================

# That's the number of features we're working with
len(vect.get_feature_names())

# %% New ipython cell ================

X_train_vectorized = vect.transform(X_train)
X_train_vectorized

# %% New ipython cell ================

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

# %% New ipython cell ================

from sklearn.metrics import roc_auc_score

predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))

# %% New ipython cell ================

feature_names = np.array(vect.get_feature_names())

sorted_coef_index = model.coef_[0].argsort()

print(f'Smallest coefs:\n{feature_names[sorted_coef_index[:10]]}')
print(f'Largest coefs:\n{feature_names[sorted_coef_index[:-11:-1]]}')

# %% New ipython cell ================

## Now let's use a Term Frequency-inverse document frequency (Tfidf) approach

from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(min_df=5).fit(X_train)
len(vect.get_feature_names())

# The min_df parameter allow us to consider a word a feature only if it appears
# in at least min_df documents. It's good to prevent words that might not be
# good predictors.

# %% New ipython cell ================

X_train_vectorized = vect.transform(X_train)

model = LogisticRegression(max_iter=300)
model.fit(X_train_vectorized, y_train)

predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))

# %% New ipython cell ================

feature_names = np.array(vect.get_feature_names())

sorted_tfidf_index = X_train_vectorized.max(0).toarray()[0].argsort()

print(f'Smallest tfidf:\n{feature_names[sorted_tfidf_index[:10]]}')
print(f'Largest tfidf:\n{feature_names[sorted_tfidf_index[:-11:-1]]}')

# %% New ipython cell ================

sorted_coef_index = model.coef_[0].argsort()

print(f'Smallest Coefs:\n{feature_names[sorted_coef_index[:10]]}')
print(f'Largest Coefs:\n{feature_names[sorted_coef_index[:-11:-1]]}')

# %% New ipython cell ================

# But we still have a problem:
print(model.predict(vect.transform(['not an issue, phone is working',
                                    'an issue, phone is not working'])))

# Our current model sees both of these reviews as negative reviews
# because it's not differentiating the order that the words appear

# %% New ipython cell ================

# We can use n-grams to solve that (i.e., features of n consecutive words)
vect = CountVectorizer(min_df=5, ngram_range=(1,2)).fit(X_train)
X_train_vectorized = vect.transform(X_train)

len(vect.get_feature_names())

# %% New ipython cell ================

# Keep in mind that, ngrams can cause the number of features to explode
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))

# %% New ipython cell ================

feature_names = np.array(vect.get_feature_names())

sorted_coef_index = model.coef_[0].argsort()

print(f'Smallest Coefs:\n{feature_names[sorted_coef_index[:10]]}')
print(f'Largest Coefs:\n{feature_names[sorted_coef_index[:-11:-1]]}')
