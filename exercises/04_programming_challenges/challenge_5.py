# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:53:36 2023

@author: wooihaw
"""

def convert_cel_to_far(C):
    return C * 9/5 + 32

def convert_far_to_cel(F):
    return (F - 32) * 5/9

f = float(input("Enter a temperature in degrees Fahrenheit: "))
print(f"The temperature converted to Celsius: {convert_far_to_cel(f):.2f}")

c = float(input("Enter a temperature in degrees Celsius: "))
print(f"The temperature converted to Fahrenheit: {convert_cel_to_far(c):.2f}")