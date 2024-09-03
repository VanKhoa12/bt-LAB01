# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:01:13 2024

@author: Dell
"""

bien = input(" nhập vào số xe cua ban ( 4 số): ")
a = int(bien[0])
b = int(bien[1])
c = int(bien[2])
d = int(bien[3])
if len(bien)==4 and d>0:
    n = (a + b + c + d) % 10
    print("số nút của xe bạn là: ",n)
else:
    print("so xe khong hop le: ")
    
