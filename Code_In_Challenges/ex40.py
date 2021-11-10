# Viết hàm truyền vào tham số là chuỗi s.
# Nếu ký tự đầu và ký tự cuối của chuỗi s là "*" (hoặc "-") thì  trả về chuỗi s với định dạng title() (hoặc swapcase()). 
# Các trường hợp còn lại trả về chuỗi s với định dạng capitalize().

def bien_doi_chuoi(s):
   if s.startswith('*') and s.endswith('*'):
       return s.title()
  
   if s.startswith('-') and s.endswith('-'):
       return s.swapcase()
      
   return s.capitalize()

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
print(bien_doi_chuoi(s))