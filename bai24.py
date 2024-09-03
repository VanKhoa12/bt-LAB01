# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:52:37 2024

@author: Dell
"""

h = int(input("nhập giờ: "))
m = int(input("nhập phút: "))
s = int(input("nhập giây: "))
if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("thòi gian hợp lệ")
else:
        print("thòi gian không hợp lệ")
