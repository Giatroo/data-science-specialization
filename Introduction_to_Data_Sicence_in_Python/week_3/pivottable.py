import pandas as pd
import numpy as np

# %% New ipython cell ================

df = pd.read_csv('datasets/cwurData.csv')
df.head(10)

# %% New ipython cell ================

def create_tier(rank):
    tiers = ['First Tier', 'Second Tier', 'Third Tier', 'Other Tier']
    if rank <= 100:
        return tiers[0]
    if rank <= 200:
        return tiers[1]
    if rank <= 300:
        return tiers[2]
    return tiers[3]


df['Rank_Level'] = df['world_rank'].apply(create_tier)
df[['world_rank', 'Rank_Level']]

# %% New ipython cell ================

df.pivot_table(values='score', index='country', columns='Rank_Level',
               aggfunc=[np.mean]).head()

# %% New ipython cell ================

df.pivot_table(values='score', index='country', columns='Rank_Level',
               aggfunc=[np.mean, np.max]).head()

# %% New ipython cell ================

df.pivot_table(values='score', index='country', columns='Rank_Level',
               aggfunc=[np.mean, np.max], margins=True).head()

# %% New ipython cell ================

new_df = df.pivot_table(values='score', index='country',
                        columns='Rank_Level',
                        aggfunc=[np.mean, np.max], margins=True)
print(new_df.index)
print(new_df.columns)

# %% New ipython cell ================

new_df['mean']['First Tier'].head()

# %% New ipython cell ================

new_df['mean']['First Tier'].idxmax()

# %% New ipython cell ================

new_df.head()

# %% New ipython cell ================

new_df=new_df.stack()
new_df.head()

# %% New ipython cell ================

new_df.unstack().head()

# %% New ipython cell ================

new_df.unstack().unstack().head()
