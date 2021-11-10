# Viết hàm tính tổng các số với số lượng bất kỳ (Tham số là *agrs).


def tinhtong(*args):
    tong=0
    for so in args:
        tong+=so
    return tong

print('Tông số muốn chạy là: ',tinhtong(3,4,5))