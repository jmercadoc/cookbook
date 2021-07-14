"""
Problem 
    You have an N-element tuple or sequence that you  would like to unpack into a collection of N variables
"""

p = ( 4, 5, 6)

x, y, z = p

print("x", x)
print("y", y)
print("z", z)

data = ["ACME", 50, 91.1, (2012, 12, 21)]

name, shares, price, (year, mon, day) = data

print("name", name)
print("shares", shares)
print("price", price)
print("year", year)
print("mon", mon)
print("day", day)

s = 'Hello'

a, b, c, d, e = s

print(a)
print(b)
print(c)
print(d)
print(e)

"""Unpacking actually works wwith any object that happens iterable..."""