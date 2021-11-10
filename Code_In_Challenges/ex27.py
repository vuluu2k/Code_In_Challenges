# Viết hàm hiển thị ra màn hình câu sau: “Xin chao! Toi la {Ten}, toi {Tuoi} tuoi.”. Với tham số là {Ten} và {Tuoi}.
# Sử dụng hàm
def hello(name,age):
    print('Hello! I\'m {name} and {age} years old'.format(name=name, age=age))

# Các viết thông thường
Ten, Tuoi= input('Nhập tên của bạn: '),input('Nhập tuổi của bạn: ')
print('Xin chào! Tôi là {Ten}, tôi {Tuoi} tuổi.'.format(Ten=Ten,Tuoi=Tuoi))
hello(Ten, Tuoi)