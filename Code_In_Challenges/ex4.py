# Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy.
# A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.

a=float(input())
b=int(input())

print('{a:.{b}f}'.format(a=a,b=b))
