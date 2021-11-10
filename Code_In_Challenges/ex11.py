# Viết chương trình giải phương trình bậc hai với các hệ số được nhập từ bàn phím và hiển thị kết quả ra màn hình.
# Chúng ta chỉ thực hiện với trường hợp nó bậc 2
import math

a,b,c = map(int, input().split())



delta=b*b-4*a*c
if delta<0:
    print ('Phương trình đã cho vô nghiêm')
elif delta==0:
    print ('Phương trình có nghiệm kép %0.2f' %(float(-b/2*a)))
else:
    print ('Phương trình có 2 nghiệm '+ (sqrt(delta)-b)/2*a +'và'+(sqrt(delta)+b)/2*a)
