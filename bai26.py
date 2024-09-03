# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:02:14 2024

@author: Dell
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
        a, b = b, a
if b > c:
        b, c = c, b
if a > b:
        a, b = b, a
print(f"Các số theo thứ tự tăng dần là: {a}, {b}, {c}")
# caub
N = input("Nhập số nguyên N: ")
sap_xep_N = ''.join(sorted(N))
print("Số có các con số theo thứ tự tăng dần: ", sap_xep_N)
