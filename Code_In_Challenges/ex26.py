# Viết chương trình nhập vào từ bàn phím hai số tự nhiên a và b (a <= b). Hiển thị ra màn hình các số nguyên tố trong đoạn từ a đến b.

from math import sqrt

def check(a):
    for i in range(2,int(sqrt(a)+1)):
        if(a%i==0):
            break
    else:
        print(a,end=" ")
        
a,b = map(int, input().split())

for i in range(a,b+1):
    if(i>2):
        check(i)