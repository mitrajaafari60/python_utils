n= int(input())
list2 =[]
for i in range(0,n):
    list= input()
    m= list.split()
    a1= int(m[0])
    a2= int(m[1])
    b=[a1,a2]
    list2.append(b)

found=False
for x in range(0,n):
    for y in range(x,n):
        if list2[x][0] < list2[y][0] and list2[x][1] > list2[y][1]:
            found=True
            break


if found:
    print("happy irsa")
else:
    print("poor irsa")
    
