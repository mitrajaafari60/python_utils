import collections
n= int(input())
ol= collections.OrderedDict()

for i in range(0,n):
    l=input()
    a=l.split()
    ol[a[0]]=a[1]

string = input()
b = string.split()

for word in b:
    if word in ol:
        print(ol[word],end=" ")
    else:
        print(word,end=" ")