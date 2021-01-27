import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

random_sample = np.random.random(size=100000)
normal_sample = np.random.normal(size=100000)
gamma_sample = np.random.gamma(2, size=100000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})

# %% New ipython cell ================

df.describe()

# %% New ipython cell ================

plt.figure()
_ = plt.boxplot(df['normal'], whis='range')
plt.grid(False)

# %% New ipython cell ================

plt.clf()
_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
plt.grid(False)

# %% New ipython cell ================

plt.figure()
_ = plt.hist(df['gamma'], bins=100)

# %% New ipython cell ================

import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)

# %% New ipython cell ================

ax2.yaxis.tick_right()

# %% New ipython cell ================

plt.figure()
plt.boxplot([df['normal'], df['random'], df['gamma']])
