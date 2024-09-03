# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:19:40 2024

@author: Dell
"""

hinh = input("Nhap vao hinh (vuong), (chu nhat), (hinh tron): ")
if hinh == 'vuong':
    c = float(input("Nhap chieu dai canh: "))
    cv = 4 * c
    print("Ket qua chu vi hinh vuong la: ", cv)
    s = c ** 2
    print("Ket qua dien tich hinh vuong la: ", s)
elif hinh == 'chu nhat':
    rong = float(input("Nhap vao chieu rong: "))
    dai = float(input("Nhap vao chieu dai"))
    cv = 2 * (rong + dai)
    print("Chu vi hinh chu nhat la: ", cv)
    s = rong * dai
    print("Dien tich hinh chu nhat la: ", s)
elif hinh == 'hinh tron':
    ban_kinh = float(input("Nhập bán kính: "))
    cv = 2 * 3.14 * ban_kinh
    print("Ban kinh hinh tron la: ", ban_kinh)
    s = 3.14 * (ban_kinh ** 2)
    print("Dien tich hinh tron la: ", s)
else:
       print("Hinh khong hop le")
       