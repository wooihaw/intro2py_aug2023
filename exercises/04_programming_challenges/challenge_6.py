# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:57:26 2023

@author: wooihaw
"""

class Circle:
    __pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.__pi * self.radius ** 2
    def circumference(self):
        return 2 * Circle.__base__pi * self.radius

c1 = Circle(4)
print(f"Area: {c1.area()}, circumference: {c1.circumference()}")
