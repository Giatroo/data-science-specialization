import matplotlib.pyplot as plt
import numpy as np

# %% New ipython cell ================

plt.figure()

Y = np.random.normal(size=10000)
X = np.random.random(size=10000)
_ = plt.hist2d(X, Y, bins=25)

# %% New ipython cell ================

plt.figure()
_ = plt.hist2d(X, Y, bins=100)

# %% New ipython cell ================

plt.colorbar()

# %% New ipython cell ================

plt.figure()

Y = np.random.normal(size=10000000)
X = np.random.normal(loc=2, scale=5, size=10000000)
_ = plt.hist2d(X, Y, bins=100)
