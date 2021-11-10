# Viết hàm liệt kê các số hoàn thiện nhỏ hơn n (Có gọi hàm kiểm tra số hoàn thiện). Với tham số tự nhiên n.

def check(n):
    s=0
    for i in range(1,n//2+1):
        if(n%i==0):
            s+=i
    if(n==s):
        print(n,end=" ")

n=int(input('Nhập n: '))

for i in range(1,n):
    if(i>1):
        check(i)