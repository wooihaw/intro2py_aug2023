# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:37:23 2023

@author: wooihaw
"""

import statistics as stat

try:
    with open("data/Heathrow.txt", "r") as f:
        raw_data = f.readlines()
except Exception as e:
    print("Error:", e)
else:
    # print(raw_data)
    data = [float(n.strip()) for n in raw_data]
    # print(data)
    data.sort()
    
    n = len(data)
    mean = sum(data) / n
    
    if n % 2 == 1:
        median = data[n//2]
    else:
        median = (data[n//2 - 1] + data[n//2]) / 2
    
    print(f"Lowest: {data[0]}, highest: {data[-1]}")
    print(f"Mean: {mean:.3f}, median: {median}")
    
    print(f"Mean: {stat.mean(data):.3f}, median: {stat.median(data)}")