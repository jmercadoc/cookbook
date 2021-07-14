text = 'yeah, but no, but yeah, but no, but yeah'
url = 'https://lair-store.s3.amazonaws.com/recursos/logos/numenera+reveries+of+the+ninth+world+-+3d+printable+files+by+lair_license.png'
print("numenera2--->", url.find('numenera2'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

print(datepat.findall(text3))
