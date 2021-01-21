import matplotlib.pyplot as plt
import numpy as np

# %% New ipython cell ================

linear_data = np.arange(1, 9)
quadratic_data = linear_data ** 2

plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')

# %% New ipython cell ================

plt.plot([22, 44, 55], '--r')

# %% New ipython cell ================

plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Base line', 'Competition', 'Us'])

# %% New ipython cell ================

plt.gca().fill_between(range(len(linear_data)),
                       linear_data, quadratic_data, facecolor='b',
                       alpha=.25)

# %% New ipython cell ================

plt.figure()

observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')

plt.plot(observation_dates, linear_data, '-o',
         observation_dates, quadratic_data, '-o')

# %% New ipython cell ================

import pandas as pd

plt.figure()

observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates))

plt.plot(observation_dates, linear_data, '-o',
         observation_dates, quadratic_data, '-o')

# %% New ipython cell ================

x = plt.gca().xaxis

for item in x.get_ticklabels():
    item.set_rotation(45)

# %% New ipython cell ================

plt.subplots_adjust(bottom=0.25)

# %% New ipython cell ================

ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Quadratic vs. Linear performance')

# %% New ipython cell ================

ax.set_title("Quadratic ($x^2$) vs. Linear ($x$) performance")
