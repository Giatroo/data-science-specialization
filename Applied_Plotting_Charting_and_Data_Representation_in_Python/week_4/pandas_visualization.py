import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% New ipython cell ================

plt.style.available

# %% New ipython cell ================

plt.style.use('seaborn-colorblind')

# %% New ipython cell ================

np.random.seed(123)

df = pd.DataFrame({'A' : np.random.randn(365).cumsum(),
                   'B' : np.random.randn(365).cumsum() + 20,
                   'C' : np.random.randn(365).cumsum() - 20},
                  index = pd.date_range('1/1/2017', periods=365))
df.head()

# %% New ipython cell ================

df.plot();

# %% New ipython cell ================

df.plot('A', 'B', kind='scatter');

# %% New ipython cell ================

df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis');

# %% New ipython cell ================

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis');
ax.set_aspect('equal')

# %% New ipython cell ================

df.plot.box();

# %% New ipython cell ================

df.plot.hist();

# %% New ipython cell ================

df.plot.kde();

# %% New ipython cell ================

iris = pd.read_csv('iris.csv')
iris.head()

# %% New ipython cell ================

pd.plotting.scatter_matrix(iris);

# %% New ipython cell ================

plt.figure()
pd.plotting.parallel_coordinates(iris, 'Name');
