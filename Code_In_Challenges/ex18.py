# Viết chương trình tính và hiển thị ra màn hình n giai thừa (n!). Với n là số tự nhiên nhập từ bàn phím.

ip=int(input())
giaithua=1
for x in range(1,ip+1):
    giaithua*=x
print(giaithua)

# Giải với đệ quy
def giaithuaDeQuy(ip):
    if(ip==0):
        return 1
    return ip*giaithuaDeQuy(ip-1)
print(giaithuaDeQuy(ip))