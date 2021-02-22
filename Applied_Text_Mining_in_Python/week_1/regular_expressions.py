text10 = '"Ethics are built right into the ideals and objectives of the United Nations" #UNSG @ NY Society for Ethical Culture bit.ly/2guVelr @UN @UN_Women'

# %% New ipython cell ================

text11 = text10.split(' ')
text11

# %% New ipython cell ================

[word for word in text11 if word.startswith('@') or word.startswith('#')]

# %% New ipython cell ================

# Doing so we get a single '@'. That's not what we want, we need something
# before @.

[w for w in text11 if w.startswith('@')]

# %% New ipython cell ================

import re
[w for w in text11 if re.search('@[A-Za-z0-9_]+', w)]

# Using Regex we can achieve what we want

# %% New ipython cell ================

# . : wildcard
# ^ : start of a string
# $ : end of a string
# [] : set
# [a-z] : lower case characters
# [^abc] : anything that is not a, b or c
# a|b : a or b
# () : Scoping for operators
# \ : espace character

# \b : word boundary
# \d : any digit
# \D : any non-digit
# \s : any whitespace
# \S : any non-whitespace
# \w : any alphanumeric
# \W : any non-alphanumeric

# * : zero or more
# + : one or more
# ? : zero or one
# {n} : n times
# {n,} : at least n times
# {,n} : at most n times
# {m,n} : at least m and at most n times

# %% New ipython cell ================

[w for w in text11 if re.search('@\w+', w)]

# %% New ipython cell ================

text12 = 'ouagadougou'
re.findall(r'[aeiou]', text12)

# %% New ipython cell ================

re.findall(r'[^aeiou]', text12)

# %% New ipython cell ================

# Regular expressions for Dates:

# 23rd October 2002 could be written as:
# 23-10-2002
# 23/10/2002
# 23/10/02
# 10/23/2002
# 23 Oct 2002
# 23 October 2002
# Oct 23, 2002
# October 23, 2002

# We can use the regex:
regex_date = r'\d{2}[/-]\d{2}[/-]\d{4}'
dateStr = '23-10-2002\n23/10/2002\n23/10/02\n10/23/2002\n23 Oct 2002\n 23 October 2002\nOct 23, 2002\nOctober 23, 2002\n'

re.findall(regex_date, dateStr)

# %% New ipython cell ================

regex_date = r'\d{2}[/-]\d{2}[/-]\d{2,4}'
re.findall(regex_date, dateStr)

# %% New ipython cell ================

regex_date = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
re.findall(regex_date, dateStr)

# %% New ipython cell ================

regex_date2 = r'\d{2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}'
re.findall(regex_date2, dateStr)

# %% New ipython cell ================

regex_date2 = r'\d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}'
re.findall(regex_date2, dateStr)

# %% New ipython cell ================

regex_date2 = r'\d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}'
re.findall(regex_date2, dateStr)

# %% New ipython cell ================

regex_date2 = r'(?:\d{2})?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{2}, )?\d{4}'
re.findall(regex_date2, dateStr)
