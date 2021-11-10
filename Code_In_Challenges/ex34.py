# Viết hàm truyền vào tham số là hai chuỗi s1 và s2. 
# Kiểm tra chuỗi s2 có xuất hiện trong chuỗi s1 không, nếu không thì hiển thị thông báo, nếu có thì hiển thị số lần xuất hiện.

s1="Xin Chao"
s2="Chao"

def ex34(s1,s2):
    if(s1.count(s2)>0):
        print(s1.count(s2))
    else :
        print(f'{s1} not in {s2}')

ex34(s1,s2)