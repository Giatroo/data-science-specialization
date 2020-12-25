import numpy as np
import pandas as pd

# %% New ipython cell ================

## Timestamp

pd.Timestamp('9/1/2019 10:05AM')

# %% New ipython cell ================

pd.Timestamp(2019, 12, 20, 0, 0)

# %% New ipython cell ================

pd.Timestamp(2019, 12, 20, 0, 0).isoweekday()

# %% New ipython cell ================

pd.Timestamp(2019, 12, 20, 5, 2, 23).second

# %% New ipython cell ================

## Period

pd.Period('2016-01', 'M')

# %% New ipython cell ================

pd.Period('3/5/2016')

# %% New ipython cell ================

pd.Period('1/2016') + 5

# %% New ipython cell ================

pd.Period('3/5/2016') - 2

# %% New ipython cell ================

## DatetimeIndex and PeriodIndex

t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'),
                             pd.Timestamp('2016-09-02'),
                             pd.Timestamp('2016-09-03')])
t1

# %% New ipython cell ================

type(t1.index)

# %% New ipython cell ================

mount = pd.Period('2016-09')
t2 = pd.Series(list('def'), [mount, mount+1, mount+2])
t2

# %% New ipython cell ================

type(t2.index)

# %% New ipython cell ================

## Converting to Datetime

d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']

ts3 = pd.DataFrame(np.random.randint(10, 100, (4, 2)), index=d1,
                   columns=list('ab'))
ts3

# %% New ipython cell ================

ts3.index = pd.to_datetime(ts3.index)
ts3

# %% New ipython cell ================

pd.to_datetime('4.7.12', dayfirst=True)

# %% New ipython cell ================

## Timedelta

# They're differences in time
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')

# %% New ipython cell ================

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')

# %% New ipython cell ================

## Offset

pd.Timestamp('9/4/2016').weekday()

# %% New ipython cell ================

pd.Timestamp('9/4/2016') + pd.offsets.Week()

# %% New ipython cell ================

pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd()

# %% New ipython cell ================

## Working with Dates in a Dataframe

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
dates

# %% New ipython cell ================

pd.date_range('10-01-2016', periods=9, freq='B')

# %% New ipython cell ================

pd.date_range('04-01-2016', periods=12, freq='QS-JUn')

# %% New ipython cell ================

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                   'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
df

# %% New ipython cell ================

df.index.day_name()

# %% New ipython cell ================

df.diff()

# %% New ipython cell ================

df.resample('M').mean()

# %% New ipython cell ================

df['2017']

# %% New ipython cell ================

df['2016-12']

# %% New ipython cell ================

df['2016-12':]
