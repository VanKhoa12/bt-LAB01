# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:45:20 2024

@author: Dell
"""
n = int(input("Nhập vào số nguyên dương có 2 chữ số: "))
if 10 <= n <= 99:
    hang_chuc = n // 10  
    hang_don_vi = n % 10
    tong = hang_chuc + hang_don_vi
    print(f"{n} = {hang_chuc} + {hang_don_vi} = {tong}")

else:
    print("Vui lòng nhập một số nguyên dương có 2 chữ số.")
    
