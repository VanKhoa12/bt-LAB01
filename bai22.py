# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:04:24 2024

@author: Dell
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a != 0:
        x = -b / a
        print(f"Phương trình có nghiệm duy nhất: x = {x}")
else:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình không có nghiệm.")
