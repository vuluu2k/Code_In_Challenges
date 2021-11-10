# Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu. Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.
ip=int(input())

for x in range(1,ip+1):
    for y in range(1,x+1):
        print(y,end=" ")
    print()