import math

n= int(input())
list =[]
for i in range(0,n):
    list.append(int(input()))

for i in range(0,n):
    num= float(math.sqrt(list[i]))
    i_part = int(num)
    f_part = num - i_part
    str1= str(f_part)
    if str1=="0.0":
        str1="0.0000"
    str2=str(i_part)+"."+str1[2:6]
    print(str2)