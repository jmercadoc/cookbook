"""
Problem
    You need to split a string into fields, but the delimiters
    aren't consistent throughout the string
"""

line = "asdf fdjk]; afed, fjek,asdf,     foo"
import re

print(re.split(r'[;,\s]\s*', line))
