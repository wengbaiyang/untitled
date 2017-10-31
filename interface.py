import os
print os.getcwd()

# print dir(os)
# # help(os)

import glob
print glob.glob('*.txt')

# This is a very fanny function, without doing anything, the result will change everytime
import random
print random.choice(['apple', 'pear', 'banana'])
print random.random()
print random.randrange(10)

from datetime import date
now = date.today()
print date.today().strftime("%m-%d-%y, %d %b %Y is a %A on the %d day of %B")
birthday = date(1996, 3, 24)
age = now - birthday
print age

import zlib
s = b'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(zlib.compress(s))
print zlib.decompress(t)

import doctest
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>>print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

print average([10, 20, 30])