# Viết chương trình nhập vào ba số a, b, c.
# Hiển thị ra màn hình cho biết a, b, c có là ba cạnh của một tam giác hay không.

a,b,c=map(float,input().split())
# print (a,b,c,sep='--')
if a+b>c and a+c>b and b+c>a:
    print("{}, {}, {} la ba canh cua mot tam giac".format(a, b, c))
else:
    print("{}, {}, {} khong la ba canh cua mot tam giac".format(a, b, c))


