# Viết chương trình hiển thị ra màn hình bảng cửu chương n. Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.
# Ở đây mình in ra là list kết quả cửu chương nha
ip=int(input('Nhập số bạn muốn: '))
items=[ip*x for x in range(1,11)]
print(items)
