# Viết hàm truyền vào tham số là hai chuỗi s1 và s2. 
# Trả về chuỗi kết quả bằng cách nối 2 chuỗi s1 và s2 sau khi được xử lý như sau: 
# nếu độ dài chuỗi nào nhỏ hơn 5 thì lặp lại chuỗi đó 3 lần.

def chuoi_ket_qua(s1, s2):
   #Su dung ham len de tra ve do dai chuoi
   if len(s1) <= 5:
       #Su dung toan tu * de tao chuoi lap lai
       s1 = s1*3
   if len(s2) <= 5:
       s2 = s2*3
   #Su dung toan tu + de noi cac chuoi
   return s1 + s2

#Nhap cac chuoi tu ban phim
s1 = input()
s2 = input()

#Goi ham xu ly va truyen cac tham so can thiet
print(chuoi_ket_qua(s1, s2))