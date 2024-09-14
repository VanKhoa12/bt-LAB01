# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:40:27 2024

@author: Dell
"""

gio1 = int(input("Nhập giờ của thời gian thứ nhất: "))
phut1 = int(input("Nhập phút của thời gian thứ nhất: "))
giay1 = int(input("Nhập giây của thời gian thứ nhất: "))
gio2 = int(input("Nhập giờ của thời gian thứ hai: "))
phut2 = int(input("Nhập phút của thời gian thứ hai: "))
giay2 = int(input("Nhập giây của thời gian thứ hai: "))
phep_toan = input("Nhập phép toán (+ hoặc -): ")
tong_giay1 = gio1 * 3600 + phut1 * 60 + giay1
tong_giay2 = gio2 * 3600 + phut2 * 60 + giay2
if phep_toan == "+":
      tong_giay = tong_giay1 + tong_giay2
else:
      tong_giay = tong_giay1 - tong_giay2
gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60
print("Kết quả:",gio, "giờ",phut, "phút",giay, "giây")
