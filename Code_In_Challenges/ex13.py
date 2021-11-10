# Viết chương trình nhập vào bàn phím hai số nguyên a và b (a <= b).
#  Tính và hiển thị ra màn hình tổng các số trong khoảng a đến b. Yêu cầu sử dụng vòng lặp for.
#Cách1
a,b=map(int,input().split())
s=0
s1=0
for x in range(a,b+1):
    s+=x
print(s)
#Cach2
while a<=b:
    s1+=a
    a+=1
print(s1)