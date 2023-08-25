# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:16:57 2023

@author: wooihaw
"""

# c - number of chickens
# r - number of rabbits
# c + r = 35
# 2*c + 4*r = 94

for c in range(36):
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f"There are {c} \N{chicken} and {r} \N{rabbit} in the farm.")