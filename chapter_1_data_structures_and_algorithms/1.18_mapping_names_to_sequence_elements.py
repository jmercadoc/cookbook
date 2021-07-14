"""
Problem
    You have code that access list or tuple element by position, but this
    makes the code somewhat difficult to read at times. You'd also like to be
    less dependent on position in the structure, by accessing the elements by name.
"""

from collections import namedtuple

Suscriber = namedtuple('Suscriber', ['addr', 'joined'])

sub = Suscriber('jones@example.com', '2012-10-19')

print(sub)
print(sub.addr)
print(sub.joined)

addr, joined = sub
print('addr', addr)
print('joined', joined)

# Dictionary to namedtuple with replace method

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = { 'name': 'ACME', 'shares': 100, 'price': 123.45 }

print(dict_to_stock(a))