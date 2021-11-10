a1=input()
b1=input()
try:
    a=int(a1)
    b=int(b1)
except ValueError:
    print('Bạn nhập sai kiểu dữ liệu')


tong=lambda a,b: int(a)+int(b)
print(tong(a1,b1))