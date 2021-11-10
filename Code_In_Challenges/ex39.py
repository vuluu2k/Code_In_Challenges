# Viết hàm truyền vào tham số là chuỗi s. Nếu ký tự đầu của chuỗi s là ký tự viết thường (hoặc viết hoa) 
# thì trả về chuỗi s với tất cả ký tự được chuyển thành viết thường (hoặc viết hoa). Các trường hợp khác trả về chuỗi s.

ip=input()
if('A'<ip<'Z'):
    print(ip.upper())
elif('a'<ip<'z'):
    print(ip.lower())
else:
    print(ip)