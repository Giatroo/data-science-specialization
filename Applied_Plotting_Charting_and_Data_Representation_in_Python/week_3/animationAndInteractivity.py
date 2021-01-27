import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# %% New ipython cell ================

n = 100
x = np.random.randn(n)

def update(curr):
    if curr == n:
        a.event_source.stop()
    plt.cla()
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x[:curr], bins=bins)
    plt.axis([-4, 4, 0, 30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate(f'n = {curr}', [3, 27])

fig = plt.figure()
a = animation.FuncAnimation(fig, update, interval=100)

# %% New ipython cell ================

plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title(f'''Event at pixels {event.x}, {event.y}\nand data
                        {event.xdata}, {event.ydata}''')

plt.gcf().canvas.mpl_connect('button_press_event', onclick)

# %% New ipython cell ================

from random import shuffle
import pandas as pd

origins = ['China', 'Brazil', 'India', 'USA', 'Canada', 'UK', 'Germany',
           'Iraq', 'Chile', 'Mexico']

shuffle(origins)

df = pd.DataFrame({'height': np.random.rand(10),
                   'weight': np.random.rand(10),
                   'origin': origins})
df

# %% New ipython cell ================

plt.figure()
plt.scatter(df['height'], df['weight'], picker=5)
plt.gca().set_ylabel('Weight')
plt.gca().set_xlabel('Height')

# %% New ipython cell ================

def onpick(event):
    origin = df.iloc[event.ind[0]]['origin']
    plt.gca().set_title(f'Selected item came from {origin}')
plt.gcf().canvas.mpl_connect('pick_event', onpick)
