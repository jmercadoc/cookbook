a = {
    'x': 1,
    'y': 2,
    'z': 3
}


b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print("Find keys in common", a.keys() & b.keys())

print("Find keys in a that are not in b", a.keys() - b.keys())

print("Find (key, value) pairs in common", a.items() & b.items())

c = { key:a[key] for key in a.keys() - {'z','w'}}
print(c)