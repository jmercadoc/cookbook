import unicodedata


s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)

print(s1 == s2)
print(len(s1))
print(len(s2))

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)

print(t1 == t2)