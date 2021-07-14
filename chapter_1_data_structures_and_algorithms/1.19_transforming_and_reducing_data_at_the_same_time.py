"""
Problem
    You need to execute a reduction function (e.g. sum(), min(), max()), but first
    need transform or filter the data.
"""


nums = [1, 2, 3 , 4, 5]
s = sum(n * n for n in nums)
print(s)



import os
files = os.listdir()
if any( name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')



s = ('ACME', 50, 123.45)
print(','.join( str(v) for v in s) )

