import matplotlib.pyplot as plt
import numpy as np

# %% New ipython cell ================

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1, ax2, ax3, ax4]

for n in range(0, len(axs)):
    sample_size = 10 ** (n+1)
    sample = np.random.normal(size=sample_size)
    axs[n].hist(sample)
    axs[n].set_title(f'n={sample_size}')

# %% New ipython cell ================

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1, ax2, ax3, ax4]

for n in range(0, len(axs)):
    sample_size = 10 ** (n+1)
    sample = np.random.normal(size=sample_size)
    axs[n].hist(sample, bins=100)
    axs[n].set_title(f'n={sample_size}')

# %% New ipython cell ================

plt.figure()
Y = np.random.normal(size=10000)
X = np.random.random(size=10000)
plt.scatter(X, Y)

# %% New ipython cell ================

import matplotlib.gridspec as gridspec

plt.figure()
gspec = gridspec.GridSpec(3, 3)

top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

# %% New ipython cell ================

lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
s = side_histogram.hist(Y, bins=100, orientation='horizontal')

# %% New ipython cell ================

top_histogram.clear()
top_histogram.hist(X, bins=100, density=True)
side_histogram.clear()
side_histogram.hist(Y, bins=100, orientation='horizontal', density=True)
side_histogram.invert_xaxis()

# %% New ipython cell ================

for ax in [top_histogram, lower_right]:
    ax.set_xlim(0, 1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5, 5)
