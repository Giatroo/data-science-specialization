import matplotlib.pyplot as plt
import numpy as np

# %% New ipython cell ================

x = np.array(range(1, 9))
y = x

plt.figure()
plt.scatter(x, y)

# %% New ipython cell ================

x = np.array(range(1, 9))
y = x
colors = ['green']*(len(x)-1)
colors.append('red')

plt.figure()
plt.scatter(x, y, s=100, c=colors)

# %% New ipython cell ================

x = range(1, 6)
y = range(6, 11)
plt.figure()
plt.scatter(x[:2], y[:2], s=100, c='r', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='b', label='Short students')

# %% New ipython cell ================

plt.xlabel('the number of times the child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

# %% New ipython cell ================

plt.legend()

# %% New ipython cell ================

plt.legend(loc=4, frameon=False, title='Legend')

# %% New ipython cell ================

plt.gca().get_children()

# %% New ipython cell ================

from matplotlib.artist import Artist

def rec_gc(art, depth=0):
    if isinstance(art, Artist):
        print("  " * depth + str(art))
        for child in art.get_children():
            rec_gc(child, depth+2)
rec_gc(plt.gca().get_children()[-2])
