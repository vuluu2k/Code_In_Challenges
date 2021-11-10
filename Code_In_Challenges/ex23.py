# Viết chương trình hiển thị ra màn hình tất cả các ước của một số tự nhiên n nhập từ bàn phím.

n=int(input('Nhập số tính ước: '))


for i in range(1,n+1):
    if(n%i==0):
        print(i,end="\n")
