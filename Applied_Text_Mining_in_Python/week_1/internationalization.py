# ASCII: American Standard Code for Information Interchange
# 7-bit character encoding standar: 128 valid codes
# To encode more characters, we need a larger codification.

# %% New ipython cell ================

# Some other characters encodings are:
# * IBM EBCDIC
# * Latin-1
# * JIS: Japanese Industrial Standards
# * CCCII: Chinese Character Code for information Interchange
# * EUC: Extended Unix Code
# * Numerous other national standards

# * Unicode and UTF-8
# Today, Unicode is the most used encoding.

# %% New ipython cell ================

# It has over 128,000 characters from 130+ scripts and symbol sets (like greek
# symbols, card symbols and so on)

# It can be implemented by different character endings:
# - UTF-8: Goes one byte to up to four bytes
# - UTF-16: One or two 16-bit code units
# - UTF-32: One 32-bit code unit

# UTF-8 stands for Unicode Transformation Format - 8-bits
# It has variable length encoding: one to four bytes
# It has backward compatibility with ASCII
# - One byte codes are the same as ASCII
# It's the dominant character encoding for the Web
# It's the default encoding in Python3
# In Python2, you must use a 'u' before the string, like: u'Résumé'
