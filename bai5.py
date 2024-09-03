# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:03:48 2024

@author: Dell
"""

thoi_gian = input("Nhập thời gian theo định dạng hh:mm:ss: ")
h, m, s = map(int, thoi_gian.split(':'))
tong = h * 3600 + m * 60 + s
print(f"Tổng số giây là: {tong}")
