import math

num = math.sqrt(4)
i_part = int(num)
print(i_part)
f_part = float(num - i_part)
print(f_part)
str1= str(f_part)
if str1=="0.0":
    str1="0.0000"
str2=str(i_part)+"."+str1[2:6]
print(str1)
print(str2)  # 2.2360
