# Viết hàm trả về tổng các số từ 1 đến n (Dùng đệ quy). Với tham số là số tự nhiên n.

def dequy(n):
    if(n==1):
        return 1
    return n+dequy(n-1)
print(dequy(20))