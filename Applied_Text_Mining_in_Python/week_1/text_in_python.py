text1 = "Ethics are built right into the idealas and objectives of the United Nations "

# %% New ipython cell ================

len(text1)

# %% New ipython cell ================

text2 = text1.split(' ')

# %% New ipython cell ================

len(text2)

# %% New ipython cell ================

text2

# %% New ipython cell ================

[w for w in text2 if len(w) > 3]

# %% New ipython cell ================

[w for w in text2 if w.istitle()]

# %% New ipython cell ================

[w for w in text2 if w.endswith('s')]

# %% New ipython cell ================

text3 = 'To be or not to be'
text4 = text3.split(' ')
len(text4)

# %% New ipython cell ================

len(set(text4))

# %% New ipython cell ================

set(text4)

# %% New ipython cell ================

len(set([w.lower() for w in text4]))

# %% New ipython cell ================

set([w.lower() for w in text4])

# %% New ipython cell ================

# s.startswith(t) ; s.endswith(t)

# t in s

# s.isupper(); s.islower(); s.istitle()

# s.isalpha(); s.isdidigt(); s.isalnum()

# %% New ipython cell ================

# s.lower(); s.upper(); s.titlecase()

# s.split(t)

# s.splitlines()

# s.join(t)

# s.strip(); s.rstrip(); s.lstrip()

# s.find(t); s.rfind(t)

# s.replace(u, v)

# %% New ipython cell ================

## Splitting and joining:

text5 = 'ouagadougou'
text6 = text5.split('ou')
text6

# %% New ipython cell ================

'ou'.join(text6)

# %% New ipython cell ================

## Getting a list of chars from the string:

text5.split('')

# %% New ipython cell ================

list(text5)

# %% New ipython cell ================

[c for c in text5]

# %% New ipython cell ================

## Text cleaning:
text8   = '   A quick brown fox jumped over the lazy dog. '
text8.split(' ') # See how messy it's to split this text

# %% New ipython cell ================

text9 = text8.strip()
text9.split(' ')

# %% New ipython cell ================

## Changing text:

text9

# %% New ipython cell ================

text9.find('o')

# %% New ipython cell ================

text9.rfind('o')

# %% New ipython cell ================

text9.replace('o', 'O')

# %% New ipython cell ================

text9 # as you see, that doesn't change the original string

# %% New ipython cell ================

## Handling larger texts

f = open('./moby.txt', 'r')
f.readline()

# %% New ipython cell ================

f.seek(0) # goes back to the first line
text12 = f.read()
text12

# %% New ipython cell ================

len(text12)

# %% New ipython cell ================

text13 = text12.splitlines()
len(text13)

# %% New ipython cell ================

text13[0]

# %% New ipython cell ================

# f = open(filename, mode)
# f.readline(); f.read(); f.read(n)
# for line in f: doSomething(line)
# f.seek(n)
# f.write(message)
# f.close()
# f.closed

# %% New ipython cell ================

f = open('./moby.txt', 'r')
text14 = f.readline()
text14

# %% New ipython cell ================

text14.rstrip() # remove the '\n'
