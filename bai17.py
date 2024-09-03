# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:31:50 2024

@author: Dell
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
so_nho = min(a, b, c)
so_lon = max(a, b, c)
print("Số lớn nhất là: ",so_lon)
print("Số nhỏ nhất là: ",so_nho)