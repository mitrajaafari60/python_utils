import collections
n= int(input())
list =[]
for i in range(0,n):
    list.append(input())

ol= collections.OrderedDict()
for i in range(0,n):
    ol[list[i]]= ol.get(list[i],0)+1
for k in sorted(ol):
    print("%s %s"%(k,ol[k]))



