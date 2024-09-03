# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:55:27 2024

@author: Dell
"""
def doc_so(n):
  """Hàm đọc số từ 0 đến 9"""
  so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
  if 0 <= n <= 9:
    return so_chu[n]
  else:
    return "Không đọc được"
n = int(input("Nhập một số: "))
ket_qua = doc_so(n)
print(ket_qua)
