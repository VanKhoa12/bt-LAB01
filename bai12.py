# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:07:09 2024

@author: Dell
"""

import random
def generate_random(a, b,is_float =False):
    if is_float:
       return random.uniform(a, b)
    else:
         return random.randint(int(a), int(b))
is_float_a = random.choice([True, False]) 
number_a = generate_random(0, 100, is_float=is_float_a)
print(f"Số ngẫu nhiên từ 0 đến 100 (nguyên hoặc thực): {number_a}")

is_float_b = random.choice([True, False])
number_b = generate_random(50, 99, is_float=is_float_b)
print(f"Số ngẫu nhiên từ 50 đến 99 (nguyên hoặc thực): {number_b}")

is_float_c = random.choice([True, False])
number_c = generate_random(-39, 79, is_float=is_float_c)
print(f"Số ngẫu nhiên từ -39 đến 79 (nguyên hoặc thực): {number_c}")


is_float_d = random.choice([True, False])
number_d = generate_random(-79, -39, is_float=is_float_d)
print(f"Số ngẫu nhiên từ -79 đến -39 (nguyên hoặc thực): {number_d}")
