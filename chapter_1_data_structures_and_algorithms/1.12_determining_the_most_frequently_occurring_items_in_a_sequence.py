"""
Problem
    You have a sequence of items, and you'd like to determinate the most
    frequently occuring items in the sequence
"""


words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look',  'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under']

from collections import Counter

word_counts = Counter(words)

print(word_counts)