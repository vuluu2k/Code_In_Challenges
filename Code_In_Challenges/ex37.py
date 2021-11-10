# Viết hàm truyền vào tham số là chuỗi s.
# Trả về chuỗi kết quả bằng cách thay thế đuôi "ing" bằng đuôi "ly" nếu chuỗi s kết thúc bằng "ing", nếu không thì thêm đuôi "ing" vào chuỗi s.

ip=input()

if(ip[-3:]=='ing'):
    ip=ip[0:-3]+'ly'
else:
    ip+='ing'
print(ip)