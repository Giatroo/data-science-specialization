import pandas as pd
import numpy as np
import timeit

df = pd.read_csv('datasets/census.csv')
df.head()

# %% New ipython cell ================

(df.where(df['SUMLEV']==50)
 .dropna()
 .set_index(['STNAME', 'CTYNAME'])
 .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

# %% New ipython cell ================

df = df[df['SUMLEV']==50]
df.set_index(['STNAME', 'CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
