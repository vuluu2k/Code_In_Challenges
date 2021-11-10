# Viết chương trình kiểm tra n có phải số hoàn hoàn thiện (số hoàn hảo) không. Với n là số nguyên dương nhập từ bàn phím.
n=int(input())
s=0
for i in range(1,n//2+1):
    if(n%i==0):
        s+=i
# print(s)
if(n==s):
    print(f'{n} là số hoàn hảo')
else:
    print('Số nhập không là số hoàn hảo')