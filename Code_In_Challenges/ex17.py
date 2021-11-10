# Viết chương trình hiển thị ra màn hình tam giác cân chứa các ký tự alphabet kích thước n theo mẫu. 
# Với n là số tự nhiên nhập từ bàn phím.

ip=int(input())
maAscii=65
for x in range(ip):
    space=" "*((ip-x)*2-1)
    print(space,end=' ')
    for y in range(2*x+1):
        char=chr(maAscii)
        print(char,end=' ')
        maAscii+=1
        if(chr(maAscii)>'Z'):
            maAscii=65
    print()

