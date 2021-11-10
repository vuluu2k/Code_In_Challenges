# Viết chương trình kiểm tra n có phải số nguyên tố không. Với n là số tự nhiên nhập từ bàn phím.
from math import sqrt

n=int(input())

for i in range(2,int(sqrt(n)+1)):
    if(n%i==0):
        print(f'{n} không phải số nguyên tố')
        break
else:
    print(f'{n} là số nguyên tố')