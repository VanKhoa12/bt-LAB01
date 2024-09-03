# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:18:01 2024

@author: Dell
"""
import math
a = float(input("nhap a: "))
b = float(input("nhap b: "))
s = (a + b) / (math.sqrt(a) + math.sqrt(b)) - 3 * math.sqrt(a * b)
print("dap an la: ",s)

