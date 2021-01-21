import matplotlib.pyplot as plt
plt.plot?

# %% New ipython cell ================

plt.plot(3,2)

# %% New ipython cell ================

plt.plot(3, 2, 'r.') # red dot

# %% New ipython cell ================

# Using the Artist Layer:
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvasAgg(fig)

ax = fig.add_subplot(111)
ax.plot(3, 2, 'r.')
canvas.print_png('test.png')

# %% New ipython cell ================

plt.figure()
plt.plot(3, 2, 'o')
ax = plt.gca()
ax.axis([0, 6, 0, 10])

# %% New ipython cell ================

plt.figure()
plt.plot(1.5, 1.5, 'o')
plt.plot(2, 2, 'o')
plt.plot(2.5, 2.5, 'o')

# %% New ipython cell ================

ax = plt.gca()
ax.get_children()
