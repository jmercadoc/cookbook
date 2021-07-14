"""
Problem

    You want to eliminate the duplicate values in a sequence, but preserve the orden of the remaining items
"""


def dedupe(items):
    seen = set()

    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]


print(list(dedupe(a)))


def dedupe2(items, key=None):
    seen = set()

    for item in items:
        val = item if key is None else key(item)

        if val not in seen:
            yield item
            seen.add(val)

b = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(list(dedupe2(a)))

print(list(dedupe2(b, key=lambda d: (d['x'],d['y']) )))

print(list(dedupe2(b, key=lambda d: d['x'] )))