# Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ,
# dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng. Tính tổng của dãy số và hiển thị ra màn hình.

ip= input("Nhập dãy số cách nhau bởi khoảng trắng: ")

items=[x for x in ip.strip().split(' ')]
print(items)
s=0
for number in items:
    s+=int(number)
print(s)