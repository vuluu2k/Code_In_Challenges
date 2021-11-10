# Viết chương trình nhập vào từ file input một câu chào hỏi làm quen với độ dài bất kỳ,
# mỗi từ nằm trên một dòng. Xuất ra file output câu chào hỏi vừa nhận được trên 1 dòng duy nhất, các từ cách nhau 1 khoảng trắng. 

with open('ex7.txt','r') as file_input:
    items=file_input.read().split('\n')
with open('ex7.txt','w') as file_output:
    file_output.write((' ').join(items))