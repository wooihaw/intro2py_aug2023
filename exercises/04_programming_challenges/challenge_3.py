# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:32:34 2023

@author: wooihaw
"""

s1 = set(range(1, 101))  # Set of numbers from 1 to 100
s2 = set(range(5, 101, 5))  # Set of numbers divisible by 5
s3 = set(range(7, 101, 7))  # Set of numbers divisible by 7

answer = s1 - (s2 | s3)
print(answer)