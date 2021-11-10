# Viết hàm tính số Fibonacci thứ n (Dùng đệ quy). Với tham số là số tự nhiên n.

def dequy(n):
    if(n==1 or n==2):
        return 1
    return dequy(n-1)+dequy(n-2) # đây chính là tổng của n
print(dequy(38))

# ex22