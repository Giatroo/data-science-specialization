import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits = pd.read_table('fruit_data_with_colors.txt')
fruits.head()

# %% New ipython cell ================

fruits.shape

# %% New ipython cell ================

X = fruits[['mass', 'width', 'height', 'color_score']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# train_test_split will *randomly* split the data into two parts:
# * The training set, and;
# * The test set.
# The default behavior is 75% for the train and 25% for the test.
# random_state is the seed for the randomizer.

# The features will be denoted by X and the labels by y.

# %% New ipython cell ================

X_train.shape

# %% New ipython cell ================

y_train.shape

# %% New ipython cell ================

X_test.shape

# %% New ipython cell ================

y_test.shape

# %% New ipython cell ================

X_train

# %% New ipython cell ================

y_train

# %% New ipython cell ================

X_test

# %% New ipython cell ================

y_test

# %% New ipython cell ================

# We can use some visualization techinques to predict weather the
# classifier will be likely or not to recognize some patterns in the data.

from matplotlib import cm
cmap = cm.get_cmap('gnuplot')
scatter = pd.plotting.scatter_matrix(X_train, c=y_train, marker='o',
                                     s=40, hist_kwds={'bins':15},
                                     figsize=(12, 12), cmap=cmap)

# %% New ipython cell ================

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'],
           c=y_train, marker='o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()

# K-Nearest Neighbors Classification:

# %% New ipython cell ================

lookup_fruit_name = dict(zip(fruits.fruit_label.unique(),
                             fruits.fruit_name.unique()))
lookup_fruit_name

# %% New ipython cell ================

# Create the test and train sets:
X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# %% New ipython cell ================

# Create the classifier:
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

# %% New ipython cell ================

# Train the classifier:
knn.fit(X_train, y_train)

# %% New ipython cell ================

# Estimate the accuracy of the classifier:
knn.score(X_test, y_test)

# %% New ipython cell ================

# We can also use to predict a simple value:
fruit_prediction = knn.predict([[20, 4.3, 5.5]])
lookup_fruit_name[fruit_prediction[0]]

# %% New ipython cell ================

fruit_prediction = knn.predict([[100, 6.3, 8.5]])
lookup_fruit_name[fruit_prediction[0]]

# %% New ipython cell ================

k_range = range(1, 20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0, 5, 10, 15, 20])

# %% New ipython cell ================


