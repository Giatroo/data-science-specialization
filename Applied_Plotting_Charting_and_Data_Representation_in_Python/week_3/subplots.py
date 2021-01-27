import matplotlib.pyplot as plt
import numpy as np

# %% New ipython cell ================

plt.figure()
plt.subplot(1, 2, 1)

linear_data = np.arange(1, 9)

plt.plot(linear_data, '-o')

# %% New ipython cell ================

exponential_data = linear_data ** 2

plt.subplot(1, 2, 2)
plt.plot(exponential_data, '-o')

# %% New ipython cell ================

plt.subplot(1, 2, 1)
plt.plot(exponential_data, '-o')

# %% New ipython cell ================

plt.figure()
ax1 = plt.subplot(1, 2, 1)
plt.plot(linear_data, '-o')
ax2 = plt.subplot(1, 2, 2, sharey=ax1)
plt.plot(exponential_data, '-x')

# %% New ipython cell ================

plt.figure()
plt.subplot(1, 2, 1) == plt.subplot(121) # True

# Notice that the index is 1-index

# %% New ipython cell ================

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3,
                                                               sharex=True,
                                                               sharey=True)

ax5.plot(linear_data, '--X')

# %% New ipython cell ================

for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)

plt.gcf().canvas.draw()
