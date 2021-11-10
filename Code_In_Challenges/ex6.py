# Viết chương trình nhập vào từ file input {Tên}, {Tuổi hiện tại} và xuất ra file output theo mẫu sau:
# “Vao 20 nam nua, tuoi cua {Tên} se la {Tuổi cần tìm}”. 

with open('ex6.txt','r') as fileInp:

    ten=fileInp.readline().rstrip('\n')

    tuoiHienTai=int(fileInp.readline())
    fileInp.close()

with open('ex6.txt','a+') as fileOut:

    fileOut.write('\nNext Year, I\'m {name} and {age} years old'.format(name=ten,age=tuoiHienTai+1))
    fileOut.close()