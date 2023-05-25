from collections import OrderedDict


numbers = OrderedDict()
lastNum = 1
for i in range(0,10):
    n= int(input())
    if n> lastNum:
        lastNum=n
    numbers[n]=0

sorted_nums= OrderedDict(sorted(numbers.items(), key=lambda x: x[0],reverse=True))
list=[]
for num in range(2, lastNum-1 ):
   # all prime numbers are greater than 2 till maxNumber-1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list.append(num)


for key, value in sorted_nums.items():
    for i in list:
        if key <= i:
            break
        elif (key%i)==0:
            value +=1
    sorted_nums[key]=value

pre_sorted_nums= OrderedDict(sorted(sorted_nums.items(), key=lambda x: x[1],reverse=True))

result = pre_sorted_nums.popitem(False)
print(result[0],result[1])
