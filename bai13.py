# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:18:16 2024

@author: Dell
"""

thoi_gian = input("Nhập thời gian theo định dạng ngày tháng năm: ")
a,b,c = map(int, thoi_gian.split(' '))
if 1<=a<=31 and  1<=b<=12 and 1800<=c<=2024:
    print(f"{a}/{b}/{c}")
    print(f"{a}/{b}/",c%100)
    print(f"{c}/{b}/{a}")
else:
    print("ngay thang nam khong hop le")
    
thoi_gian = input("Nhập thời gian theo định dạng ngày/tháng/năm: ")
a,b,c = map(int, thoi_gian.split('/'))
if 1<=a<=31 and  1<=b<=12 and 1800<=c<=2024:
    print(f"{a} {b} {c}")
    print(f"{a} {b} ",c%100)
    print(f"{c} {b} {a}")
else:
    print("ngay thang nam khong hop le")
    
 