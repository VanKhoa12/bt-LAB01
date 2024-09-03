# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:43:15 2024

@author: Dell
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
so_nho = a
if b < so_nho:
   so_nho = b
if c < so_nho:
    so_nho = c
if d < so_nho:
    so_nho = d
print(f"Số nhỏ nhất là: {so_nho}")