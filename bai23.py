# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:23:47 2024

@author: Dell
"""

import math
print("Giải phương trình bậc hai")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a!=0:
    delta= b**2 - 4*a*c
    if (delta<0):
        print("Phương trình vô nghiệm")
    elif (delta==0):
        x = -b/(2*a)
        print("Có nghiệm kép x1=x2=", x)
    else :
        x1 = (-b-(math . sqrt(delta)))/(2*a)
        x2 = (-b+(math . sqrt(delta)))/(2*a)
        print("Có hai nghiệm phân biệt x1={0}, x2={1}", format(x1, x2))
else :
        print("Phương trình có hai nghiệm phân biệt")