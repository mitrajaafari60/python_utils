n= int(input())
l=input()
mem=l.split()
count=0

for m in mem:
    i=int(m)
    if i<=2:
        count=count+1

print(count//3)