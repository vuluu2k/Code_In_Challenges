# Viết hàm truyền vào tham số là hai chuỗi s1 và s2. 
# Trả về chuỗi kết quả bằng cách đan xen lần lượt ký tự đầu của chuỗi s1 và ký tự cuối của chuỗi s2 cho đến hết chuỗi.

def danxen(s1,s2):
    s2re=s2[::-1]
    maxLenStr=max(len(s1),len(s2))
    # print(maxLenStr)
    chuoiDanXen=""
    for i in range(maxLenStr):
        if(i<len(s1)):
            chuoiDanXen+=s1[i]
        if(i<len(s2)):
            chuoiDanXen+=s2re[i]
    return chuoiDanXen

s1 = input()
s2 = input()

print(danxen(s1,s2))