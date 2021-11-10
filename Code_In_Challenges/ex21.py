# Viết chương trình tính và hiển thị ra màn hình tích của tổng các chữ số 
# chẵn và tổng các chữ số lẻ của một số tự nhiên nhập từ bàn phím.

n=int(input())
Schan=0
Sle=0
while n>0:
    if(n%2==0):
        Schan+=n%10
    else:
        Sle+=n%10
    n=n//10
print(Schan*Sle)
