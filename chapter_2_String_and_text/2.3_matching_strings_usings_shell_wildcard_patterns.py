from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '?oo.txt'))

print(fnmatch('Dat1.csv', 'Dat[0-9]*.csv'))
