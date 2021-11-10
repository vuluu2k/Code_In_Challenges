# Viết hàm trả về từ có độ dài lớn nhất trong chuỗi s. 
# Với tham số truyền vào là chuỗi s. Nếu có nhiều từ có độ dài bằng nhau thì trả về từ có thứ tự nhỏ hơn (sắp xếp theo bảng chữ cái).

def tu_dai_nhat(s):
   #Bien luu tu dai nhat
   tuDaiNhat = ""
   #Su dung phuong thuc split() de cat chuoi s thanh cac tu ngan cach bang khoang trang
   dsCacTu = s.split()
   #Su dung vong lap for de duyet cac tu trong danh sach cac tu cua chuoi s
   for tu in dsCacTu:
       #So sanh do dai cac tu voi do dai tuDaiNhat hien tai
       #Neu do dai bang voi tuDaiNhat thi so sanh theo thu tu bang chu cai
       if (len(tu) > len(tuDaiNhat)) or (len(tu) == len(tuDaiNhat) and tu < tuDaiNhat):
           tuDaiNhat = tu
      
   return tuDaiNhat

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
print(tu_dai_nhat(s))