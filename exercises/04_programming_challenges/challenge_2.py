# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:22:56 2023

@author: wooihaw
"""

try:
    investment = float(input("Enter the initial investment: "))
    rate = float(input("Enter the annual rate: "))
    years = int(input("Enter the years of investment: "))
except:
    print("Invalid input value!")
else:
    print(f"Initial investment: RM{investment:.2f}, annual rate: {rate:.2f}%, years of investment: {years}")
    for y in range(years):
        investment = investment + investment * rate/100
        print(f"Year {y+1}: RM {investment:.2f}")
