# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:41:58 2024

@author: Dell
"""

a = print("menu:")
print("1. hủ tieu")
print("2. chao long")
print("3. banh canh")
print("4. bun rieu")
print("5. pho bo")
a = int(input("mời nhập lựa chọn: "))
if a == 1:
    print("hu tieu")
elif a == 2:
    print("chao long")
elif a == 3:
    print("banh canh")
elif a==4:
    print("bun rieu")
elif a == 5:
    print("pho bo")
else:
    print("lua chon khong co trong menu")
