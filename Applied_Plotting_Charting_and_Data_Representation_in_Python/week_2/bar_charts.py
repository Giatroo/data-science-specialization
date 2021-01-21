import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% New ipython cell ================

linear_data = np.arange(1, 9)
quadratic_data = linear_data ** 2

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

# %% New ipython cell ================

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, quadratic_data, width=0.3, color='r')

# %% New ipython cell ================

from random import randint

linear_err = [randint(0,6) for x in range(len(linear_data))]
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)

# %% New ipython cell ================

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, quadratic_data, width = 0.3, bottom=linear_data, color='r')

# %% New ipython cell ================

plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(xvals, quadratic_data, height = 0.3, left=linear_data, color='r')
