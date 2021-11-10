# Viết hàm truyền vào tham số là chuỗi s và hai số tự nhiên a, b (a <= b). 
# Trả về chuỗi con đảo ngược từ vị trí a đến vị trí b của chuỗi s (vị trí của chuỗi bắt đầu từ 0).
# Đây là gợi cho bạn viết hàm
s1='Hello Anh Em'
a=1
b=6
items=list(s1)
print(('').join(items[a:b+1][::-1]))