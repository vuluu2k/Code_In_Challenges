# Viết hàm truyền vào tham số là chuỗi s. Trả về số lượng các ký tự nguyên âm và chuỗi s sau khi đã thay thế các ký tự nguyên âm bằng ký tự "$".


def thay_the_nguyen_am(s):
   #Liet ke cac ky tu nguyen am
   nguyenAm = "ueoaiUEOAI"
   tongNguyenAm = 0
   #Duyet qua tung ky tu nguyen am
   for c in nguyenAm:
       #Dem cac ky tu nguyen am va cong don vao tong
       tongNguyenAm += s.count(c)
       #Thay the cac ky tu nguyen am thanh ky tu "$"
       s = s.replace(c, '$')
   return tongNguyenAm, s

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
soLuongNguyenAm, chuoiKetQua = thay_the_nguyen_am(s)

#In ket qua
print(soLuongNguyenAm)
print(chuoiKetQua)