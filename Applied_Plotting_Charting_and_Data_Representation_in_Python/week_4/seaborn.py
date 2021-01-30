import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% New ipython cell ================

np.random.seed(1234)

v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(60, 15, 1000), name='v2')

# %% New ipython cell ================

plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1');
plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label='v2');
plt.legend();

# %% New ipython cell ================

plt.figure()
plt.hist([v1, v2], histtype='barstacked', density=True)
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3);

# %% New ipython cell ================

plt.figure()
sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'});

# %% New ipython cell ================

sns.jointplot(v1, v2, alpha=0.4);

# %% New ipython cell ================

grid = sns.jointplot(v1, v2, alpha=0.4);
grid.ax_joint.set_aspect('equal')

# %% New ipython cell ================

sns.jointplot(v1, v2, kind='hex');

# %% New ipython cell ================

sns.set_style('white');

sns.jointplot(v1, v2, kind='kde', space=0);

# %% New ipython cell ================

iris = pd.read_csv('iris.csv')
sns.pairplot(iris, hue='Name', diag_kws='kde');

# %% New ipython cell ================

plt.figure(figsize=(12, 8))
plt.subplot(1, 2, 1)
sns.swarmplot('Name', 'PetalLength', data=iris);
plt.subplot(1, 2, 2)
sns.violinplot('Name', 'PetalLength', data=iris);
