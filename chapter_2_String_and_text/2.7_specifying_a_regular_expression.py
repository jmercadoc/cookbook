import re

str_pat = re.compile(r'\"(.*)\"')

text1 = 'Couter says "no."'

print(str_pat.findall(text1))

text1 = 'Couter says "no." Phone says "yes."'

print(str_pat.findall(text1))

str_pat = re.compile(r'\"(.*?)\"')

print(str_pat.findall(text1))
