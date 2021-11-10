# Tạo tam giác ngược với ex15

ip=int(input())
for x in range(ip):
    for y in range(ip-x,0,-1):
        print(y,end=" ")
    print()
