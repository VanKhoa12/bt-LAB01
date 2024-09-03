# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:16:27 2024

@author: Dell
"""

a = input("Nhập một chữ cái: ")
if a.islower():
    a = a.upper()
else:
    a = a.lower()
print("in ra:", a)

    