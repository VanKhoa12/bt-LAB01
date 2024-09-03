# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:43:03 2024

@author: Dell
"""

a = float(input("Nhập số nguyên a: "))
b = float(input("Nhập số nguyên b: "))
c = float(input("Nhập số nguyên c: "))
so_lon = a
if b > so_lon:
   so_lon = b
if c > so_lon:
    so_lon = c
print(f"Số nhỏ nhất là: {so_lon}")