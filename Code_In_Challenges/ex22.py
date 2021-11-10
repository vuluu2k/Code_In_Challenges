# Viết chương trình tính và hiển thị dãy số Fibonacci thứ n. Với n là số tự nhiên nhập từ bàn phím
# Làm theo tư duy bình thường
n=int(input('Nhập giá trị đầu vào cho n: '))

a,next_a=1,1
print(next_a)
for i in range(n-2):
    a,next_a=next_a,a+next_a
    print(next_a)
