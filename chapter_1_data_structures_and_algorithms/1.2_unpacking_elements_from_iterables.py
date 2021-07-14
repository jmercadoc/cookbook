"""
Problem 
    You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too many values to unpack" exception
"""
from statistics import mean

def drop_first_last(grades):

    first, *middle, last = grades

    return mean(middle)


print(drop_first_last((3, 4, 5, 6, 7, 8)))


record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")

name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)


record = ("ACME", 50, 91.1, (2012, 12, 21))

name, *_, (year, *_) = record

print(name)
print(year)

list_items = [1, 10, 7, 4, 5, 9]

def suma(items):
    head, *tail = items
    return head + suma(tail) if len(tail)>0 else head

print("sum(items)", suma(list_items))