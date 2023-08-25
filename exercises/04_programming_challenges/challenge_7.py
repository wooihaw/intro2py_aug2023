# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:03:02 2023

@author: wooihaw
"""

from collections import Counter

try:
    with open("data/alice.txt", "r") as f:
        s = f.read()
except Exception as e:
    print("Error: ", e)
else:
    t = [c.lower() if c.isalpha() else ' ' for c in s]
    u = ''.join(t)
    # print(u)
    w = u.split()
    # print(w)
    count = Counter(w)
    
    print(f"Number of unique words: {len(count)}")
    print(f"Ten most common words: {count.most_common(10)}")
    print(f"The word 'alice' appears {count['alice']} times in the text file.")