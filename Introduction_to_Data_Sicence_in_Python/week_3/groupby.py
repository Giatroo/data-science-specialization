import pandas as pd
import numpy as np

# %% New ipython cell ================

df = pd.read_csv('datasets/census.csv')
df.head()

# %% New ipython cell ================

%%timeit -n 3

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    #print(f'Conties in state {state} have an average pop of {str(avg)}')

# %% New ipython cell ================

%%timeit -n 3

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    #print(f'Conties in state {state} have an average pop of {str(avg)}')

# %% New ipython cell ================

df = df.set_index('STNAME')


def set_batch_number(item):
    if item[0] < 'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2


for group, frame in df.groupby(set_batch_number):
    print(
        f'There are {str(len(frame))} records in group {str(group)} for processing.')

# %% New ipython cell ================

df = pd.read_csv('datasets/listings.csv')
df.head()

# %% New ipython cell ================

df = df.set_index(['cancellation_policy', 'review_scores_value'])

for group, frame in df.groupby(level=(0, 1)):
    print(group)

# %% New ipython cell ================


def grouping_fun(item):
    if item[1] == 10.0:
        return (item[0], "10.0")
    return (item[0], "not 10.0")


for group, frame in df.groupby(by=grouping_fun):
    print(group)

# %% New ipython cell ================

df = df.reset_index()

df.groupby('cancellation_policy').agg({'review_scores_value': np.average})

# %% New ipython cell ================

df.groupby('cancellation_policy').agg({'review_scores_value': np.nanmean})

# %% New ipython cell ================

df.groupby('cancellation_policy').agg({'review_scores_value': (np.nanmean,
                                                               np.nanstd),
                                       'reviews_per_month' : np.nanmean})

# %% New ipython cell ================

cols=['cancellation_policy', 'review_scores_value']

transform_df = df[cols].groupby('cancellation_policy').transform(np.nanmean)
transform_df.head()

# %% New ipython cell ================

transform_df.rename({'review_scores_value' : 'mean_review_scores'},
                    axis='columns', inplace=True)
df = df.merge(transform_df, left_index=True, right_index=True)
df.head()

# %% New ipython cell ================

df['mean_diff'] = np.absolute(df['review_scores_value']-df['mean_review_scores'])
df['mean_diff'].head()

# %% New ipython cell ================

df.groupby('cancellation_policy').filter(lambda x:
                                         np.nanmean(x['review_scores_value'])>9.2)

# %% New ipython cell ================

df = pd.read_csv('datasets/listings.csv')
df = df[['cancellation_policy', 'review_scores_value']]
df.head()

# %% New ipython cell ================

def calc_mean_review_scores(group):
    avg=np.nanmean(group['review_scores_value'])
    group['review_scores_value'] = np.abs(avg-group['review_scores_value'])
    return group

df.groupby('cancellation_policy').apply(calc_mean_review_scores).head()

# %% New ipython cell ================


