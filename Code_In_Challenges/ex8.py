# Viết chương trình nhập vào từ bàn phím tên và chiều cao (cm) của hai bạn. 
# Hiển thị ra màn hình thông báo bạn nào cao hơn.

class Person:
    def __init__(self,name,tall):
        self.name = name
        self.tall =tall
People1=Person(input('Nhập tên bạn thứ nhất: '),float(input('Nhập chiều cao bạn thứ nhất: ')))
People2=Person(input('Nhập tên bạn thứ hai: '),float(input('Nhập chiều cao bạn thứ hai: ')))
if(People1.tall>People2.tall):
    print('{} Cao hơn {}'.format(People1.name,People2.name))
else:
    print('{} Cao hơn {}'.format(People2.name,People1.name))
