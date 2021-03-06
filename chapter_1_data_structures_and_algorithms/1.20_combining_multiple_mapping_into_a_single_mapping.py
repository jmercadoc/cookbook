"""
Problem
    You have a multiple dictionaries or mapping that ypu want to logically
    combine into a single mapping to perform certain operations, such as
    looking up values or checking for the existence of keys 
"""

a = {'x': 1 ,'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap

c = ChainMap(a, b)

print(c['x'])
print(c['y'])
print(c['z'])

del(c['x'])
print(a)
print(c)