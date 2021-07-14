filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.com'

print(url.startswith('http:'))

import os

filenames = os.listdir('.')
print(filenames)
files = [name for name in filenames if name.endswith('.py')]

print(files)

print('any', any(name.endswith('.py') for name in filenames))